# QFNU考试安排导出工具

曲阜师范大学教务系统考试安排导出工具 - 将考试安排导出为ICS日历文件，便于导入手机/电脑日历

![image](assets/image.png)

## 功能特点

- 一键导出考试安排为ICS日历文件
- 移动端友好的WebUI界面
- 支持手动输入验证码
- 端口自动检测，避免冲突
- 支持Nuitka编译为独立可执行文件

## 快速开始

### 方式一：使用uv（推荐）

1. **安装uv**

   ```bash
   pip install uv
   ```

2. **克隆项目**

   ```bash
   git clone https://github.com/W1ndys/qfnu-exam-2-ics.git
   cd qfnu-exam-2-ics
   ```

3. **创建虚拟环境并安装依赖**

   ```bash
   uv venv
   # Windows
   .venv\Scripts\activate
   # Linux/macOS
   source .venv/bin/activate

   uv pip install -e .
   ```

4. **运行程序**

   ```bash
   python -m qfnu_exam.main
   ```

   程序会自动打开浏览器，访问本地WebUI界面。

### 方式二：使用pip

1. **克隆项目**

   ```bash
   git clone https://github.com/W1ndys/qfnu-exam-2-ics.git
   cd qfnu-exam-2-ics
   ```

2. **安装依赖**

   ```bash
   pip install -e .
   ```

3. **运行程序**

   ```bash
   python -m qfnu_exam.main
   ```

## 编译为可执行文件

项目支持使用Nuitka编译为独立的可执行文件，无需Python环境即可运行。

### Windows

```bash
scripts\build_windows.bat
```

### Linux

```bash
chmod +x scripts/build_linux.sh
./scripts/build_linux.sh
```

### macOS

```bash
chmod +x scripts/build_macos.sh
./scripts/build_macos.sh
```

编译完成后，可执行文件位于 `dist` 目录。

## 项目结构

```
qfnu-exam-2-ics/
├── src/
│   └── qfnu_exam/
│       ├── __init__.py          # 包初始化
│       ├── main.py              # 主入口
│       ├── core/                # 核心模块
│       │   ├── __init__.py
│       │   ├── auth.py          # 认证模块
│       │   ├── calendar.py      # 日历生成模块
│       │   └── config.py        # 配置模块
│       └── web/                 # Web模块
│           ├── __init__.py
│           ├── server.py        # Web服务器
│           └── static/          # 静态资源
│               └── index.html   # 前端页面
├── scripts/                     # 编译脚本
│   ├── build_windows.bat
│   ├── build_linux.sh
│   └── build_macos.sh
├── pyproject.toml               # 项目配置
└── README.md
```

## 使用说明

1. 运行程序后，浏览器会自动打开WebUI界面
2. 输入教务系统账号和密码
3. 点击验证码图片获取验证码，手动输入
4. 点击"获取考试安排"按钮
5. 获取成功后可以：
   - 下载ICS日历文件，导入到手机/电脑日历
   - 复制考试信息文本

## 技术栈

- **后端**: Python + Flask
- **前端**: HTML + CSS + Vant组件库风格
- **日历**: ics库
- **编译**: Nuitka
- **包管理**: uv

## 开发

```bash
# 安装开发依赖
uv pip install -e ".[dev]"

# 运行测试
pytest

# 代码格式化
black src/
isort src/
```

## 许可证

MIT License

## 联系方式

- 作者: [W1ndys](https://www.w1ndys.top)
- GitHub: [W1ndys/qfnu-exam-2-ics](https://github.com/W1ndys/qfnu-exam-2-ics)
- QQ群: [曲师大选课指北群](https://qm.qq.com/q/7RsPEDwlrO)
