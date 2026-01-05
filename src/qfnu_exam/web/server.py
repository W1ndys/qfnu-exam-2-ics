"""Web服务器模块 - 提供本地WebUI服务"""

import os
import sys
import socket
import base64
import webbrowser
from typing import Optional, Tuple
from flask import Flask, request, jsonify, send_from_directory

from ..core import QFNUAuth, CalendarGenerator, Config
from .. import __version__


class WebServer:
    """Web服务器类"""

    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()
        self.app = Flask(__name__, static_folder="static")
        self.auth = QFNUAuth(self.config)
        self.calendar_gen = CalendarGenerator(self.config)

        # 存储当前会话状态
        self._current_session = None
        self._current_cookies = None

        self._setup_routes()

    def _setup_routes(self):
        """设置路由"""

        @self.app.route("/")
        def index():
            """返回主页"""
            return send_from_directory(self.app.static_folder, "index.html")

        @self.app.route("/api/captcha")
        def get_captcha():
            """获取验证码图片"""
            try:
                # 初始化会话
                self._current_session, self._current_cookies, _ = self.auth.get_initial_session()
                # 获取验证码图片
                captcha_bytes = self.auth.get_captcha_bytes()
                return captcha_bytes, 200, {"Content-Type": "image/jpeg"}
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        @self.app.route("/api/login", methods=["POST"])
        def login():
            """登录并获取考试安排"""
            data = request.json
            if not data:
                return jsonify({"error": "请求数据为空"}), 400

            user_account = data.get("userAccount")
            user_password = data.get("userPassword")
            captcha_code = data.get("captchaCode")

            if not all([user_account, user_password, captcha_code]):
                return jsonify({"error": "请填写完整信息"}), 400

            try:
                # 执行登录
                response = self.auth.login(user_account, user_password, captcha_code)

                if response.status_code != 200:
                    return jsonify({"error": "登录失败"}), 400

                login_text = response.text

                if "验证码错误" in login_text:
                    return jsonify({"error": "验证码错误，请重新输入"}), 400

                if "密码错误" in login_text or "账号或密码错误" in login_text:
                    return jsonify({"error": "用户名或密码错误"}), 400

                if "系统繁忙" in login_text:
                    return jsonify({"error": "教务系统繁忙，请稍后再试"}), 400

                # 二次验证：通过访问用户信息页确认登录成功
                if not self.auth.verify_login(user_account):
                    return jsonify({"error": "登录验证失败，请重试"}), 400

                # 获取考试页面
                exam_response = self.auth.get_exam_page()

                # 解析考试数据
                exams = self.calendar_gen.parse_exam_page(exam_response.text)

                if not exams:
                    return jsonify({
                        "exams": [],
                        "icsBase64": None,
                        "message": "暂无考试安排"
                    })

                # 生成日历
                calendar = self.calendar_gen.create_calendar(exams)
                ics_content = calendar.serialize()

                # 保存文件
                filename = f"exam_schedule_{user_account}.ics"
                self.calendar_gen.save_calendar(calendar, filename)

                # 返回数据
                return jsonify({
                    "exams": exams,
                    "icsBase64": base64.b64encode(ics_content.encode("utf-8")).decode("utf-8"),
                    "message": "获取成功"
                })

            except Exception as e:
                error_message = str(e) if str(e) else "未知错误，请稍后重试"
                return jsonify({"error": error_message}), 400

        @self.app.route("/api/version")
        def version():
            """获取版本信息"""
            return jsonify({"version": __version__})

        @self.app.route("/api/shutdown", methods=["POST"])
        def shutdown():
            """关闭服务器"""
            def shutdown_server():
                os._exit(0)

            import threading
            threading.Timer(0.5, shutdown_server).start()
            return jsonify({"message": "服务器正在关闭..."})

    def find_available_port(self, start_port: int) -> int:
        """
        查找可用端口

        参数:
            start_port: 起始端口号

        返回: 可用的端口号
        """
        port = start_port
        max_attempts = self.config.max_port_attempts

        for _ in range(max_attempts):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.bind((self.config.host, port))
                    return port
            except OSError:
                port += 1

        raise RuntimeError(f"无法在 {start_port} - {start_port + max_attempts} 范围内找到可用端口")

    def run(self, open_browser: bool = True):
        """
        启动服务器

        参数:
            open_browser: 是否自动打开浏览器
        """
        # 查找可用端口
        port = self.find_available_port(self.config.port)

        url = f"http://{self.config.host}:{port}"

        print(f"\n{'=' * 50}")
        print(f"  曲阜师范大学考试安排导出工具 v{__version__}")
        print(f"{'=' * 50}")
        print(f"\n  服务已启动: {url}")
        print(f"\n  请在浏览器中打开上述地址使用")
        print(f"\n  按 Ctrl+C 停止服务")
        print(f"\n{'=' * 50}\n")

        # 自动打开浏览器
        if open_browser:
            webbrowser.open(url)

        # 启动服务器
        self.app.run(host=self.config.host, port=port, debug=False, threaded=True)


def create_app(config: Optional[Config] = None) -> Flask:
    """创建Flask应用实例"""
    server = WebServer(config)
    return server.app
