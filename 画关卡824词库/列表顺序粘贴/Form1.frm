VERSION 5.00
Begin VB.Form Form1 
   AutoRedraw      =   -1  'True
   Caption         =   "处理列表粘贴"
   ClientHeight    =   7680
   ClientLeft      =   60
   ClientTop       =   405
   ClientWidth     =   5625
   KeyPreview      =   -1  'True
   LinkTopic       =   "Form1"
   ScaleHeight     =   7680
   ScaleWidth      =   5625
   StartUpPosition =   3  '窗口缺省
   Begin VB.CheckBox Check2 
      Caption         =   "UP时"
      Height          =   255
      Left            =   4500
      TabIndex        =   18
      Top             =   7320
      Width           =   915
   End
   Begin VB.TextBox Text8 
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   10.5
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1875
      Left            =   4440
      MultiLine       =   -1  'True
      ScrollBars      =   2  'Vertical
      TabIndex        =   16
      Text            =   "Form1.frx":0000
      Top             =   5400
      Width           =   1095
   End
   Begin VB.TextBox Text7 
      Height          =   315
      Left            =   4500
      TabIndex        =   13
      Text            =   "Text7"
      Top             =   2400
      Width           =   855
   End
   Begin VB.TextBox Text6 
      Height          =   330
      Left            =   2940
      TabIndex        =   12
      Text            =   "Text6"
      Top             =   7860
      Width           =   435
   End
   Begin VB.TextBox Text5 
      Height          =   315
      Left            =   4500
      TabIndex        =   10
      Text            =   "0"
      Top             =   4020
      Width           =   855
   End
   Begin VB.TextBox Text4 
      Height          =   315
      Left            =   4500
      TabIndex        =   8
      Text            =   " "
      Top             =   3360
      Width           =   855
   End
   Begin VB.CommandButton Command1 
      Caption         =   "分割列表"
      Height          =   495
      Left            =   4500
      TabIndex        =   7
      Top             =   4440
      Width           =   855
   End
   Begin VB.Timer Timer1 
      Enabled         =   0   'False
      Interval        =   1
      Left            =   5040
      Top             =   2580
   End
   Begin VB.CheckBox Check1 
      Caption         =   "开始"
      Height          =   315
      Left            =   4500
      TabIndex        =   4
      Top             =   1740
      Width           =   1035
   End
   Begin VB.TextBox Text3 
      Height          =   375
      Left            =   4440
      TabIndex        =   2
      Text            =   "Text3"
      Top             =   1020
      Width           =   1155
   End
   Begin VB.TextBox Text2 
      Height          =   375
      Left            =   4440
      Locked          =   -1  'True
      TabIndex        =   1
      Top             =   300
      Width           =   1155
   End
   Begin VB.TextBox Text1 
      Height          =   7275
      Left            =   780
      MultiLine       =   -1  'True
      ScrollBars      =   3  'Both
      TabIndex        =   0
      Text            =   "Form1.frx":0006
      Top             =   60
      Width           =   3615
   End
   Begin VB.Label Label8 
      Alignment       =   2  'Center
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "历史预览："
      Height          =   180
      Left            =   4470
      TabIndex        =   17
      Top             =   5100
      Width           =   900
   End
   Begin VB.Label Label7 
      Alignment       =   2  'Center
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "(0~N)"
      Height          =   180
      Left            =   4500
      TabIndex        =   15
      Top             =   1440
      Width           =   450
   End
   Begin VB.Label Label6 
      Alignment       =   2  'Center
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "当前号："
      Height          =   180
      Left            =   4500
      TabIndex        =   14
      Top             =   2160
      Width           =   720
   End
   Begin VB.Label Label5 
      Alignment       =   2  'Center
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "列号(0~N)："
      Height          =   180
      Left            =   4500
      TabIndex        =   11
      Top             =   3780
      Width           =   990
   End
   Begin VB.Label Label4 
      Alignment       =   2  'Center
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "分割符："
      Height          =   180
      Left            =   4470
      TabIndex        =   9
      Top             =   3060
      Width           =   720
   End
   Begin VB.Label Label3 
      Alignment       =   2  'Center
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "开始序号："
      Height          =   180
      Left            =   4470
      TabIndex        =   6
      Top             =   780
      Width           =   900
   End
   Begin VB.Label Label2 
      Alignment       =   2  'Center
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "粘贴键："
      Height          =   180
      Left            =   4500
      TabIndex        =   5
      Top             =   60
      Width           =   720
   End
   Begin VB.Label Label1 
      Alignment       =   2  'Center
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "列表："
      Height          =   240
      Left            =   240
      TabIndex        =   3
      Top             =   60
      Width           =   720
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
Dim UP时复制 As Boolean


