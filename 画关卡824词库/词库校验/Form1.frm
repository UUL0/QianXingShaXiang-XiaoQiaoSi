VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "a=x=b相同数据提取分组"
   ClientHeight    =   10065
   ClientLeft      =   60
   ClientTop       =   405
   ClientWidth     =   12105
   LinkTopic       =   "Form1"
   ScaleHeight     =   10065
   ScaleWidth      =   12105
   StartUpPosition =   3  '窗口缺省
   Begin VB.TextBox Text4 
      Height          =   4995
      Left            =   420
      MultiLine       =   -1  'True
      ScrollBars      =   3  'Both
      TabIndex        =   6
      Text            =   "Form1.frx":0000
      Top             =   4980
      Width           =   6615
   End
   Begin VB.TextBox Text3 
      Height          =   4635
      Left            =   7500
      MultiLine       =   -1  'True
      ScrollBars      =   3  'Both
      TabIndex        =   5
      Text            =   "Form1.frx":0008
      Top             =   240
      Width           =   4395
   End
   Begin VB.CommandButton Command1 
      Caption         =   "解析"
      Height          =   675
      Left            =   7260
      TabIndex        =   4
      Top             =   5820
      Width           =   1035
   End
   Begin VB.TextBox Text1 
      Height          =   4635
      Left            =   420
      MultiLine       =   -1  'True
      ScrollBars      =   3  'Both
      TabIndex        =   3
      Text            =   "Form1.frx":0010
      Top             =   240
      Width           =   3075
   End
   Begin VB.TextBox Text2 
      Height          =   4635
      Left            =   3840
      MultiLine       =   -1  'True
      ScrollBars      =   3  'Both
      TabIndex        =   0
      Text            =   "Form1.frx":0016
      Top             =   240
      Width           =   3195
   End
   Begin VB.Label Label2 
      Caption         =   "输出"
      Height          =   615
      Left            =   180
      TabIndex        =   8
      Top             =   5040
      Width           =   315
   End
   Begin VB.Label Label1 
      Caption         =   "字典"
      Height          =   615
      Left            =   7200
      TabIndex        =   7
      Top             =   360
      Width           =   315
   End
   Begin VB.Label Label8 
      Caption         =   "提示"
      Height          =   615
      Left            =   3600
      TabIndex        =   2
      Top             =   360
      Width           =   315
   End
   Begin VB.Label Label7 
      Caption         =   "属性"
      Height          =   495
      Left            =   180
      TabIndex        =   1
      Top             =   420
      Width           =   315
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
Dim 字母ASC转数字(128) As String

Private Sub Command1_Click()
On Error Resume Next
    Dim 缓属性() As String
    Dim 缓提示() As String
    Dim 缓字典() As String
    
    Dim 属性() As String
    Dim 提示() As String
    Dim 字典() As String

    缓属性 = Split(Text1.Text, vbCrLf)
    缓提示 = Split(Text2.Text, vbCrLf)
    缓字典 = Split(Text3.Text, vbCrLf)
    
    ReDim 属性(UBound(缓属性)) As String
    ReDim 提示(UBound(缓提示)) As String
    ReDim 字典(UBound(缓字典)) As String
    
    Dim i As Long
    Dim 值1 As Long, 参1 As String
    
    For i = 0 To UBound(缓属性)
        '属性
        '0=风
         值1 = Val(Split(缓属性(i), "=")(0))
         参1 = Split(缓属性(i), "=")(1)
         属性(值1) = 参1
    Next
    For i = 0 To UBound(缓提示)
        '提示
        '1=未知
         值1 = Val(Split(缓提示(i), "=")(0))
         参1 = Split(缓提示(i), "=")(1)
         提示(值1) = 参1
    Next
    
    Dim 参2() As String
    For i = 0 To UBound(缓字典)
        '字典
        '1=荧=9=9=0
        参2 = Split(缓字典(i), "=")
        字典(i) = 参2(0) & "=" & 参2(1) & "=" & 参2(2) & "=" & 属性(Val(参2(3))) & "=" & 提示(Val(参2(4)))
    Next
    Text4.Text = Join(字典, vbCrLf)
End Sub


'UCase 转大写，LCase 转小写
'2 abc
'3 def
'4 ghi
'5 jkl
'6 mno
'7 pqrs
'8 tuv
'9 wxyz
Public Function 字母转T9数字(ByVal abc As String) As String
On Error Resume Next
    '输出列表 = 字母列表 '这里可用redim，但为了验证某行是否完成，直接对原列表修改
    Dim 行字符数 As Long, 行时钟 As Long, 行缓存 As String, 行拼接 As String
    Dim 判断空 As String

    行缓存 = UCase(abc)
    行字符数 = Len(行缓存)
    行拼接 = ""
    判断空 = ""
    For 行时钟 = 1 To 行字符数
        判断空 = 字母ASC转数字(Asc(Mid(行缓存, 行时钟, 1)))
        If 判断空 <> "" Then
            行拼接 = 行拼接 & 判断空
        End If
    Next

    字母转T9数字 = 行拼接
End Function

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





