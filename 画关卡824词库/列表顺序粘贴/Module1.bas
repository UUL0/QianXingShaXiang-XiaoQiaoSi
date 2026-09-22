Attribute VB_Name = "Module1"
Option Explicit

Public Declare Function IsUserAnAdmin Lib "shell32" () As Long '非0表示管理员权限
Public Declare Function ShellExecute Lib "shell32.dll" Alias "ShellExecuteA" (ByVal hwnd As Long, ByVal lpOperation As String, ByVal lpFile As String, ByVal lpParameters As String, ByVal lpDirectory As String, ByVal nShowCmd As Long) As Long
Public Declare Function GetAsyncKeyState Lib "user32" (ByVal VKey As Long) As Integer 'as Integer，该函数是侦测按键硬件中断，已按过0位设置1，按下则第15bit位设置1，否则0
'验证：如果按键上次按下到目前调用的线程没有切换过，则此次调用返回上一次的按键状态，也就是上一次是否按下过
'声明必须为Integer2字节，但是原函数是SHORT类型返回值，但是位与也可以用

Public 开始序号 As Long, 列表() As String, 是否开始 As Boolean, 当前序号 As Long, 最大号 As Long
Public 历史字符 As String, 历史计数 As Long

Public 缓冲  As String, 分割符号 As String, 列号 As Long

Public 粘贴键 As Long, 检测粘贴键 As Long
