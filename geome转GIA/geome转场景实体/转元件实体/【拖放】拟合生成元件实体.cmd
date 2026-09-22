@echo off
setlocal enabledelayedexpansion


echo 正在处理：%1

py 图元拟合元件实体.py %1 %~n1_拟合元件实体.proto

pause