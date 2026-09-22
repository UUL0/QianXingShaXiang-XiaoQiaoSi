VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "音符列表时间放大,格式：时间秒 音符"
   ClientHeight    =   8670
   ClientLeft      =   60
   ClientTop       =   405
   ClientWidth     =   6975
   LinkTopic       =   "Form1"
   ScaleHeight     =   8670
   ScaleWidth      =   6975
   StartUpPosition =   3  '窗口缺省
   Begin VB.TextBox Text8 
      Height          =   270
      Left            =   6480
      TabIndex        =   16
      Text            =   "1"
      Top             =   7620
      Width           =   435
   End
   Begin VB.CommandButton Command3 
      Caption         =   "P序列用"
      Height          =   555
      Left            =   5880
      TabIndex        =   14
      Top             =   3300
      Width           =   915
   End
   Begin VB.TextBox Text7 
      Height          =   270
      Left            =   5940
      TabIndex        =   13
      Text            =   "0"
      Top             =   7620
      Width           =   435
   End
   Begin VB.TextBox Text6 
      Height          =   315
      Left            =   5940
      TabIndex        =   11
      Text            =   "1"
      Top             =   5040
      Width           =   855
   End
   Begin VB.CommandButton Command2 
      Caption         =   "计算"
      Height          =   375
      Left            =   5940
      TabIndex        =   10
      Top             =   5400
      Width           =   915
   End
   Begin VB.TextBox Text5 
      Height          =   375
      Left            =   5940
      TabIndex        =   8
      Text            =   "0.5"
      Top             =   4320
      Width           =   795
   End
   Begin VB.TextBox Text4 
      Height          =   270
      Left            =   6120
      TabIndex        =   6
      Text            =   " "
      Top             =   6120
      Width           =   555
   End
   Begin VB.TextBox Text3 
      Height          =   435
      Left            =   6120
      TabIndex        =   4
      Text            =   "1"
      Top             =   6780
      Width           =   675
   End
   Begin VB.CommandButton Command1 
      Caption         =   "乘"
      Height          =   615
      Left            =   6120
      TabIndex        =   3
      Top             =   7980
      Width           =   735
   End
   Begin VB.TextBox Text2 
      Height          =   8235
      Left            =   3000
      MultiLine       =   -1  'True
      ScrollBars      =   3  'Both
      TabIndex        =   1
      Text            =   "Form1.frx":0000
      Top             =   240
      Width           =   2775
   End
   Begin VB.TextBox Text1 
      Height          =   8175
      Left            =   420
      MultiLine       =   -1  'True
      ScrollBars      =   3  'Both
      TabIndex        =   0
      Text            =   "Form1.frx":0006
      Top             =   240
      Width           =   2475
   End
   Begin VB.Label Label6 
      AutoSize        =   -1  'True
      Caption         =   "时间  音符 列"
      Height          =   180
      Left            =   5940
      TabIndex        =   15
      Top             =   7320
      Width           =   1170
   End
   Begin VB.Label Label5 
      Caption         =   "目标倍数"
      Height          =   255
      Left            =   5940
      TabIndex        =   12
      Top             =   4740
      Width           =   855
   End
   Begin VB.Label Label4 
      Caption         =   "原倍数"
      Height          =   315
      Left            =   5940
      TabIndex        =   9
      Top             =   4020
      Width           =   795
   End
   Begin VB.Label Label3 
      Caption         =   "分割符"
      Height          =   255
      Left            =   6120
      TabIndex        =   7
      Top             =   5880
      Width           =   555
   End
   Begin VB.Label Label2 
      Caption         =   "乘倍数"
      Height          =   255
      Left            =   6120
      TabIndex        =   5
      Top             =   6480
      Width           =   555
   End
   Begin VB.Label Label1 
      AutoSize        =   -1  'True
      Caption         =   "1=>2"
      Height          =   180
      Left            =   480
      TabIndex        =   2
      Top             =   8520
      Width           =   360
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

Dim 分隔符 As String

Dim 时间倍速 As Double

Dim 时间列 As Long, 音符列 As Long


Private Sub Command1_Click()
    On Error Resume Next
    Dim 列表上限 As Long
    Dim 时钟 As Long
    时间列 = Val(Text7.Text)
    音符列 = Val(Text8.Text)
    
    字母文本1 = Text1.Text

    字母列表1 = Split(字母文本1, vbCrLf)

    输出列表 = 字母列表1
    
    列表上限 = UBound(字母列表1)
    Dim 时间 As Double
    Dim 音符 As Long
    
    For 时钟 = 0 To 列表上限
        时间 = Val(Split(字母列表1(时钟), 分隔符)(时间列))
        输出列表(时钟) = Fix((时间 * 时间倍速) * 10000) / 10000 & 分隔符 & Split(字母列表1(时钟), 分隔符)(音符列)
    Next

    Text2.Text = Join(输出列表, vbCrLf)
End Sub

Private Sub Command2_Click()
    '还原结果=目标倍数/原倍数
    '但结果是倍数需要转换
    Text3.Text = Fix((Val(Text5.Text) / Val(Text6.Text)) * 10000) / 10000
End Sub

Private Sub Command3_Click()
    On Error Resume Next
    Dim 列表上限 As Long
    Dim 时钟 As Long
    时间列 = Val(Text7.Text)
    音符列 = Val(Text8.Text)
    
    字母文本1 = Text1.Text

    字母列表1 = Split(字母文本1, vbCrLf)

    输出列表 = 字母列表1
    
    列表上限 = UBound(字母列表1)
    Dim 时间 As Long
    Dim 音符 As Long
    
    For 时钟 = 0 To 列表上限
        时间 = Val(Split(字母列表1(时钟), 分隔符)(2))
        输出列表(时钟) = Split(字母列表1(时钟), 分隔符)(0) & 分隔符 & Split(字母列表1(时钟), 分隔符)(1) & 分隔符 & Int(时间 * 时间倍速)
    Next

    Text2.Text = Join(输出列表, vbCrLf)
End Sub

Private Sub Form_Load()
    分隔符 = Text4.Text
    时间倍速 = Text3.Text
End Sub

Private Sub Text3_Change()
    时间倍速 = Text3.Text
End Sub

Private Sub Text4_Change()
    分隔符 = Text4.Text
End Sub

