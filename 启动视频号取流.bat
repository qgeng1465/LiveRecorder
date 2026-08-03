@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Starting WeChat Video Channel capture tool...
echo (first run installs dependencies, please wait)
echo.
python wechat_capture.py
echo.
pause
