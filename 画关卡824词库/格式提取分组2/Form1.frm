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
   Begin VB.CommandButton Command5 
      Caption         =   "2-8for1~7"
      Height          =   375
      Left            =   10860
      TabIndex        =   24
      Top             =   5280
      Width           =   975
   End
   Begin VB.TextBox Text8 
      Height          =   375
      Left            =   10740
      TabIndex        =   22
      Text            =   "0"
      ToolTipText     =   "新格式元素位(词行ID)"
      Top             =   780
      Width           =   855
   End
   Begin VB.CheckBox Check3 
      Caption         =   "新格式"
      Height          =   255
      Left            =   10680
      TabIndex        =   21
      ToolTipText     =   "在前面添加原数据所在行号，1开始"
      Top             =   420
      Width           =   1035
   End
   Begin VB.CheckBox Check2 
      Caption         =   "从中排除"
      Height          =   255
      Left            =   10800
      TabIndex        =   18
      ToolTipText     =   "勾选后排除模式，否则筛选模式"
      Top             =   9360
      Width           =   1095
   End
   Begin VB.TextBox Text7 
      Height          =   375
      Left            =   10800
      TabIndex        =   16
      Text            =   "中间相等"
      Top             =   8940
      Width           =   1095
   End
   Begin VB.CommandButton Command4 
      Caption         =   "筛选行"
      Height          =   375
      Left            =   10800
      TabIndex        =   15
      Top             =   8280
      Width           =   975
   End
   Begin VB.TextBox Text6 
      Height          =   330
      Left            =   10860
      TabIndex        =   12
      Text            =   "="
      Top             =   6120
      Width           =   915
   End
   Begin VB.TextBox Text5 
      Height          =   375
      Left            =   10860
      TabIndex        =   9
      Text            =   "2"
      ToolTipText     =   "满足条件时要保留的位数，左边起"
      Top             =   4860
      Width           =   975
   End
   Begin VB.TextBox Text4 
      Height          =   375
      Left            =   10860
      TabIndex        =   8
      Text            =   "3"
      ToolTipText     =   "指定列满足多少位数时执行保留位"
      Top             =   4200
      Width           =   975
   End
   Begin VB.CommandButton Command3 
      Caption         =   "筛选指定列位数"
      Height          =   555
      Left            =   10800
      TabIndex        =   7
      Top             =   3240
      Width           =   1035
   End
   Begin VB.CheckBox Check1 
      Caption         =   "追加原行号"
      Height          =   375
      Left            =   10800
      TabIndex        =   6
      ToolTipText     =   "在前面添加原数据所在行号，1开始"
      Top             =   2640
      Width           =   1335
   End
   Begin VB.TextBox Text3 
      Height          =   375
      Left            =   10800
      TabIndex        =   4
      Text            =   "2"
      ToolTipText     =   "选择要筛选排序哪一列"
      Top             =   1860
      Width           =   555
   End
   Begin VB.CommandButton Command2 
      Caption         =   "指定列分组"
      Height          =   555
      Left            =   10800
      TabIndex        =   3
      ToolTipText     =   "以某一列相同数字排列分组排序"
      Top             =   1260
      Width           =   915
   End
   Begin VB.TextBox Text2 
      Height          =   4695
      Left            =   720
      MultiLine       =   -1  'True
      ScrollBars      =   3  'Both
      TabIndex        =   2
      Text            =   "Form1.frx":0000
      Top             =   5040
      Width           =   9675
   End
   Begin VB.CommandButton Command1 
      Caption         =   "分组排序"
      Enabled         =   0   'False
      Height          =   615
      Left            =   11700
      TabIndex        =   1
      Top             =   60
      Width           =   855
   End
   Begin VB.TextBox Text1 
      Height          =   4635
      Left            =   780
      MultiLine       =   -1  'True
      ScrollBars      =   3  'Both
      TabIndex        =   0
      Text            =   "Form1.frx":0006
      Top             =   240
      Width           =   9675
   End
   Begin VB.Label Label11 
      AutoSize        =   -1  'True
      Caption         =   "第"
      Height          =   180
      Left            =   10620
      TabIndex        =   26
      Top             =   1920
      Width           =   180
   End
   Begin VB.Label Label10 
      AutoSize        =   -1  'True
      Caption         =   "列"
      Height          =   180
      Left            =   11400
      TabIndex        =   25
      Top             =   1920
      Width           =   180
   End
   Begin VB.Label Label9 
      AutoSize        =   -1  'True
      Caption         =   "位"
      Height          =   180
      Left            =   11640
      TabIndex        =   23
      Top             =   900
      Width           =   180
   End
   Begin VB.Label Label8 
      Caption         =   "输出"
      Height          =   615
      Left            =   360
      TabIndex        =   20
      Top             =   5280
      Width           =   315
   End
   Begin VB.Label Label7 
      Caption         =   "输入"
      Height          =   495
      Left            =   360
      TabIndex        =   19
      Top             =   420
      Width           =   315
   End
   Begin VB.Label Label6 
      Caption         =   "关键字"
      Height          =   195
      Left            =   10800
      TabIndex        =   17
      Top             =   8700
      Width           =   735
   End
   Begin VB.Label Label5 
      Caption         =   "一般， 简拼位数3时，筛选前2位， 4位时前3位， 5位时前3、4位， 6位时前4，5位"
      Height          =   1575
      Left            =   10860
      TabIndex        =   14
      Top             =   6600
      Width           =   1035
   End
   Begin VB.Label Label4 
      Caption         =   "列分隔符"
      Height          =   315
      Left            =   10860
      TabIndex        =   13
      Top             =   5820
      Width           =   975
   End
   Begin VB.Label Label3 
      Caption         =   "保留位数(<N)"
      Height          =   255
      Left            =   10860
      TabIndex        =   11
      Top             =   4620
      Width           =   1155
   End
   Begin VB.Label Label2 
      Caption         =   "条件:=N位"
      Height          =   195
      Left            =   10860
      TabIndex        =   10
      Top             =   3960
      Width           =   855
   End
   Begin VB.Label Label1 
      Caption         =   "0~N"
      Height          =   225
      Left            =   10860
      TabIndex        =   5
      Top             =   2340
      Width           =   450
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
Dim 列分割符 As String

