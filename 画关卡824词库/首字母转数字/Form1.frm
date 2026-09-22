VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "字母转九宫数字"
   ClientHeight    =   8865
   ClientLeft      =   60
   ClientTop       =   405
   ClientWidth     =   10275
   LinkTopic       =   "Form1"
   ScaleHeight     =   8865
   ScaleWidth      =   10275
   StartUpPosition =   3  '窗口缺省
   Begin VB.TextBox Text2 
      Height          =   8235
      Left            =   5640
      MultiLine       =   -1  'True
      ScrollBars      =   3  'Both
      TabIndex        =   2
      Text            =   "Form1.frx":0000
      Top             =   180
      Width           =   3975
   End
   Begin VB.CommandButton Command1 
      Caption         =   "转数字"
      Height          =   615
      Left            =   4620
      TabIndex        =   1
      Top             =   480
      Width           =   855
   End
   Begin VB.TextBox Text1 
      Height          =   8175
      Left            =   780
      MultiLine       =   -1  'True
      ScrollBars      =   3  'Both
      TabIndex        =   0
      Text            =   "Form1.frx":0006
      Top             =   240
      Width           =   3615
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
Dim 字母文本 As String
Dim 输出文本 As String

Dim 字母列表() As String
Dim 输出列表() As String

Dim 字母ASC转数字(128) As String
'UCase 转大写，LCase 转小写
'2 abc
'3 def
'4 ghi
'5 jkl
'6 mno
'7 pqrs
'8 tuv
'9 wxyz
Private Sub Command1_Click()
On Error Resume Next
    Dim 列表上限 As Long
    Dim 时钟 As Long
    
    字母文本 = Text1.Text
    字母列表 = Split(字母文本, vbCrLf)
    
    列表上限 = UBound(字母列表)
    '输出列表 = 字母列表 '这里可用redim，但为了验证某行是否完成，直接对原列表修改
    
    Dim 行字符数 As Long, 行时钟 As Long, 行缓存 As String, 行拼接 As String
    Dim 判断空 As String
    
    For 时钟 = 0 To 列表上限
        行缓存 = UCase(字母列表(时钟))
        行字符数 = Len(行缓存)
        行拼接 = ""
        判断空 = ""
        For 行时钟 = 1 To 行字符数
            判断空 = 字母ASC转数字(Asc(Mid(行缓存, 行时钟, 1)))
            If 判断空 <> "" Then
                行拼接 = 行拼接 & 判断空
            End If
        Next
        字母列表(时钟) = 行拼接
    Next

    Text2.Text = Join(字母列表, vbCrLf)


End Sub

Private Sub Form_Load()
    Dim 时钟 As Long
    Const 映射字符 As String = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Const 映射数字 As String = "22233344455566677778889999"
    Dim 转asc As Long
    
    For 时钟 = 1 To 26
        转asc = Asc(Mid(映射字符, 时钟, 1))
        字母ASC转数字(转asc) = Mid(映射数字, 时钟, 1)
    Next
End Sub
