"""主入口模块"""

import sys
import os

# 确保可以找到模块
if getattr(sys, 'frozen', False):
    # 如果是打包后的可执行文件
    application_path = os.path.dirname(sys.executable)
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

# 添加到路径
sys.path.insert(0, os.path.dirname(application_path))

from qfnu_exam import __version__
from qfnu_exam.core import Config
from qfnu_exam.web import WebServer


def main():
    """主函数"""
    print(f"\n曲阜师范大学考试安排导出工具 v{__version__}")
    print("=" * 50)

    # 创建配置
    config = Config()

    # 创建并启动服务器
    server = WebServer(config)
    server.run(open_browser=True)


if __name__ == "__main__":
    main()