'现有需提取中间数字相同分组，并加入原先所在的行号，再从大到小排序
'羊 = 9 = 0
'马 = 6 = 0
'大象 = 39 = 0
'狮子 = 79 = 0
'虎 = 4 = 0
'兔 = 8 = 0
'猴子 = 4 = 0
'熊猫 = 96 = 0

'循环，从第一条取数据，逐步向后判断，如果相同则提取数据并标记所在行，
Private Sub Command1_Click()
    Dim 源数据 As String
    源数据 = Text1.Text
    Dim 列表分行() As String
    Dim 总行数 As Long
    列表分行 = Split(源数据, vbCrLf)
    总行数 = UBound(列表分行)
    Dim 缓存比对 As String
    ReDim 计算结果(总行数 * 2) As String
    
    Dim 时钟X As Long, 时钟Y As Long
    Dim 时钟Z As Long
    时钟Z = 0

    For 时钟X = 0 To 总行数
            If 列表分行(时钟X) <> "" Then
                    缓存比对 = Split(列表分行(时钟X), 列分割符, -1, vbTextCompare)(1)
                    计算结果(时钟Z) = "中间相等" & 缓存比对 & "<<"
                    时钟Z = 时钟Z + 1
                    
                            For 时钟Y = 时钟X To 总行数 '从当前行后比对，不包含自身行
                                        If 列表分行(时钟Y) <> "" Then
                                                If 缓存比对 = Split(列表分行(时钟Y), 列分割符, -1, vbBinaryCompare)(1) Then '相同则取这行数据到容器内
                                                         计算结果(时钟Z) = 时钟Y + 1 & 列分割符 & 列表分行(时钟Y)
                                                         列表分行(时钟Y) = "" '清空当前值，因为没有移除列表值，只能用空字符代替
                                                         时钟Z = 时钟Z + 1
                                                End If
                                        End If
                            Next
            End If
    Next
    ReDim Preserve 计算结果(时钟Z) As String
    
    'Text2.Text = Join(计算结果, vbCrLf)
    
    'Exit Sub
    
    列表分行 = Split(Join(计算结果, vbCrLf), "中间相等") '排序
    总行数 = UBound(列表分行)
    ReDim 计算结果(总行数) As String
    时钟Z = 0
    
    Dim 大小比对 As Long, 最小值索引 As Long, 判定 As Boolean
  
    For 时钟X = 0 To 总行数 '取最小值放到容器底，原内容交换
                    判定 = False
                    If 列表分行(时钟X) <> "" Then
                            大小比对 = Val(Split(列表分行(时钟X), "<<")(0))
                            
                                    For 时钟Y = 时钟X To 总行数
                                        If 列表分行(时钟Y) <> "" Then
                                                If Val(Split(列表分行(时钟Y), "<<")(0)) < 大小比对 Then
                                                        大小比对 = Val(Split(列表分行(时钟Y), "<<")(0))
                                                        最小值索引 = 时钟Y '记录最小值
                                                        判定 = True
                                                End If
                                        End If
                                    Next
                            If 判定 Then
                                    计算结果(时钟Z) = "中间相等：" & 列表分行(最小值索引)
                                    列表分行(最小值索引) = 列表分行(时钟X) '与最小值交换
                                Else
                                    计算结果(时钟Z) = "中间相等：" & 列表分行(时钟X) '否则当前是最  小的值
                                    '列表分行(时钟X) = "" '清空，排除
                            End If
                            时钟Z = 时钟Z + 1
                    End If
    Next
    Text2.Text = Join(计算结果, vbCrLf)
    
    
