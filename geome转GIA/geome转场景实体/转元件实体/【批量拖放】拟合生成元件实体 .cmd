@echo off
REM setlocal enabledelayedexpansion

REM mkdir "批量转换元件实体" 2>nul

REM for %%f in (%*) do (
REM     set "input=%%~f"
REM     set "output=批量转换元件实体\%%~nf_拟合元件实体.proto"
REM     echo 正在封装：%1
REM     py 图元拟合元件实体.py "!input!" "!output!" || echo 处理失败: "!input!"
REM )

REM pause

@echo off
setlocal enabledelayedexpansion

REM ==========================================
REM 1. 初始化与检查
REM ==========================================
if "%~1"=="" (
    echo 请将【文件夹】或【文件】拖放到本脚本图标上！
    pause
    exit /b
)

REM 创建输出目录
mkdir "批量转换元件实体" 2>nul

REM ==========================================
REM 2. 主循环：处理所有拖入的参数 (%*)
REM ==========================================
:process_loop
if "%~1"=="" goto end_process

REM 获取当前参数的完整绝对路径
set "current_path=%~f1"


REM 【关键判断】区分文件与文件夹
REM 方法：尝试访问 "路径\"。如果成功，则是文件夹；否则是文件。
REM 注意：必须使用 %~f1 获取标准化路径，避免相对路径问题

REM dir/ad "%current_path%" >nul 2>nul && echo 是文件夹 || echo 是文件

REM 使用 for 循环获取属性
for %%I in ("%current_path%") do (
    set "attr=%%~aI"
)

REM 截取属性的第一个字符
set "first_char=%attr:~0,1%"

if "%first_char%"=="d" (
    echo [检测到文件夹] 正在遍历: %current_path%
    call :process_folder "%current_path%"
) else (
    REM 如果不是文件夹，检查它是否是一个存在的文件
    if exist "%current_path%" (
        echo [检测到文件] 正在处理: %~nx1
        call :process_single_file "%current_path%"
    ) else (
        echo [警告] 路径无效或不存在: %~1
    )
)


REM 移除已处理的第一个参数，继续处理下一个
shift
goto process_loop

:end_process
echo.
echo ========================================
echo 所有任务处理完成！
pause
exit /b

REM ==========================================
REM 子程序：处理文件夹内的所有文件
REM ==========================================
:process_folder
set "target_dir=%~1"

REM 使用 dir /b /a-d 只列出文件，排除子文件夹
REM 2^>nul 隐藏错误信息（如空文件夹）
for /f "delims=" %%f in ('dir "%target_dir%\*" /b /a-d 2^>nul') do (
    set "full_path=%target_dir%\%%f"
    
    REM 再次确认文件存在
    if exist "!full_path!" (
        call :process_single_file "!full_path!"
    )
)
goto :eof

REM ==========================================
REM 子程序：处理单个文件的核心逻辑
REM ==========================================
:process_single_file
set "input=%~1"
set "filename_no_ext=%~n1"
set "output=批量转换元件实体\%filename_no_ext%_拟合元件实体.proto"

REM 执行 Python 脚本
REM 确保 python 脚本路径正确，如果不在同一目录，请修改下方路径
py "图元拟合元件实体.py" "!input!" "!output!"

if errorlevel 1 (
    echo   [失败] %~nx1
) else (
    echo   [成功] %~nx1
)
goto :eof
