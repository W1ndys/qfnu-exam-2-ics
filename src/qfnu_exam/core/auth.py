"""认证模块 - 处理教务系统登录"""

import base64
import re
import requests
from typing import Tuple, Optional

from .config import Config


class QFNUAuth:
    """曲阜师范大学教务系统认证类"""

    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()
        self.session: Optional[requests.Session] = None
        self.cookies: Optional[dict] = None

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": self.config.base_url,
            "Referer": f"{self.config.base_url}/",
        }

    def _get_encoded_payload(self, username: str, password: str) -> str:
        """生成加密的 encoded 字段（base64编码）"""
        try:
            account_b64 = base64.b64encode(username.encode()).decode()
            password_b64 = base64.b64encode(password.encode()).decode()
            return f"{account_b64}%%%{password_b64}"
        except Exception:
            return ""

    def get_initial_session(self) -> Tuple[requests.Session, dict, str]:
        """
        创建会话并访问登录页获取初始Cookie
        返回: (session对象, cookies字典, 空字符串-兼容旧接口)
        """
        self.session = requests.Session()

        # 先访问登录页获取 JSESSIONID
        try:
            self.session.get(
                f"{self.config.base_url}/jsxsd/",
                headers=self.headers,
                timeout=10,
            )
        except Exception:
            pass

        self.cookies = self.session.cookies.get_dict()
        return self.session, self.cookies, ""

    def get_captcha_bytes(self) -> bytes:
        """
        获取验证码图片字节数据
        返回: 图片字节数据
        """
        if not self.session:
            raise RuntimeError("请先调用 get_initial_session()")

        response = self.session.get(
            self.config.captcha_url,
            headers=self.headers,
            timeout=10
        )

        if response.status_code != 200:
            raise RuntimeError("无法获取验证码")

        # 检查是否返回的是图片而非HTML
        content = response.content
        if content[:20].lower().startswith((b'<!doctype', b'<html')):
            raise RuntimeError("验证码获取失败，请重试")

        return content

    def login(self, user_account: str, user_password: str, captcha_code: str) -> requests.Response:
        """
        执行登录操作
        """
        if not self.session:
            raise RuntimeError("请先调用 get_initial_session()")

        encoded = self._get_encoded_payload(user_account, user_password)

        data = {
            "userAccount": "",
            "userPassword": "",
            "RANDOMCODE": captcha_code,
            "encoded": encoded,
        }

        return self.session.post(
            self.config.login_url,
            data=data,
            headers=self.headers,
            timeout=10
        )

    def verify_login(self, username: str) -> bool:
        """
        验证登录是否成功（通过访问用户信息页）
        """
        if not self.session:
            return False

        try:
            response = self.session.get(
                self.config.user_info_url,
                headers=self.headers,
                timeout=10
            )
            # 如果能获取到用户信息页面且包含学号或"退出"，说明登录成功
            return username in response.text or "退出" in response.text
        except Exception:
            return False

    def get_exam_page(self) -> requests.Response:
        """
        获取考试安排页面内容
        流程：
        1. GET 请求考试安排查询页，解析获取默认学期
        2. POST 请求考试安排列表页，获取考试数据
        """
        if not self.session:
            raise RuntimeError("请先完成登录")

        # 第一步：GET 请求获取默认学期
        query_response = self.session.get(
            self.config.exam_query_url,
            headers=self.headers,
            timeout=30
        )

        # 解析 HTML 获取默认学期（查找 select 中被选中的 option）
        semester = self._parse_default_semester(query_response.text)

        # 第二步：POST 请求获取考试安排数据
        data = {
            "xqlbmc": "",
            "sxxnxq": "",
            "dqxnxq": "",
            "ckbz": "",
            "xnxqid": semester,
            "xqlb": "",
        }

        return self.session.post(
            self.config.exam_list_url,
            data=data,
            headers=self.headers,
            timeout=30
        )

    def _parse_default_semester(self, html: str) -> str:
        """
        从考试安排查询页 HTML 中解析默认学期
        查找 <select id="xnxqid"> 中被 selected 的 option 的 value
        """
        # 使用正则表达式匹配被选中的 option
        # 匹配模式：<option selected value="2025-2026-1">
        pattern = r'<option\s+selected\s+value="([^"]+)"'
        match = re.search(pattern, html)
        if match:
            return match.group(1)

        # 备用匹配：<option value="2025-2026-1" selected>
        pattern_alt = r'<option\s+value="([^"]+)"\s+selected'
        match_alt = re.search(pattern_alt, html)
        if match_alt:
            return match_alt.group(1)

        # 如果都没有匹配到，返回空字符串（让服务器使用默认值）
        return ""