End Sub


Private Sub Command2_Click() '指定列
    Dim 格式类型 As Boolean
    Dim 格式2位 As Long
    格式类型 = False
    If Check3.Value = 1 Then 格式类型 = True
    格式2位 = Val(Text8.Text) '新格式的列分割取元素N
    
    Dim 指定列 As Long
    指定列 = Val(Text3.Text)
    
     Dim 源数据 As String
    源数据 = Text1.Text
    Dim 列表分行() As String
    Dim 总行数 As Long
    列表分行 = Split(源数据, vbCrLf)
    总行数 = UBound(列表分行)
    Dim 缓存比对 As String
    'ReDim 计算结果(总行数 * 2) As String
    ReDim 计算结果(总行数 + 2) As String
    
    Dim 时钟X As Long, 时钟Y As Long
    Dim 时钟Z As Long
    时钟Z = 0
    Dim 元素计数 As Long '简拼号内的数量
    Dim 简拼计数 As Long '有多少简拼号
    
    Dim 缓存值去重 As String
    
    For 时钟X = 0 To 总行数
            If 列表分行(时钟X) <> "" Then
                    缓存比对 = Split(列表分行(时钟X), 列分割符, -1, vbTextCompare)(指定列)
                    '计算结果(时钟Z) = "中间相等" & 缓存比对 & "<<" & vbCrLf
                    元素计数 = 0
                    '时钟Z = 时钟Z + 1'因为可以直接拼接字符串
                    
                            For 时钟Y = 时钟X To 总行数 '从当前行后比对，不包含自身行
                                        If 列表分行(时钟Y) <> "" Then
                                                If 缓存比对 = Split(列表分行(时钟Y), 列分割符, -1, vbBinaryCompare)(指定列) Then '相同则取这行数据到容器内
                                                        元素计数 = 元素计数 + 1
                                                        If 格式类型 Then
                                                            If Check1.Value = 1 Then '追加行号
                                                                '计算结果(时钟Z) = 计算结果(时钟Z) & 时钟Y + 1 & 列分割符 & 列表分行(时钟Y) & vbCrLf
                                                             Else
                                                                If 元素计数 <= 1 Then
                                                                    计算结果(时钟Z) = 计算结果(时钟Z) & "[去除]" & Split(列表分行(时钟Y), 列分割符, -1, vbTextCompare)(格式2位) & "[去除]"
                                                                Else
                                                                    缓存值去重 = Split(列表分行(时钟Y), 列分割符, -1, vbTextCompare)(格式2位)
                                                                    
                                                                    If InStr(1, 计算结果(时钟Z), "[去除]" & 缓存值去重 & "[去除]", vbBinaryCompare) > 0 Then   '如果已经存在值则不加入
                                                                        'Debug.Print 计算结果(时钟Z) & "  重复：" & 缓存值去重
                                                                    Else
                                                                        计算结果(时钟Z) = 计算结果(时钟Z) & ", " & "[去除]" & 缓存值去重 & "[去除]"
                                                                    End If
                                                                End If
                                                             End If
                                                        Else
                                                            If Check1.Value = 1 Then '追加行号
                                                                计算结果(时钟Z) = 计算结果(时钟Z) & 时钟Y + 1 & 列分割符 & 列表分行(时钟Y) & vbCrLf
                                                             Else
                                                                计算结果(时钟Z) = 计算结果(时钟Z) & 列表分行(时钟Y) & vbCrLf
                                                             End If
                                                        End If
                                                         列表分行(时钟Y) = "" '清空当前值，因为没有移除列表值，只能用空字符代替
