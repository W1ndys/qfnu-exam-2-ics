"""配置管理模块"""

from dataclasses import dataclass, field


@dataclass
class Config:
    """应用配置"""

    # 教务系统URL配置
    base_url: str = "http://zhjw.qfnu.edu.cn"
    login_url: str = field(default="")
    captcha_url: str = field(default="")
    user_info_url: str = field(default="")
    exam_query_url: str = field(default="")  # 考试安排查询页（获取默认学期）
    exam_list_url: str = field(default="")   # 考试安排列表页（获取考试数据）

    # Web服务器配置
    host: str = "127.0.0.1"
    port: int = 5000
    max_port_attempts: int = 100

    # 输出配置
    output_dir: str = "output"

    def __post_init__(self):
        """初始化URL"""
        if not self.login_url:
            self.login_url = f"{self.base_url}/jsxsd/xk/LoginToXkLdap"
        if not self.captcha_url:
            self.captcha_url = f"{self.base_url}/jsxsd/verifycode.servlet"
        if not self.user_info_url:
            self.user_info_url = f"{self.base_url}/jsxsd/framework/xsMain_new.jsp?t1=1"
        if not self.exam_query_url:
            self.exam_query_url = f"{self.base_url}/jsxsd/xsks/xsksap_query"
        if not self.exam_list_url:
            self.exam_list_url = f"{self.base_url}/jsxsd/xsks/xsksap_list"
