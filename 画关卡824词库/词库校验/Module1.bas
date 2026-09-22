Attribute VB_Name = "Module1"
Option Explicit


Type GroupData
    midNum As Integer
    lines() As String
End Type
  
Public Sub ProcessData(ByVal str As String)
    Dim inputData As String
    inputData = GetInputData() ' 实际应从文本框获取
      
    Dim lines() As String
    lines = Split(inputData, vbCrLf)
      
    Dim validLines As New Collection
    Dim i As Long
    For i = LBound(lines) To UBound(lines)
        Dim trimmedLine As String
        trimmedLine = Trim(lines(i))
        If trimmedLine <> "" And Left(trimmedLine, 11) <> "-----------" Then
            validLines.Add trimmedLine
        End If
    Next i
      
    Dim groups As New Collection
    Dim lineNum As Long
    lineNum = 1
      
    For i = 1 To validLines.Count
        Dim parts() As String
        parts = Split(validLines(i), "=")
        If UBound(parts) >= 1 Then
            Dim midNum As Long
            midNum = Val(parts(1))
              
            Dim groupExists As Boolean
            groupExists = False
            Dim j As Long
              
            ' 检查分组是否存在
            For j = 1 To groups.Count
                If groups(j).midNum = midNum Then
                    groupExists = True
                    Exit For
                End If
            Next j
              
            ' 创建或更新分组
            If Not groupExists Then
                Dim newGroup As GroupData
                newGroup.midNum = midNum
                ReDim newGroup.lines(1 To 1)
                newGroup.lines(1) = Format(lineNum, "0") & ": " & validLines(i)
                groups.Add newGroup
            Else
                Dim existingGroup As GroupData
                Set existingGroup = groups(j) ' 获取现有分组对象
                  
                ' 扩展分组行数组
                Dim lineCount As Long
                lineCount = UBound(existingGroup.lines)
                ReDim Preserve existingGroup.lines(1 To lineCount + 1)
                existingGroup.lines(lineCount + 1) = Format(lineNum, "0") & ": " & validLines(i)
                  
                ' 更新集合中的分组对象
                groups.Remove j ' 先移除旧对象
                groups.Add existingGroup, , j ' 在原位置添加新对象
            End If
              
            lineNum = lineNum + 1
        End If
    Next i
      
    ' 生成输出结果
    Dim output As String
    output = ""
    For i = 1 To groups.Count
        output = output & "中间数字=" & groups(i).midNum & vbCrLf
        For j = 1 To UBound(groups(i).lines)
            output = output & groups(i).lines(j) & vbCrLf
        Next j
        output = output & "-----------" & vbCrLf
    Next i
      
    ' 显示结果（实际应输出到显示控件）
    Debug.Print output
End Sub
  
Function GetInputData() As String
    ' 示例数据，实际应从文本框获取
    GetInputData = "猫=6=0" & vbCrLf & _
                   "狗=4=0" & vbCrLf & _
                   "猪=9=0" & vbCrLf & _
                   "-----------" & vbCrLf & _
                   "牛=6=0" & vbCrLf & _
                   "羊=9=0" & vbCrLf & _
                   "马=6=0"
End Function