'                                                        If Check1.Value = 1 Then '追加行号
'                                                            计算结果(时钟Z) = 时钟Y + 1 & 列分割符 & 列表分行(时钟Y)
'                                                         Else
'                                                            计算结果(时钟Z) = 列表分行(时钟Y)
'                                                         End If
'                                                         列表分行(时钟Y) = "" '清空当前值，因为没有移除列表值，只能用空字符代替
'                                                         时钟Z = 时钟Z + 1
                                                End If
                                        End If
                            Next
                            
                            If 格式类型 Then
                                计算结果(时钟Z) = Replace(计算结果(时钟Z), "[去除]", "", 1, -1, vbBinaryCompare)
                                计算结果(时钟Z) = "中间相等" & 缓存比对 & "<<[" & 计算结果(时钟Z) & "]" & vbCrLf
                            Else
                                计算结果(时钟Z) = "中间相等" & 缓存比对 & "<<，元素数>>" & 元素计数 & "" & vbCrLf & 计算结果(时钟Z)
                            End If
                             时钟Z = 时钟Z + 1
            End If
    Next
    计算结果(0) = "简拼号数目>>" & 时钟Z & vbCrLf & 计算结果(0)
    ReDim Preserve 计算结果(时钟Z) As String
    
'    Text2.Text = Join(计算结果, vbCrLf)
'
'    Exit Sub
    
    列表分行 = Split(Join(计算结果, ""), "中间相等") '排序
    
    总行数 = UBound(列表分行)
    ReDim 计算结果(总行数) As String
    时钟Z = 0
    
    Dim 大小比对 As Long, 最小值索引 As Long, 判定 As Boolean
  
    For 时钟X = 0 To 总行数 '取最小值放到容器底，原内容交换
                    判定 = False
                    If 列表分行(时钟X) <> "" Then
                            大小比对 = Val(Split(列表分行(时钟X), "<<")(0))
                                    For 时钟Y = 时钟X To 总行数
                                        If 列表分行(时钟Y) <> "" Then
                                                If Val(Split(列表分行(时钟Y), "<<")(0)) < 大小比对 Then
                                                        大小比对 = Val(Split(列表分行(时钟Y), "<<")(0))
                                                        最小值索引 = 时钟Y '记录最小值
                                                        判定 = True
                                                End If
                                        End If
                                    Next
                            If 格式类型 Then
                                If 判定 Then
                                        计算结果(时钟Z) = Replace(列表分行(最小值索引), "<<", "：", 1, -1, vbBinaryCompare) 'Split(列表分行(最小值索引), "<<", -1, vbBinaryCompare)(1)
                                        列表分行(最小值索引) = 列表分行(时钟X) '与最小值交换
                                    Else
                                        计算结果(时钟Z) = Replace(列表分行(时钟X), "<<", "：", 1, -1, vbBinaryCompare)   'Split(列表分行(时钟X), "<<", -1, vbBinaryCompare)(1)  '否则当前是最  小的值
                                        '列表分行(时钟X) = "" '清空，排除
                                End If
                            Else
                                If 判定 Then
                                        计算结果(时钟Z) = "中间相等：" & 列表分行(最小值索引)
                                        列表分行(最小值索引) = 列表分行(时钟X) '与最小值交换
                                    Else
                                        计算结果(时钟Z) = "中间相等：" & 列表分行(时钟X) '否则当前是最  小的值
                                        '列表分行(时钟X) = "" '清空，排除
                                End If
                            End If
                            时钟Z = 时钟Z + 1
                    End If
    Next
    'Text2.Text = Join(计算结果, vbcrlf)
    Text2.Text = Join(计算结果, "")
End Sub

