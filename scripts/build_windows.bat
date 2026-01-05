@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo ============================================
echo   QFNU Exam Export Tool - Nuitka Build
echo ============================================
echo.

:: 切换到项目根目录
cd /d "%~dp0.."
echo [INFO] Working directory: %cd%

:: 检查uv是否安装
where uv >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] uv not found, please install uv first
    echo Install command: pip install uv
    pause
    exit /b 1
)

:: 创建虚拟环境（如果不存在）
if not exist ".venv" (
    echo [INFO] Creating virtual environment...
    uv venv
)

:: 激活虚拟环境
echo [INFO] Activating virtual environment...
call .venv\Scripts\activate.bat

:: 安装依赖
echo [INFO] Installing project dependencies...
uv pip install -e .

echo [INFO] Installing build dependencies...
uv pip install nuitka ordered-set zstandard

:: 创建输出目录
if not exist "dist" mkdir dist

echo.
echo [INFO] Starting Nuitka compilation...
echo.

python -m nuitka ^
    --standalone ^
    --onefile ^
    --windows-console-mode=attach ^
    --enable-plugin=anti-bloat ^
    --include-data-dir=src/qfnu_exam/web/static=qfnu_exam/web/static ^
    --output-dir=dist ^
    --output-filename=qfnu-exam-2-ics.exe ^
    --company-name="W1ndys" ^
    --product-name="QFNU Exam Export Tool" ^
    --file-version=3.0.0 ^
    --product-version=3.0.0 ^
    --file-description="QFNU Exam Schedule to ICS Calendar" ^
    --copyright="Copyright (c) 2024 W1ndys" ^
    src/qfnu_exam/main.py

if %errorlevel% equ 0 (
    echo.
    echo ============================================
    echo   Build successful!
    echo   Output: dist\qfnu-exam-2-ics.exe
    echo ============================================
) else (
    echo.
    echo [ERROR] Build failed, please check the error message
)

pause
