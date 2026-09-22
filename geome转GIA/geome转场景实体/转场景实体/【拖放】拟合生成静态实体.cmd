@echo off
setlocal enabledelayedexpansion


echo 正在处理：%1

py 图元拟合场景实体.py %1 %~n1_拟合场景实体.proto

pause