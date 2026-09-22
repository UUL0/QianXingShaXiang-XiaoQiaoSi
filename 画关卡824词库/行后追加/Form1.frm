VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "列表拼合"
   ClientHeight    =   8865
   ClientLeft      =   60
   ClientTop       =   405
   ClientWidth     =   13725
   LinkTopic       =   "Form1"
   ScaleHeight     =   8865
   ScaleWidth      =   13725
   StartUpPosition =   3  '窗口缺省
   Begin VB.TextBox Text6 
      Height          =   390
      Left            =   12600
      TabIndex        =   11
      Text            =   "8"
      Top             =   3300
      Width           =   855
   End
   Begin VB.CommandButton Command4 
      Caption         =   "不足N补字符数"
      Height          =   555
      Left            =   12600
      TabIndex        =   10
      Top             =   2700
      Width           =   915
   End
   Begin VB.TextBox Text5 
      Height          =   435
      Left            =   12720
      TabIndex        =   8
      Text            =   "0"
      Top             =   7380
      Width           =   675
   End
   Begin VB.CommandButton Command3 
      Caption         =   "前加数字"
      Height          =   555
      Left            =   12720
      TabIndex        =   7
      Top             =   6480
      Width           =   675
   End
   Begin VB.CommandButton Command2 
      Caption         =   "追加字符"
      Height          =   675
      Left            =   12660
      TabIndex        =   6
      Top             =   4680
      Width           =   795
   End
   Begin VB.TextBox Text4 
      Height          =   315
      Left            =   12660
      TabIndex        =   5
      Text            =   "="
      Top             =   5400
      Width           =   675
   End
   Begin VB.TextBox Text3 
      Height          =   8235
      Left            =   8400
      MultiLine       =   -1  'True
      ScrollBars      =   3  'Both
      TabIndex        =   3
      Text            =   "Form1.frx":0000
      Top             =   240
      Width           =   3975
   End
   Begin VB.TextBox Text2 
      Height          =   8235
      Left            =   4200
      MultiLine       =   -1  'True
      ScrollBars      =   3  'Both
      TabIndex        =   2
      Text            =   "Form1.frx":0008
      Top             =   240
      Width           =   3975
   End
   Begin VB.CommandButton Command1 
      Caption         =   "拼合"
      Height          =   615
      Left            =   12480
      TabIndex        =   1
      Top             =   900
      Width           =   855
   End
   Begin VB.TextBox Text1 
      Height          =   8175
      Left            =   420
      MultiLine       =   -1  'True
      ScrollBars      =   3  'Both
      TabIndex        =   0
      Text            =   "Form1.frx":000E
      Top             =   240
      Width           =   3615
   End
   Begin VB.Label Label2 
      AutoSize        =   -1  'True
      Caption         =   "起始值"
      Height          =   180
      Left            =   12720
      TabIndex        =   9
      Top             =   7080
      Width           =   540
   End
   Begin VB.Label Label1 
      AutoSize        =   -1  'True
      Caption         =   "1+2=3"
      Height          =   180
      Left            =   540
      TabIndex        =   4
      Top             =   8580
      Width           =   450
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
Dim 字母文本1 As String
Dim 字母文本2 As String

Dim 输出文本 As String

Dim 字母列表1() As String
Dim 字母列表2() As String

Dim 输出列表() As String


Private Sub Command1_Click()
On Error Resume Next
    Dim 列表上限 As Long
    Dim 时钟 As Long
    
    字母文本1 = Text1.Text
    字母文本2 = Text2.Text
    
    字母列表1 = Split(字母文本1, vbCrLf)
    字母列表2 = Split(字母文本2, vbCrLf)
    输出列表 = 字母列表1
    
    列表上限 = UBound(字母列表1)
    
    For 时钟 = 0 To 列表上限
        输出列表(时钟) = 字母列表1(时钟) & 字母列表2(时钟)
    Next

    Text3.Text = Join(输出列表, vbCrLf)


End Sub

Private Sub Command2_Click()
    On Error Resume Next
    Dim 列表上限 As Long
    Dim 时钟 As Long
    
    字母文本1 = Text1.Text
    字母文本2 = Text2.Text
    
    字母列表1 = Split(字母文本1, vbCrLf)
    字母列表2 = Split(字母文本2, vbCrLf)
    输出列表 = 字母列表1
    
    列表上限 = UBound(字母列表1)
    
    For 时钟 = 0 To 列表上限
        输出列表(时钟) = 字母列表1(时钟) & Text4.Text
    Next

    Text3.Text = Join(输出列表, vbCrLf)
End Sub

Private Sub Command3_Click()
    On Error Resume Next
    Dim 列表上限 As Long
    Dim 时钟 As Long
    Dim 起始值 As Long
    
    字母文本1 = Text1.Text
    字母文本2 = Text2.Text
    
    字母列表1 = Split(字母文本1, vbCrLf)
    字母列表2 = Split(字母文本2, vbCrLf)
    输出列表 = 字母列表1
    
    列表上限 = UBound(字母列表1)
    起始值 = Text5.Text
    For 时钟 = 0 To 列表上限
        输出列表(时钟) = 起始值 + 时钟 & Text4.Text & 字母列表1(时钟)
    Next

    Text3.Text = Join(输出列表, vbCrLf)
End Sub

Private Sub Command4_Click()
    On Error Resume Next
    Dim 列表上限 As Long
    Dim 时钟 As Long
    Dim 目标字符数 As Long
    
    字母文本1 = Text1.Text
    字母文本2 = Text2.Text
    
    字母列表1 = Split(字母文本1, vbCrLf)
    字母列表2 = Split(字母文本2, vbCrLf)
    输出列表 = 字母列表1
    
    列表上限 = UBound(字母列表1)
    Dim 需要的空格数 As Long
    Dim 缓存字符数 As Long
    
    目标字符数 = Val(Text6.Text)
    
    For 时钟 = 0 To 列表上限
            缓存字符数 = Len(字母列表1(时钟))
            If 缓存字符数 < 目标字符数 Then
                需要的空格数 = 目标字符数 - 缓存字符数
                输出列表(时钟) = 字母列表1(时钟) & Space(需要的空格数 * 2)
            End If
    Next

    Text3.Text = Join(输出列表, vbCrLf)
End Sub
