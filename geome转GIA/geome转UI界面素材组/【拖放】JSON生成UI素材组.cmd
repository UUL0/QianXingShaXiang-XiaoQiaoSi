@echo off
setlocal enabledelayedexpansion

echo 正在处理：%1

py 生成拟合素材组.py %1 %~n1_拟合素材组.proto

pause