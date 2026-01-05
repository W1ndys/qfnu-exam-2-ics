#!/bin/bash

echo "============================================"
echo "  曲阜师范大学考试安排导出工具 - macOS编译"
echo "============================================"
echo

# 切换到项目根目录
cd "$(dirname "$0")/.."
echo "[信息] 工作目录: $(pwd)"

# 检查uv是否安装
if ! command -v uv &> /dev/null; then
    echo "[错误] 未找到uv，请先安装uv"
    echo "安装命令: pip install uv"
    exit 1
fi

# 创建虚拟环境（如果不存在）
if [ ! -d ".venv" ]; then
    echo "[信息] 正在创建虚拟环境..."
    uv venv
fi

# 激活虚拟环境
echo "[信息] 正在激活虚拟环境..."
source .venv/bin/activate

# 安装依赖
echo "[信息] 正在安装项目依赖..."
uv pip install -e .

echo "[信息] 正在安装编译依赖..."
uv pip install nuitka ordered-set zstandard

# 创建输出目录
mkdir -p dist

# 编译
echo
echo "[信息] 开始Nuitka编译..."
echo

python -m nuitka \
    --standalone \
    --onefile \
    --macos-create-app-bundle \
    --enable-plugin=anti-bloat \
    --output-dir=dist \
    --output-filename=qfnu-exam-2-ics \
    --macos-app-name="QFNU考试导出" \
    src/qfnu_exam/main.py

if [ $? -eq 0 ]; then
    echo
    echo "============================================"
    echo "  编译成功！"
    echo "  输出文件: dist/qfnu-exam-2-ics.app"
    echo "============================================"
else
    echo
    echo "[错误] 编译失败，请检查错误信息"
fi
