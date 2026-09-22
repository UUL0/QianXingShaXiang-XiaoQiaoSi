from io import StringIO
import os
import struct
import sys
import math
import json

# 
# 
全局偏移X=0.0
全局偏移Y=0.0
全局缩放W=0.01
全局缩放H=0.01

线宽=0.1 # line形状下的线宽

忽略透明度=1 # 1始终255，0引入data

# 纵轴浮动=0.00001
纵轴浮动=0.000001 # 没有办法进行混合（层级），一点一点往顶层移动

# 方体：10009001
# 空模型：10005018
# 三棱柱：10009004
# 圆柱：10009008

def 图元拟合静态实体(data_list,output_file):
    # 设定起始初始参数
    GUID起始值=1077943195

    起始坐标X=0.0
    起始坐标Y=0.0
    起始坐标Z=0.0

    实体旋转X=0.0
    实体旋转Y=0.0
    实体旋转Z=0.0

    实体缩放X=1.0
    实体缩放Y=0.2
    实体缩放Z=1.0

    图形ID=10009001

    静态 = 1
    碰撞=1
    攀爬=1
    可见=1
    覆盖装饰颜色=1

    实体名称= "图元拟" # os.path.basename(output_file) # "静态画像素实体"

    排序ID=0

    X间距=1.0
    Y间距=1.0
    Z间距=1.0

    引用参数1="{\n"

    参数 = [""] * 53 # 列表N个空项

    参数[0]=""
    参数[1]=""
    参数[2]="  '01:"
    参数[3]=f"{排序ID:02d}" # {排序ID:02d}
    参数[4]=":embedded message': \n    {\n      '01:00:embedded message': \n        {\n          '02:00:Varint': 1,\n          '03:01:Varint': 2,\n          '04:02:Varint': "
    参数[5]=f"{GUID起始值}" # GUID
    参数[6]="\n        },\n      '03:01:string': '"
    参数[7]=f"{实体名称}" # 名称
    参数[8]="',\n      '05:02:Varint': 3,\n      '12:03:embedded message': \n        {\n          '01:00:embedded message': \n            {\n              '01:00:Varint': "
    参数[9]=f"{GUID起始值}" # GUID

    参数[10]=",\n              '02:01:embedded message': \n                {\n                  '01:00:Varint': "
    参数[11]=f"{图形ID}" # 图形ID
    参数[12]=",\n                  '02:01:Varint': 1\n                },\n              '05:02:embedded message': \n                {\n                  '01:00:Varint': 1,\n                  '11:01:embedded message': \n                    {\n                      '01:00:string': '"
    参数[13]=f"{实体名称}" # 名称
    参数[14]="',\n                      '02:01:Varint': "
    参数[15]=f"{静态}" # 静态=1，动态=0
    参数[16]="\n                    }\n                },\n              '05:03:embedded message': \n                {\n                  '01:00:Varint': 13,\n                  '22:01:embedded message': \n                    {\n                      '04:00:Varint': 4294967295\n                    }\n                },\n              '05:04:embedded message': \n                {\n                  '01:00:Varint': 14,\n                  '23:01:embedded message': \n                    {\n                      '01:00:embedded message': \n                        {\n                          '03:00:string': 'MPActionGroup'\n                        }\n                    }\n                },\n              '05:05:embedded message': \n                {\n                  '01:00:Varint': 38,\n                  '48:01:embedded message': \n                    {\n                      '01:00:32-bit': 1.0\n                    }\n                },\n              '05:06:embedded message': \n                {\n                  '01:00:Varint': 40,\n                  '50:01:embedded message': \n                    {\n                    }\n                },\n              '05:07:embedded message': \n                {\n                  '01:00:Varint': 111,\n                  '93:01:embedded message': \n                    {\n                    }\n                },\n              '05:08:embedded message': \n                {\n                  '01:00:Varint': 61,\n                  '65:01:embedded message': \n                    {\n                    }\n                },\n              '05:09:embedded message': \n                {\n                  '01:00:Varint': 62,\n                  '66:01:embedded message': \n                    {\n                    }\n                },\n              '05:10:embedded message': \n                {\n                  '01:00:Varint': 19,\n                  '28:01:embedded message': \n                    {\n                    }\n                },\n              '05:11:embedded message': \n                {\n                  '01:00:Varint': 52,\n                  '62:01:embedded message': \n                    {\n                    }\n                },\n              '06:12:embedded message': \n                {\n                  '01:00:Varint': 1,\n                  '11:01:embedded message': \n                    {\n                      '01:00:embedded message': \n                        {\n                          '01:00:32-bit': "

    参数[17]=f"{起始坐标X}" # 起始坐标X
    参数[18]=",\n                          '02:01:32-bit': "
    参数[19]=f"{起始坐标Y}" # 起始坐标Y

    参数[20]=",\n                          '03:02:32-bit': "
    参数[21]=f"{起始坐标Z}" # 起始坐标Z
    参数[22]="\n                        },\n                      '02:01:embedded message': \n                        {\n                          '01:00:32-bit': "
    参数[23]=f"{实体旋转X}" # 实体旋转X
    参数[24]=",\n                          '02:01:32-bit': "
    参数[25]=f"{实体旋转Y}" # 实体旋转Y
    参数[26]=",\n                          '03:02:32-bit': "
    参数[27]=f"{实体旋转Z}" # 实体旋转Z
    参数[28]="\n                        },\n                      '03:02:embedded message': \n                        {\n                          '01:00:32-bit': "
    参数[29]=f"{实体缩放X}" # 实体缩放X
 
    参数[30]=",\n                          '02:01:32-bit': "
    参数[31]=f"{实体缩放Y}" # 实体缩放Y
    参数[32]=",\n                          '03:02:32-bit': "
    参数[33]=f"{实体缩放Z}" # 实体缩放Z

    参数[34]="\n                        },\n                      '501:03:Varint': 4294967295\n                    }\n                },\n              '06:13:embedded message': \n                {\n                  '01:00:Varint': 2,\n                  '12:01:embedded message': \n                    {\n                    }\n                },\n              '06:14:embedded message': \n                {\n                  '01:00:Varint': 3,\n                  '13:01:embedded message': \n                    {\n                    }\n                },\n              '06:15:embedded message': \n                {\n                  '01:00:Varint': 4,\n                  '14:01:embedded message': \n                    {\n                      '01:00:Varint': 1\n                    }\n                },\n              '06:16:embedded message': \n                {\n                  '01:00:Varint': 5,\n                  '15:01:embedded message': \n                    {\n                      '01:00:Varint': "
    参数[35]=f"{碰撞}" # 自身碰撞开=1，关=0
    参数[36]=",\n                      '02:01:Varint': "
    参数[37]=f"{攀爬}" # 可攀爬开=1，关=0
    参数[38]="\n                    }\n                },\n              '06:17:embedded message': \n                {\n                  '01:00:Varint': 6,\n                  '16:01:embedded message': \n                    {\n                    }\n                },\n              '06:18:embedded message': \n                {\n                  '01:00:Varint': 7,\n                  '17:01:embedded message': \n                    {\n                      '01:00:32-bit': 1000.0,\n                      '03:01:32-bit': 500.0,\n                      '04:02:Varint': 1,\n                      '05:03:Varint': 1,\n                      '06:04:embedded message': \n                        {\n                          '02:00:Varint': 10200002\n                        },\n                      '08:05:32-bit': 0.10000000149011612,\n                      '09:06:32-bit': 0.10000000149011612,\n                      '10:07:32-bit': 0.10000000149011612,\n                      '11:08:32-bit': 0.10000000149011612,\n                      '12:09:32-bit': 0.10000000149011612,\n                      '13:10:32-bit': 0.10000000149011612,\n                      '14:11:32-bit': 0.10000000149011612,\n                      '15:12:32-bit': 0.10000000149011612\n                    }\n                },\n              '06:19:embedded message': \n                {\n                  '01:00:Varint': 8,\n                  '18:01:embedded message': \n                    {\n                      '01:00:Varint': "
    参数[39]=f"{可见}" # 可见性开=1，关=0

    参数[40]=",\n                      '501:01:Varint': 1\n                    }\n                },\n              '06:20:embedded message': \n                {\n                  '01:00:Varint': 11,\n                  '21:01:embedded message': \n                    {\n                      '01:00:embedded message': \n                        {\n                          '01:00:string': 'GI_RootNode',\n                          '02:01:embedded message': \n                            {\n                            },\n                          '03:02:embedded message': \n                            {\n                            },\n                          '502:03:string': '中心原点',\n                          '504:04:Varint': 1,\n                          '505:05:string': 'RootNode'\n                        }\n                    }\n                },\n              '06:21:embedded message': \n                {\n                  '01:00:Varint': 12,\n                  '22:01:embedded message': \n                    {\n                      '01:00:Varint': 1\n                    }\n                },\n              '06:22:embedded message': \n                {\n                  '01:00:Varint': 16,\n                  '26:01:embedded message': \n                    {\n                    }\n                },\n              '06:23:embedded message': \n                {\n                  '01:00:Varint': 17,\n                  '27:01:embedded message': \n                    {\n                    }\n                },\n              '06:24:embedded message': \n                {\n                  '01:00:Varint': 19,\n                  '29:01:embedded message': \n                    {\n                      '01:00:Varint': 1\n                    }\n                },\n              '06:25:embedded message': \n                {\n                  '01:00:Varint': 20,\n                  '30:01:embedded message': \n                    {\n                      '02:00:Varint': 2\n                    }\n                },\n              '06:26:embedded message': \n                {\n                  '01:00:Varint': 22,\n                  '32:01:embedded message': \n                    {\n                      '01:00:Varint': 1,\n                      '02:01:Varint': "
    参数[41]=f"{覆盖装饰颜色}" # 覆盖装饰颜色开=1，关=0
    参数[42]=",\n                      '03:02:Varint': "
    参数[43]="" # 引用ARGB
    参数[44]=",\n                      '04:03:32-bit': "
    参数[45]="" # 透明度
    参数[46]=",\n                      '05:04:Varint': "
    参数[47]="" # 实体RGB
    参数[48]=",\n                      '06:05:Varint': 6700\n                    }\n                },\n              '08:27:Varint': "
    参数[49]=f"{图形ID}" # 图形ID
    参数[50]="\n            },\n          '02:01:Varint': 1402,\n          '04:02:Varint': "
    参数[51]=f"{图形ID}" # 图形ID
    参数[52]="\n        }\n    },\n"



    引用参数2="\n  '03:"
    # {排序ID:02d}
    引用参数3=":string': '111111111-1790057300-1073741800-\\静态实体模板.gia',\n  '05:"
    # {排序ID:02d}
    引用参数4=":string': '7.0.0'\n}"

    # 通过HEX编辑器或解封装gia，最后几行中查看
    # 你账号导出gia的最后参数字符串(例如：xxxxxxxxx-xxxxxxxxxx-xxxxxxxxxx，似乎是账号UID+"-"+ID1+"-"+ID2)

    # 写入文件流程：
    # 参数00
    # 实体循环：
    # 参数0+排序ID+参数1+实体GUID+参数2+实体名称+参数3+实体GUID+参数4+实体名称+参数5+实体位置X+参数6+实体位置Y+参数7+实体位置Z+参数8+实体缩放X+参数9+实体缩放Y+参数10+实体缩放Z+参数11+引用ARGB+参数11_ARGB+实体颜色透明度+参数12+实体颜色+参数13
    # 实体循环结束

    # 引用参数1+实体循环+引用参数2+{排序ID:02d}+引用参数3+{排序ID:02d}+引用参数4

    # 预拼接模板 + StringIO 批量写入
    # 缓冲区
    buffer = StringIO()

    # 开始循环

    实体数量=0

    # 以下是生成的计数用的

    实体GUID=0

    实体位置X=起始坐标X
    实体位置Y=起始坐标Y
    实体位置Z=起始坐标Z

    排序ID=0

    buffer.write(引用参数1)

    序号=0
    总元数量=len(data_list)

    for 序号 in range(总元数量):
        实体位置Y+=纵轴浮动

        # 获取一个元素
        元参=data_list[序号] 
        # 1. 获取 type
        item_type = 元参['type']
        # 2. 获取 data (列表)
        item_data = 元参['data']
        # 3. 获取 color (列表 [R, G, B, A])
        item_color_rgba = 元参['color']

        # 将 [R, G, B, A] 列表转换为 ARGB 格式的 32位整数
        Cr, Cg, Cb, Ca = item_color_rgba # 解包获取各通道值
        Cr, Cg, Cb, Ca = int(Cr), int(Cg), int(Cb), int(Ca) # 确保值在 0-255 范围内
        if 忽略透明度==1:
            Ca=255
        引用ARGB = (Ca << 24) | (Cr << 16) | (Cg << 8) | Cb

        实体颜色=引用ARGB & 0xFFFFFF # 十进制RGB值
        实体颜色透明度=float(round(Ca * (100 / 255))) # 映射到 0-100浮点数

        实体GUID=GUID起始值+实体数量
        实体数量+=1

        if item_type == 0: # 矩形
            图形ID = 10009001
            X1, Y1, X2, Y2 = item_data
            x=float((X1+X2)/2)
            y=float((Y1+Y2)/2)
            w=float(X2-X1)
            h=float(Y2-Y1)
            # 大小
            实体缩放X=w * 全局缩放W
            实体缩放Z=h * 全局缩放H
            # 位置（素材组位置信息，0.0,0.0为屏幕显示中心）
            实体位置X=(x * 全局缩放W) + 全局偏移X
            实体位置Z=(-y * 全局缩放H) + 全局偏移Y
            # 旋转
            实体旋转Y=float(0.0)
        elif item_type == 1: # 旋转矩形
            图形ID = 10009001
            X1, Y1, X2, Y2, Rto= item_data
            x=float((X1+X2)/2)
            y=float((Y1+Y2)/2)
            w=float(X2-X1)
            h=float(Y2-Y1)
            Rot=float(Rto) 
            # 大小
            实体缩放X=w * 全局缩放W
            实体缩放Z=h * 全局缩放H
            # 位置
            实体位置X=(x * 全局缩放W) + 全局偏移X
            实体位置Z=(-y * 全局缩放H) + 全局偏移Y
            # 旋转
            实体旋转Y=Rot
        elif item_type == 3: # 椭圆
            图形ID = 10009008
            X, Y, RX, RY= item_data
            x=float(X)
            y=float(Y)
            w=float(RX*2)
            h=float(RY*2)
            # 大小
            实体缩放X=w * 全局缩放W
            实体缩放Z=h * 全局缩放H
            # 位置
            实体位置X=(x * 全局缩放W) + 全局偏移X
            实体位置Z=(-y * 全局缩放H) + 全局偏移Y
            # 旋转
            实体旋转Y=float(0.0)
        elif item_type == 4: # 旋转椭圆
            图形ID = 10009008
            X, Y, RX, RY, Rto= item_data
            x=float(X)
            y=float(Y)
            w=float(RX*2)
            h=float(RY*2)
            Rot=float(Rto) 
            # 大小
            实体缩放X=w * 全局缩放W
            实体缩放Z=h * 全局缩放H
            # 位置
            实体位置X=(x * 全局缩放W) + 全局偏移X
            实体位置Z=(-y * 全局缩放H) + 全局偏移Y
            # 旋转
            实体旋转Y=Rot
        elif item_type == 5: # 圆
            图形ID = 10009008
            X, Y, R= item_data
            x=float(X)
            y=float(Y)
            w=float(R*2)
            h=float(R*2)
            # 大小
            实体缩放X=w * 全局缩放W
            实体缩放Z=h * 全局缩放H
            # 位置
            实体位置X=(x * 全局缩放W) + 全局偏移X
            实体位置Z=(-y * 全局缩放H) + 全局偏移Y
            # 旋转
            实体旋转Y=float(0.0)
        elif item_type == 6: # 线
            图形ID = 10009001
            X1, Y1, X2, Y2= item_data
            dx=float(X2-X1)
            dy=float(Y2-Y1)
            angle_rad = math.atan2(dx, dy)
            if angle_rad < 0:
                angle_rad += 2 * math.pi
            # 转换为角度制
            Rto = math.degrees(angle_rad)

            x=float((X1+X2)/2)
            y=float((Y1+Y2)/2)
            w=线宽
            h=math.sqrt((dx**2+dy**2))
            Rot=float(Rto)
            # 大小
            实体缩放X=w * 全局缩放W
            实体缩放Z=h * 全局缩放H
            # 位置
            实体位置X=(x * 全局缩放W) + 全局偏移X
            实体位置Z=(-y * 全局缩放H) + 全局偏移Y
            # 旋转
            实体旋转Y=Rot
        elif item_type == 8: # 等腰三角
            图形ID = 10009004
            item_params = 元参['params']
            X, Y, dW, dH, Rto= item_params
            X1,Y1,X2,Y2,X3,Y3=item_data
            x=float((X1+X2+X3)/3) # 以顶点计算出重心
            y=float((Y1+Y2+Y3)/3)

            w=float(dW)*1.1544 # 三棱柱实体不是完整填充的三角
            h=float(dH)*1.3333
            Rot=float(Rto) 
            # 大小
            实体缩放X=w * 全局缩放W
            实体缩放Z=h * 全局缩放H
            # 位置
            实体位置X=(x * 全局缩放W) + 全局偏移X
            实体位置Z=(-y * 全局缩放H) + 全局偏移Y
            # 旋转
            实体旋转Y=Rot
        else:
            pass

        参数[0]=""
        参数[3]=f"{排序ID:02d}" # {排序ID:02d}
        参数[5]=f"{实体GUID}" # GUID
        参数[7]=f"{实体名称}_{序号}" # 名称
        参数[9]=f"{实体GUID}" # GUID
        参数[11]=f"{图形ID}" # 图形ID
        参数[13]=f"{实体名称}_{序号}" # 名称
        参数[15]=f"{静态}" # 静态=1，动态=0
        参数[17]=f"{实体位置X}" # 起始坐标X
        参数[19]=f"{实体位置Y}" # 起始坐标Y
        参数[21]=f"{实体位置Z}" # 起始坐标Z
        参数[23]=f"{实体旋转X}" # 实体旋转X
        参数[25]=f"{实体旋转Y}" # 实体旋转Y
        参数[27]=f"{实体旋转Z}" # 实体旋转Z
        参数[29]=f"{实体缩放X}" # 实体缩放X
        参数[31]=f"{实体缩放Y}" # 实体缩放Y
        参数[33]=f"{实体缩放Z}" # 实体缩放Z
        参数[35]=f"{碰撞}" # 自身碰撞开=1，关=0
        参数[37]=f"{攀爬}" # 可攀爬开=1，关=0
        参数[39]=f"{可见}" # 可见性开=1，关=0
        参数[41]=f"{覆盖装饰颜色}" # 覆盖装饰颜色开=1，关=0
        参数[43]=f"{引用ARGB}" # 引用ARGB
        参数[45]=f"{实体颜色透明度}" # 透明度
        参数[47]=f"{实体颜色}" # 实体RGB
        参数[49]=f"{图形ID}" # 图形ID
        参数[51]=f"{图形ID}" # 图形ID


        实体循环结果="".join(参数) # 拼接数组
        buffer.write(实体循环结果)
        排序ID+=1


    buffer.write(f"{引用参数2}{排序ID:02d}{引用参数3}")
    排序ID+=1
    buffer.write(f"{排序ID:02d}{引用参数4}")

    # ========== 一次性写入文件 ==========
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(buffer.getvalue())
    print(f"本次生成{排序ID}个实体 场景数据写入{output_file}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("用法: python script.py <输入文件> <输出文件>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # 1. 一次性完整加载整个JSON文件
    # 显式指定encoding='utf-8'，避免中文或特殊字符读取异常
    with open(input_file, 'r', encoding='utf-8') as f:
        data_list = json.load(f)  # 直接将整个JSON数组解析为Python列表

    if not isinstance(data_list, list):
        print("警告：JSON文件根节点不是数组格式")
    else:
        element_total = len(data_list)
        print(f"成功加载，数组元素总数：{element_total}")

    # 2. 获取数组中元素的总个数
    element_total = len(data_list)
    print(f"JSON数组中元素总数：{element_total}")

    # 3. 遍历访问每个元素的字段（可选）
    # for index, item in enumerate(data_list):
        # print(f"第{index}个元素：type={item.get('type')}, score={item.get('score')}")

    图元拟合静态实体(data_list,output_file)