Private Sub Check1_Click()
    If Check1.Value = 1 Then
            是否开始 = True
            列表() = Split(Text1.Text, vbCrLf)
            最大号 = UBound(列表)
            历史计数 = 0
            历史字符 = ""
            
            当前序号 = 开始序号
            Text7.Text = 当前序号
        Else
            是否开始 = False
    End If
    Timer1.Enabled = 是否开始
End Sub

Private Sub Check2_Click()
    If Check2.Value = 1 Then
                UP时复制 = True
            Else
                UP时复制 = False
    End If
End Sub

Private Sub Command1_Click() '列表分割，按照每行：0 1 2 3 4类似的列表分割
    Dim 列表2() As String, 上限 As Long, i As Long
    缓冲 = Text1.Text
    分割符号 = Text4.Text
    列号 = Val(Text5.Text)
    列表2 = Split(缓冲, vbCrLf)
    上限 = UBound(列表2)
    
    ReDim 列表3(上限) As String
    
    For i = 0 To 上限
        列表3(i) = Split(列表2(i), 分割符号, -1, vbBinaryCompare)(列号)
    Next
    
    Text1.Text = Join(列表3, vbCrLf)
End Sub

Private Sub Form_Load()
    If IsUserAnAdmin = 0 Then
            Me.Caption = Me.Caption & "::非管理员"
            If MsgBox("是否以管理员运行？", 4096 Or vbYesNo, "程序未获得权限") = vbYes Then ShellExecute 0, "runas", App.Path & "\" & App.EXEName & ".exe", "", "", 1: End  'SW_SHOWNORMAL
        Else
            Me.Caption = Me.Caption & "::管理员"
    End If
    开始序号 = 0
    是否开始 = False
    粘贴键 = 0
    Text2.Text = 粘贴键
    Text3.Text = 开始序号
    
End Sub

Private Sub Form_Unload(Cancel As Integer)
    End
End Sub

Private Sub Text2_KeyDown(KeyCode As Integer, Shift As Integer)
    Timer1.Enabled = False
        Text2.Text = KeyCode
        粘贴键 = KeyCode
        Text6.SetFocus
End Sub

Private Sub Text3_Change()
开始序号 = Val(Text3.Text)
End Sub

Private Sub Timer1_Timer()
    On Error Resume Next
    If ((GetAsyncKeyState(粘贴键) And &H8000) = &H8000) And 检测粘贴键 = 0 Then
        检测粘贴键 = 1
         '按下时触发
            If Not UP时复制 Then
                    If 当前序号 <= 最大号 Then
                           缓冲 = 列表(当前序号)
                           Clipboard.Clear '用前必须清一下
                           Clipboard.SetText 缓冲
                           历史字符 = 历史字符 & 缓冲 & vbCrLf
                           Text8.Text = 历史字符
                           历史计数 = 历史计数 + 1
                           If 历史计数 > 6 Then
                               历史计数 = 0
                               历史字符 = ""
                           End If
                          当前序号 = 当前序号 + 1
                          Text7.Text = 当前序号
                    End If
            End If
         ElseIf GetAsyncKeyState(粘贴键) = 0 And 检测粘贴键 = 1 Then
                检测粘贴键 = 0
                If UP时复制 Then
                            If 当前序号 <= 最大号 Then
                           缓冲 = 列表(当前序号)
                           Clipboard.Clear '用前必须清一下
                           Clipboard.SetText 缓冲
                           历史字符 = 历史字符 & 缓冲 & vbCrLf
                           Text8.Text = 历史字符
                           历史计数 = 历史计数 + 1
                           If 历史计数 > 6 Then
                               历史计数 = 0
                               历史字符 = ""
                           End If
                          当前序号 = 当前序号 + 1
                          Text7.Text = 当前序号
                    End If

                End If
    End If

End Sub