Private Sub Command3_Click()
    On Error Resume Next
    Dim 目标列 As Long
    Dim 条件位数 As Long
    Dim 保留位数 As Long
    Dim 文本列表1() As String
    文本列表1 = Split(Text1.Text, vbCrLf)
    Dim 列表上限 As Long
    列表上限 = UBound(文本列表1)
    Dim 时钟 As Long
    Dim 缓存目标() As String
    
    目标列 = Val(Text3.Text)
    条件位数 = Val(Text4.Text)
    保留位数 = Val(Text5.Text)
    
    ReDim 输出列表(列表上限) As String
    Dim 筛选条目 As Long
    
    筛选条目 = 0
    For 时钟 = 0 To 列表上限
            缓存目标 = Split(文本列表1(时钟), 列分割符) '当前行分列
            If Len(缓存目标(目标列)) = 条件位数 Then '目标列的位数满足
                缓存目标(目标列) = Left(缓存目标(目标列), 保留位数) '取位
                输出列表(筛选条目) = Join(缓存目标, 列分割符) '修改
                筛选条目 = 筛选条目 + 1
            End If
    Next
    ReDim Preserve 输出列表(筛选条目 - 1) As String
    Text2.Text = Join(输出列表, vbCrLf)
End Sub

Private Sub Command4_Click()
    On Error Resume Next
    Dim 文本列表1() As String
    文本列表1 = Split(Text1.Text, vbCrLf)
    Dim 列表上限  As Long
    Dim 时钟 As Long
    Dim 关键词 As String
    关键词 = Text7.Text
    列表上限 = UBound(文本列表1)
    
    ReDim 输出列表(列表上限) As String
    Dim 筛选计数 As Long
    筛选计数 = 0
    
    If Check2.Value = 1 Then '排除模式
            For 时钟 = 0 To 列表上限
                If InStr(1, 文本列表1(时钟), 关键词, vbBinaryCompare) = 0 Then '没有则存
                    输出列表(筛选计数) = 文本列表1(时钟)
                    筛选计数 = 筛选计数 + 1
                End If
            Next
        Else '筛选模式，仅保留找到的行
            For 时钟 = 0 To 列表上限
                If InStr(1, 文本列表1(时钟), 关键词, vbBinaryCompare) > 0 Then '找到则存
                    输出列表(筛选计数) = 文本列表1(时钟)
                    筛选计数 = 筛选计数 + 1
                End If
            Next
    End If
    
    ReDim Preserve 输出列表(筛选计数) As String
    Text2.Text = Join(输出列表, vbCrLf)
End Sub

Public Function 指定位等于保留(ByRef 文本表() As String, ByVal 指定列 As Long, ByVal 等于位 As Long, ByVal 保留位 As Long) As String
    On Error Resume Next
    Dim 列表上限 As Long
    列表上限 = UBound(文本表)
    
    Dim 时钟 As Long
    Dim 缓存目标() As String
    
    ReDim 输出列表(列表上限) As String
    Dim 筛选条目 As Long
    
    筛选条目 = 0
    For 时钟 = 0 To 列表上限
            缓存目标 = Split(文本表(时钟), 列分割符) '当前行分列
            If Len(缓存目标(指定列)) = 等于位 Then '目标列的位数满足
                缓存目标(指定列) = Left(缓存目标(指定列), 保留位) '取位
                输出列表(筛选条目) = Join(缓存目标, 列分割符) '修改
                筛选条目 = 筛选条目 + 1
            End If
    Next
    ReDim Preserve 输出列表(筛选条目 - 1) As String
    If (输出列表(UBound(输出列表)) = vbCrLf) Or (输出列表(UBound(输出列表)) = "") Then
        ReDim Preserve 输出列表(UBound(输出列表) - 1) As String
    End If
    指定位等于保留 = Join(输出列表, vbCrLf)
End Function

Private Sub Command5_Click() '等于N位=>>保留指定位
    Dim 保留位 As Long
    Dim 等于位 As Long
    
    Dim 文本列表1() As String
    文本列表1 = Split(Text1.Text, vbCrLf)
    
    Dim 目标列 As Long
    目标列 = Val(Text3.Text)
    
    ReDim 输出(7 * 7) As String
    Dim i As Long
    '1位和8位本就在原始字典简拼结构中
    i = 0
    For 保留位 = 1 To 7 '保留1~7位
            For 等于位 = (保留位 + 1) To 8 '等于多少位时保留
                输出(i) = 指定位等于保留(文本列表1, 目标列, 等于位, 保留位)
                If Not ((输出(i) = vbCrLf) Or (输出(i) = "")) Then i = i + 1
            Next
    Next
    ReDim Preserve 输出(i) As String
    Text2.Text = Join(输出, vbCrLf)
End Sub

Private Sub Form_Load()
    列分割符 = Text6.Text
End Sub

Private Sub Text6_Change()
    列分割符 = Text6.Text
End Sub
