from io import StringIO
import os
import struct
import sys
import math
import json


# UI素材组封装
# 一个公共容器：素材组，需要一个唯一ID
# 素材内容ID
# 每添加一个素材内容，素材组内需要更新两个列表02:N:embedded message、503:05:repeated
# 
# 
全局偏移X=-128.0
全局偏移Y=128.0
全局缩放W=0.5
全局缩放H=0.5

线宽=1.5


def 生成素材组(data_list,output_file):
    # 通过HEX编辑器或解封装gia，最后几行中查看
    导出参数ID="100000000-1782032127-1073741832" # 你账号导出gia的最后参数字符串(例如：xxxxxxxxx-xxxxxxxxxx-xxxxxxxxxx，似乎是账号UID+"-"+ID1+"-"+ID2)
    版本号="6.7.0" #当前版本的版本号

    # 设定起始初始参数
    索引起始值=1073741843
    生成数量=1

    # 是无符号的4字节
    # 0~360度的色相颜色，360个，0~359，整数十六进制格式AARRGGBB
    ARGB颜色值 = [4294901764]

    # 素材组名称
    素材组名 = "拟合图元_"
    素材内容名 = "D_"
    
    # 程序运行内使用的
    当前生成ID = 0 # 生成计数

    # 未知素材唯一ID，根据生成数量后顺序追加
    素唯一ID起始 = 索引起始值 + (生成数量 * 1)

    # 素材内内容ID
    素材内内容ID = 索引起始值 + (生成数量 * 2)

    # 素材段
    素材组段="  '01:"
    素材内容段="  '02:"
    
    # 排序ID
    排序ID=0
    
    # 素材组信息
    # 缩放（对于素材组本身是无效的）
    组缩X=1.0
    组缩Y=1.0
    组缩Z=1.0
    # 大小
    组W=256.0
    组H=256.0
    # 位置（素材组位置信息，0.0,0.0为屏幕显示中心）
    组位X=0.0
    组位Y=0.0
    
    # 未知2（可能是自定义锚点，但是对于素材组本身无效）
    组锚MinX=0.5
    组锚MinY=0.5
    
    # 未知3（可能是自定义锚点，但是对于素材组本身无效）
    组锚MaxX=0.5
    组锚MaxY=0.5
    
    # 未知4（可能是自定义锚点，但是对于素材组本身无效）
    组锚中心X=0.5
    组锚中心Y=0.5
    
    # 未知5（可能是旋转信息，是空的，没有数值或默认时是空）
    组保留未知5=0.0
    # 素材组内内容信息
    # 缩放
    素缩X=1.0
    素缩Y=1.0
    素缩Z=1.0
    # 大小
    素W=256.0
    素H=256.0
    # 位置（素材组位置信息，0.0,0.0为屏幕显示中心）
    素位X=0.0
    素位Y=0.0
    
    # Min（自定义锚点）
    素锚MinX=0.5
    素锚MinY=0.5
    
    # Max（自定义锚点）
    素锚MaxX=0.5
    素锚MaxY=0.5
    
    # 中心（自定义锚点）
    素锚中心X=0.5
    素锚中心Y=0.5
    
    # 旋转
    素旋=0.0
    
    # 内容引用资产ID
    素内容引用ID = 106092
    
    参数00="{\n"
    # 拼接字符串太多了，这里用字符串数组
    参数组 = [""] * 138 # 列表138个空项

    # 素材组段
    # 排序ID
    参数组[0] = f"{素材组段}{排序ID:02d}"

    参数组[1] = ":embedded message': \n    {\n      '01:00:embedded message': \n        {\n          '02:00:Varint': 1,\n          '03:01:Varint': 8,\n          '04:02:Varint': "
    # 自身素材ID
    参数组[2] = f"{索引起始值 + 当前生成ID}"
    参数组[3] = "\n        },\n"

    内排序ID = 1
    # 自身容器内内容ID
    参数组[4] = ""

    #自身容器内内容ID，列
    容器ID列参1="\n      '02:"
    # {内排序ID:02d}
    容器ID列参2=":embedded message': \n        {\n          '02:00:Varint': 1,\n          '03:01:Varint': 8,\n          '04:02:Varint': "
    # {素材内内容ID + 当前生成ID}
    容器ID列参3="\n        },\n"
    
    自身容器ID列=[]
    当前生成ID=0
    生成N = len(data_list) # 要装入的素材数
    for 当前生成ID in range(生成N): # 生成素材内容ID列
        自身容器ID列.append(f"{容器ID列参1}{内排序ID:02d}{容器ID列参2}{素材内内容ID + 当前生成ID}{容器ID列参3}")
        内排序ID+=1

    参数组[4] = ''.join(自身容器ID列)
    当前生成ID=0

    参数组[5] = "\n      '03:" + f"{内排序ID:02d}" + ":string': '"
    内排序ID+=1
    # 自身名称
    参数组[6] = f"{素材组名}{当前生成ID}"
    参数组[7] = "',\n      '05:" + f"{内排序ID:02d}" + ":Varint': 61,\n      '19:" + f"{内排序ID:02d}" + ":embedded message': \n        {\n          '01:00:embedded message': \n            {\n              '501:00:Varint': "
    内排序ID+=1

    # 自身素材ID
    参数组[8] = f"{索引起始值 + 当前生成ID}"
    参数组[9] = ",\n              '502:01:embedded message': \n                {\n                  '11:00:embedded message': \n                    {\n                      '501:00:Varint': "
    # 自身素材ID
    参数组[10] = f"{索引起始值 + 当前生成ID}"

    未知层ID参1 =  "\n                    },\n                  '501:01:Varint': 1,\n                  '502:02:Varint': 5\n                },\n              '502:02:embedded message': \n                {\n                  '12:00:embedded message': \n                    {\n                      '501:00:Varint': "

    # 未知与素材内容连接、连续ID

    未知层ID = 20

    未知层ID参2 = "\n                    },\n                  '501:01:Varint': 2,\n                  '502:02:Varint': 6\n                },\n              '502:03:embedded message': \n                {\n                  '14:00:embedded message': \n                    {\n                      '501:00:repeated': ["

    参数组[11] = f"{未知层ID参1}{未知层ID}{未知层ID参2}"
    未知层ID+=1


    # 未知自身内唯一数值（ID）
    参数组[12] = f"{素唯一ID起始 + 当前生成ID}"
    参数组[13] = "]\n                    },\n                  '501:01:Varint': 4,\n                  '502:02:Varint': 4\n                },\n              '502:04:embedded message': \n                {\n                  '16:00:embedded message': \n                    {\n                      '11:00:embedded message': \n                        {\n                        },\n                      '501:01:Varint': 1\n                    },\n                  '501:01:Varint': 6,\n                  '502:02:Varint': 55,\n                  '503:03:embedded message': \n                    {\n                      '46:00:embedded message': \n                        {\n                        },\n                      '501:01:Varint': 39,\n                      '502:02:Varint': 55,\n                      '503:03:Varint': 1,\n                      '504:04:embedded message': \n                        {\n                          '02:00:Varint': 1,\n                          '03:01:Varint': 8,\n                          '04:02:Varint': "
    # 自身素材ID
    参数组[14] = f"{索引起始值 + 当前生成ID}"


    # 存素材内容ID，列表
    参数组[15] = "\n                        }\n                    }\n                },\n              '503:05:repeated': ["
    # 自身容器内内容ID
    # 参数组[16] = f"{素材内内容ID + 当前生成ID}"


    自身容器内容ID列表=[]
    当前生成ID=0
    生成N = len(data_list) # 要装入的素材数
    for 当前生成ID in range(生成N): # 生成素材内容ID列
        if 当前生成ID == (生成N - 1): # 最后一次
            自身容器内容ID列表.append(f"{素材内内容ID + 当前生成ID}")
        else:
            自身容器内容ID列表.append(f"{素材内内容ID + 当前生成ID},")

    参数组[16] = ''.join(自身容器内容ID列表)
    当前生成ID=0

    参数组[17] = "],\n              '505:06:embedded message': \n                {\n                  '12:00:embedded message': \n                    {\n                      '501:00:string': '"
    # 自身名称
    参数组[18] = f"{素材组名}{当前生成ID}"
    # 以下是素材组自身的位置缩大小锚点遮罩信息等
    参数组[19] = "'\n                    },\n                  '501:01:Varint': 2,\n                  '502:02:Varint': 15\n                },\n              '505:07:embedded message': \n                {\n                  '11:00:embedded message': \n                    {\n                      '12:00:embedded message': \n                        {\n                        },\n                      '501:01:Varint': 2\n                    },\n                  '501:01:Varint': 1,\n                  '502:02:Varint': 12,\n                  '503:03:embedded message': \n                    {\n                      '13:00:embedded message': \n                        {\n                          '12:00:embedded message': \n                            {\n                              '501:00:embedded message': \n                                {\n                                  '502:00:embedded message': \n                                    {\n                                      '501:00:embedded message': \n                                        {\n                                          '01:00:32-bit': "
    # 组缩放X
    参数组[20] = f"{组缩X}"
    参数组[21] = ",\n                                          '02:01:32-bit': "
    # 组缩放Y
    参数组[22] = f"{组缩Y}"
    参数组[23] = ",\n                                          '03:02:32-bit': "
    # 组缩放Z
    参数组[24] = f"{组缩Z}"
    参数组[25] = "\n                                        },\n                                      '502:01:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组锚MinX
    参数组[26] = f"{组锚MinX}"
    参数组[27] = ",\n                                          '502:01:32-bit': "
    # 组锚MinY
    参数组[28] = f"{组锚MinY}"
    参数组[29] = "\n                                        },\n                                      '503:02:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组锚MaxX
    参数组[30] = f"{组锚MaxX}"
    参数组[31] = ",\n                                          '502:01:32-bit': "
    # 组锚MaxY
    参数组[32] = f"{组锚MaxY}"
    参数组[33] = "\n                                        },\n                                      '504:03:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组位X
    参数组[34] = f"{组位X}"
    参数组[35] = ",\n                                          '502:01:32-bit': "
    # 组位Y
    参数组[36] = f"{组位Y}"
    参数组[37] = "\n                                        },\n                                      '505:04:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组W
    参数组[38] = f"{组W}"
    参数组[39] = ",\n                                          '502:01:32-bit': "
    # 组H
    参数组[40] = f"{组H}"
    参数组[41] = "\n                                        },\n                                      '506:05:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组锚中心X
    参数组[42] = f"{组锚中心X}"
    参数组[43] = ",\n                                          '502:01:32-bit': "
    # 组锚中心Y
    参数组[44] = f"{组锚中心Y}"
    参数组[45] = "\n                                        },\n                                      '508:06:embedded message': \n                                        {\n                                          '03:00:32-bit': "
    # 保留未知（可能是素材组自身旋转）
    参数组[46] = f"{组保留未知5}"
    # 未知的第一次信息
    参数组[47] = "\n                                        }\n                                    }\n                                },\n                              '501:01:embedded message': \n                                {\n                                  '501:00:Varint': 1,\n                                  '502:01:embedded message': \n                                    {\n                                      '501:00:embedded message': \n                                        {\n                                          '01:00:32-bit': "
    # 组缩放X
    参数组[48] =  f"{组缩X}"
    参数组[49] = ",\n                                          '02:01:32-bit': "
    # 组缩放Y
    参数组[50] =  f"{组缩Y}"
    参数组[51] = ",\n                                          '03:02:32-bit': "
    # 组缩放Z
    参数组[52] =  f"{组缩Z}"
    参数组[53] = "\n                                        },\n                                      '502:01:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组锚MinX
    参数组[54] = f"{组锚MinX}"
    参数组[55] = ",\n                                          '502:01:32-bit': "
    # 组锚MinY
    参数组[56] = f"{组锚MinY}"
    参数组[57] = "\n                                        },\n                                      '503:02:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组锚MaxX
    参数组[58] = f"{组锚MaxX}"
    参数组[59] = ",\n                                          '502:01:32-bit': "
    # 组锚MaxY
    参数组[60] = f"{组锚MaxY}"
    参数组[61] = "\n                                        },\n                                      '504:03:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组位X
    参数组[62] =  f"{组位X}"
    参数组[63] = ",\n                                          '502:01:32-bit': "
    # 组位Y
    参数组[64] =  f"{组位Y}"
    参数组[65] = "\n                                        },\n                                      '505:04:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组W
    参数组[66] =  f"{组W}"
    参数组[67] = ",\n                                          '502:01:32-bit': "
    # 组H
    参数组[68] =  f"{组H}"
    参数组[69] = "\n                                        },\n                                      '506:05:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组锚中心X
    参数组[70] = f"{组锚中心X}"
    参数组[71] = ",\n                                          '502:01:32-bit': "
    # 组锚中心Y
    参数组[72] = f"{组锚中心Y}"
    参数组[73] = "\n                                        },\n                                      '508:06:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 保留未知（可能是素材组自身旋转）
    参数组[74] =  f"{组保留未知5}"
    # 未知的第二次信息
    参数组[75] = "\n                                        }\n                                    }\n                                },\n                              '501:02:embedded message': \n                                {\n                                  '501:00:Varint': 2,\n                                  '502:01:embedded message': \n                                    {\n                                      '501:00:embedded message': \n                                        {\n                                          '01:00:32-bit': "
    # 组缩放X
    参数组[76] = f"{组缩X}"
    参数组[77] = ",\n                                          '02:01:32-bit': "
    # 组缩放Y
    参数组[78] = f"{组缩Y}"
    参数组[79] = ",\n                                          '03:02:32-bit': "
    # 组缩放Z
    参数组[80] = f"{组缩Z}"
    参数组[81] = "\n                                        },\n                                      '502:01:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组锚MinX
    参数组[82] = f"{组锚MinX}"
    参数组[83] = ",\n                                          '502:01:32-bit': "
    # 组锚MinY
    参数组[84] = f"{组锚MinY}"
    参数组[85] = "\n                                        },\n                                      '503:02:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组锚MaxX
    参数组[86] = f"{组锚MaxX}"
    参数组[87] = ",\n                                          '502:01:32-bit': "
    # 组锚MaxY
    参数组[88] = f"{组锚MaxY}"
    参数组[89] = "\n                                        },\n                                      '504:03:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组位X
    参数组[90] = f"{组位X}"
    参数组[91] = ",\n                                          '502:01:32-bit': "
    # 组位Y
    参数组[92] = f"{组位Y}"
    参数组[93] = "\n                                        },\n                                      '505:04:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组W
    参数组[94] = f"{组W}"
    参数组[95] = ",\n                                          '502:01:32-bit': "
    # 组H
    参数组[96] = f"{组H}"
    参数组[97] = "\n                                        },\n                                      '506:05:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组锚中心X
    参数组[98] = f"{组锚中心X}"
    参数组[99] = ",\n                                          '502:01:32-bit': "
    # 组锚中心Y
    参数组[100] = f"{组锚中心Y}"
    参数组[101] = "\n                                        },\n                                      '508:06:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 保留未知（可能是素材组自身旋转）
    参数组[102] = f"{组保留未知5}"
    # 未知的第三次信息
    参数组[103] = "\n                                        }\n                                    }\n                                },\n                              '501:03:embedded message': \n                                {\n                                  '501:00:Varint': 3,\n                                  '502:01:embedded message': \n                                    {\n                                      '501:00:embedded message': \n                                        {\n                                          '01:00:32-bit': "
    # 组缩放X
    参数组[104] = f"{组缩X}"
    参数组[105] = ",\n                                          '02:01:32-bit': "
    # 组缩放Y
    参数组[106] = f"{组缩Y}"
    参数组[107] = ",\n                                          '03:02:32-bit': "
    # 组缩放Z
    参数组[108] = f"{组缩Z}"
    参数组[109] = "\n                                        },\n                                      '502:01:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组锚MinX
    参数组[110] = f"{组锚MinX}"
    参数组[111] = ",\n                                          '502:01:32-bit': "
    # 组锚MinY
    参数组[112] = f"{组锚MinY}"
    参数组[113] = "\n                                        },\n                                      '503:02:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组锚MaxX
    参数组[114] = f"{组锚MaxX}"
    参数组[115] = ",\n                                          '502:01:32-bit': "
    # 组锚MaxY
    参数组[116] = f"{组锚MaxY}"
    参数组[117] = "\n                                        },\n                                      '504:03:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组位X
    参数组[118] = f"{组位X}"
    参数组[119] = ",\n                                          '502:01:32-bit': "
    # 组位Y
    参数组[120] = f"{组位Y}"
    参数组[121] = "\n                                        },\n                                      '505:04:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组W
    参数组[122] = f"{组W}"
    参数组[123] = ",\n                                          '502:01:32-bit': "
    # 组H
    参数组[124] = f"{组H}"
    参数组[125] = "\n                                        },\n                                      '506:05:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 组锚中心X
    参数组[126] = f"{组锚中心X}"
    参数组[127] = ",\n                                          '502:01:32-bit': "
    # 组锚中心Y
    参数组[128] = f"{组锚中心Y}"
    参数组[129] = "\n                                        },\n                                      '508:06:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 保留未知（可能是素材组自身旋转）
    参数组[130] = f"{组保留未知5}"
    参数组[131] = "\n                                        }\n                                    }\n                                },\n                              '504:04:Varint': 1\n                            },\n                          '501:01:Varint': 2\n                        },\n                      '501:01:Varint': 4,\n                      '502:02:Varint': 12,\n                      '503:03:Varint': 1,\n                      '504:04:embedded message': \n                        {\n                          '02:00:Varint': 1,\n                          '03:01:Varint': 8,\n                          '04:02:Varint': "
    # 自身素材ID
    参数组[132] = f"{索引起始值 + 当前生成ID}"
    参数组[133] = "\n                        }\n                    }\n                },\n              '505:08:embedded message': \n                {\n                  '14:00:embedded message': \n                    {\n                      '15:00:embedded message': \n                        {\n                        },\n                      '501:01:Varint': 5\n                    },\n                  '501:01:Varint': 4,\n                  '502:02:Varint': 23,\n                  '503:03:embedded message': \n                    {\n                      '14:00:embedded message': \n                        {\n                          '15:00:embedded message': \n                            {\n                            },\n                          '501:01:Varint': 5\n                        },\n                      '501:01:Varint': 5,\n                      '502:02:Varint': 23,\n                      '503:03:Varint': 1,\n                      '504:04:embedded message': \n                        {\n                          '02:00:Varint': 1,\n                          '03:01:Varint': 8,\n                          '04:02:Varint': "
    # 自身素材ID
    参数组[134] = f"{索引起始值 + 当前生成ID}"
    # 以下包含遮罩信息，形状位置大小等
    参数组[135] = "\n                        }\n                    }\n                },\n              '505:09:embedded message': \n                {\n                  '46:00:embedded message': \n                    {\n                    },\n                  '501:01:Varint': 38,\n                  '502:02:Varint': 56,\n                  '503:03:embedded message': \n                    {\n                      '47:00:embedded message': \n                        {\n                          '01:00:embedded message': \n                            {\n                            },\n                          '02:01:embedded message': \n                            {\n                              '501:00:32-bit': 50.0,\n                              '502:01:32-bit': 50.0\n                            },\n                          '03:02:Varint': 2\n                        },\n                      '501:01:Varint': 40,\n                      '502:02:Varint': 56,\n                      '503:03:Varint': 1,\n                      '504:04:embedded message': \n                        {\n                          '02:00:Varint': 1,\n                          '03:01:Varint': 8,\n                          '04:02:Varint': "
    # 自身素材ID
    参数组[136] = f"{索引起始值 + 当前生成ID}"
    参数组[137] = "\n                        }\n                    }\n                }\n            }\n        }\n    },\n"

    # 拼合参数 = "".join(参数组) # 拼接数组

    内参数组 = [""] * 137 # 列表137个空项
    # 素材内容段
    内参数组[0] = 素材内容段
    # 排序ID
    内参数组[1] = f"{排序ID:02d}"
    内参数组[2] = ":embedded message': \n    {\n      '01:00:embedded message': \n        {\n          '02:00:Varint': 1,\n          '03:01:Varint': 8,\n          '04:02:Varint': "
    # 容器内容ID
    内参数组[3] = f"{素材内内容ID + 当前生成ID}"
    内参数组[4] = "\n        },\n      '03:01:string': '"
    # 素材内容名
    内参数组[5] = f"{素材内容名}{当前生成ID}"
    内参数组[6] = "',\n      '05:02:Varint': 15,\n      '19:03:embedded message': \n        {\n          '01:00:embedded message': \n            {\n              '501:00:Varint': "

    # 容器内容ID
    内参数组[7] = f"{素材内内容ID + 当前生成ID}"
    内参数组[8] = ",\n              '502:01:embedded message': \n                {\n                  '11:00:embedded message': \n                    {\n                      '501:00:Varint': "
    # 容器内容ID
    内参数组[9] = f"{素材内内容ID + 当前生成ID}"

    未知层ID参3 = "\n                    },\n                  '501:01:Varint': 1,\n                  '502:02:Varint': 5\n                },\n              '502:02:embedded message': \n                {\n                  '12:00:embedded message': \n                    {\n                      '501:00:Varint': "


    未知层ID参4 = "\n                    },\n                  '501:01:Varint': 2,\n                  '502:02:Varint': 6\n                },\n              '504:03:Varint': "

    内参数组[10] =  f"{未知层ID参3}{未知层ID}{未知层ID参4}"

    # 容器对应的素材组ID
    内参数组[11] = f"{索引起始值 + 当前生成ID}"
    内参数组[12] = ",\n              '505:04:embedded message': \n                {\n                  '12:00:embedded message': \n                    {\n                      '501:00:string': '"
    # 素材内容名
    内参数组[13] = f"{素材内容名}{当前生成ID}"
    内参数组[14] = "'\n                    },\n                  '501:01:Varint': 2,\n                  '502:02:Varint': 15\n                },\n              '505:05:embedded message': \n                {\n                  '14:00:embedded message': \n                    {\n                      '15:00:embedded message': \n                        {\n                        },\n                      '501:01:Varint': 5\n                    },\n                  '501:01:Varint': 4,\n                  '502:02:Varint': 23,\n                  '503:03:embedded message': \n                    {\n                      '14:00:embedded message': \n                        {\n                          '15:00:embedded message': \n                            {\n                            },\n                          '501:01:Varint': 5\n                        },\n                      '501:01:Varint': 5,\n                      '502:02:Varint': 23,\n                      '503:03:Varint': 1,\n                      '504:04:embedded message': \n                        {\n                          '02:00:Varint': 1,\n                          '03:01:Varint': 8,\n                          '04:02:Varint': "
    # 容器内容ID
    内参数组[15] = f"{素材内内容ID + 当前生成ID}"
    # 以下是容器素材的位置大小信息等
    内参数组[16] = "\n                        }\n                    }\n                },\n              '505:06:embedded message': \n                {\n                  '11:00:embedded message': \n                    {\n                      '12:00:embedded message': \n                        {\n                        },\n                      '501:01:Varint': 2\n                    },\n                  '501:01:Varint': 1,\n                  '502:02:Varint': 12,\n                  '503:03:embedded message': \n                    {\n                      '13:00:embedded message': \n                        {\n                          '12:00:embedded message': \n                            {\n                              '501:00:embedded message': \n                                {\n                                  '502:00:embedded message': \n                                    {\n                                      '501:00:embedded message': \n                                        {\n                                          '01:00:32-bit': "
    # 素缩X
    内参数组[17] = f"{素缩X}"
    内参数组[18] = ",\n                                          '02:01:32-bit': "
    # 素缩Y
    内参数组[19] = f"{素缩Y}"
    内参数组[20] = ",\n                                          '03:02:32-bit': "
    # 素缩Z
    内参数组[21] = f"{素缩Z}"
    内参数组[22] = "\n                                        },\n                                      '502:01:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素锚MinX
    内参数组[23] = f"{素锚MinX}"
    内参数组[24] = ",\n                                          '502:01:32-bit': "
    # 素锚MinY
    内参数组[25] = f"{素锚MinY}"
    内参数组[26] = "\n                                        },\n                                      '503:02:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素锚MaxX
    内参数组[27] = f"{素锚MaxX}"
    内参数组[28] = ",\n                                          '502:01:32-bit': "
    # 素锚MaxY
    内参数组[29] = f"{素锚MaxY}"
    内参数组[30] = "\n                                        },\n                                      '504:03:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素位X
    内参数组[31] = f"{素位X}"
    内参数组[32] = ",\n                                          '502:01:32-bit': "
    # 素位Y
    内参数组[33] = f"{素位Y}"
    内参数组[34] = "\n                                        },\n                                      '505:04:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素W
    内参数组[35] = f"{素W}"
    内参数组[36] = ",\n                                          '502:01:32-bit': "
    # 素H
    内参数组[37] = f"{素H}"
    内参数组[38] = "\n                                        },\n                                      '506:05:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素锚中心X
    内参数组[39] = f"{素锚中心X}"
    内参数组[40] = ",\n                                          '502:01:32-bit': "
    #  素锚中心Y
    内参数组[41] = f"{素锚中心Y}"
    内参数组[42] = "\n                                        },\n                                      '508:06:embedded message': \n                                        {\n                                          '03:00:32-bit': "
    # 素旋
    内参数组[43] = f"{素旋}"
    # 以下是未知第一次信息
    内参数组[44] = "\n                                        }\n                                    }\n                                },\n                              '501:01:embedded message': \n                                {\n                                  '501:00:Varint': 1,\n                                  '502:01:embedded message': \n                                    {\n                                      '501:00:embedded message': \n                                        {\n                                          '01:00:32-bit': "
    # 素缩X
    内参数组[45] = f"{素缩X}"
    内参数组[46] = ",\n                                          '02:01:32-bit': "
    # 素缩Y
    内参数组[47] = f"{素缩Y}"
    内参数组[48] = "0,\n                                          '03:02:32-bit': "
    # 素缩Z
    内参数组[49] = f"{素缩Z}"
    内参数组[50] = "\n                                        },\n                                      '502:01:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素锚MinX
    内参数组[51] = f"{素锚MinX}"
    内参数组[52] = ",\n                                          '502:01:32-bit': "
    # 素锚MinY
    内参数组[53] = f"{素锚MinY}"
    内参数组[54] = "\n                                        },\n                                      '503:02:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素锚MaxX
    内参数组[55] = f"{素锚MaxX}"
    内参数组[56] = ",\n                                          '502:01:32-bit': "
    # 素锚MaxY
    内参数组[57] = f"{素锚MaxY}"
    内参数组[58] = "\n                                        },\n                                      '504:03:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素位X
    内参数组[59] = f"{素位X}"
    内参数组[60] = ",\n                                          '502:01:32-bit': "
    # 素位Y
    内参数组[61] = f"{素位Y}"
    内参数组[62] = "\n                                        },\n                                      '505:04:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素W
    内参数组[63] = f"{素W}"
    内参数组[64] = ",\n                                          '502:01:32-bit': "
    # 素H
    内参数组[65] = f"{素H}"
    内参数组[66] = "\n                                        },\n                                      '506:05:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素锚中心X
    内参数组[67] = f"{素锚中心X}"
    内参数组[68] = ",\n                                          '502:01:32-bit': "
    # 素锚中心Y
    内参数组[69] = f"{素锚中心Y}"
    内参数组[70] = "\n                                        },\n                                      '508:06:embedded message': \n                                        {\n                                          '03:00:32-bit':"
    # 素旋
    内参数组[71] = f"{素旋}"
    # 以下是未知第二次信息
    内参数组[72] = "\n                                        }\n                                    }\n                                },\n                              '501:02:embedded message': \n                                {\n                                  '501:00:Varint': 2,\n                                  '502:01:embedded message': \n                                    {\n                                      '501:00:embedded message': \n                                        {\n                                          '01:00:32-bit': "
    # 素缩X
    内参数组[73] = f"{素缩X}"
    内参数组[74] = ",\n                                          '02:01:32-bit': "
    # 素缩Y
    内参数组[75] = f"{素缩Y}"
    内参数组[76] = "0,\n                                          '03:02:32-bit': "
    # 素缩Z
    内参数组[77] = f"{素缩Z}"
    内参数组[78] = "\n                                        },\n                                      '502:01:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素锚MinX
    内参数组[79] = f"{素锚MinX}"
    内参数组[80] = ",\n                                          '502:01:32-bit': "
    # 素锚MinY
    内参数组[81] = f"{素锚MinY}"
    内参数组[82] = "\n                                        },\n                                      '503:02:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素锚MaxX
    内参数组[83] = f"{素锚MaxX}"
    内参数组[84] = ",\n                                          '502:01:32-bit': "
    # 素锚MaxY
    内参数组[85] = f"{素锚MaxY}"
    内参数组[86] = "\n                                        },\n                                      '504:03:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素位X
    内参数组[87] = f"{素位X}"
    内参数组[88] = ",\n                                          '502:01:32-bit': "
    # 素位Y
    内参数组[89] = f"{素位Y}"
    内参数组[90] = "\n                                        },\n                                      '505:04:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素W
    内参数组[91] = f"{素W}"
    内参数组[92] = ",\n                                          '502:01:32-bit': "
    # 素H
    内参数组[93] = f"{素H}"
    内参数组[94] = "\n                                        },\n                                      '506:05:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素锚中心X
    内参数组[95] = f"{素锚中心X}"
    内参数组[96] = ",\n                                          '502:01:32-bit': "
    # 素锚中心Y
    内参数组[97] = f"{素锚中心Y}"
    内参数组[98] = "\n                                        },\n                                      '508:06:embedded message': \n                                        {\n                                          '03:00:32-bit':"
    # 素旋
    内参数组[99] = f"{素旋}"
    # 以下是未知第三次信息
    内参数组[100] = "\n                                        }\n                                    }\n                                },\n                              '501:03:embedded message': \n                                {\n                                  '501:00:Varint': 3,\n                                  '502:01:embedded message': \n                                    {\n                                      '501:00:embedded message': \n                                        {\n                                          '01:00:32-bit': "
    # 素缩放X
    内参数组[101] = f"{素缩X}"
    内参数组[102] = ",\n                                          '02:01:32-bit': "
    # 素缩放Y
    内参数组[103] = f"{素缩Y}"
    内参数组[104] = "0,\n                                          '03:02:32-bit': "
    # 素缩放Z
    内参数组[105] = f"{素缩Z}"
    内参数组[106] = "\n                                        },\n                                      '502:01:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素锚MinX
    内参数组[107] = f"{素锚MinX}"
    内参数组[108] = ",\n                                          '502:01:32-bit': "
    # 素锚MinY
    内参数组[109] = f"{素锚MinY}"
    内参数组[110] = "\n                                        },\n                                      '503:02:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素锚MaxX
    内参数组[111] = f"{素锚MaxX}"
    内参数组[112] = ",\n                                          '502:01:32-bit': "
    # 素锚MaxY
    内参数组[113] = f"{素锚MaxY}"
    内参数组[114] = "\n                                        },\n                                      '504:03:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素位X
    内参数组[115] =  f"{素位X}"
    内参数组[116] = ",\n                                          '502:01:32-bit': "
    # 素位Y
    内参数组[117] =  f"{素位Y}"
    内参数组[118] = "\n                                        },\n                                      '505:04:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素W
    内参数组[119] = f"{素W}"
    内参数组[120] = ",\n                                          '502:01:32-bit': "
    # 素H
    内参数组[121] = f"{素H}"
    内参数组[122] = "\n                                        },\n                                      '506:05:embedded message': \n                                        {\n                                          '501:00:32-bit': "
    # 素锚中心X
    内参数组[123] = f"{素锚中心X}"
    内参数组[124] = ",\n                                          '502:01:32-bit': "
    # 素锚中心Y
    内参数组[125] = f"{素锚中心Y}"
    内参数组[126] = "\n                                        },\n                                      '508:06:embedded message': \n                                        {\n                                          '03:00:32-bit':"
    # 素旋
    内参数组[127] = f"{素旋}"
    # 以下是素材的设置引用、颜色、拉伸模式等
    内参数组[128] = "\n                                        }\n                                    }\n                                },\n                              '502:04:Varint': 9,\n                              '504:05:Varint': 1\n                            },\n                          '501:01:Varint': 2\n                        },\n                      '501:01:Varint': 4,\n                      '502:02:Varint': 12,\n                      '503:03:Varint': 1,\n                      '504:04:embedded message': \n                        {\n                          '02:00:Varint': 1,\n                          '03:01:Varint': 8,\n                          '04:02:Varint': "
    # 容器内容ID
    内参数组[129] = f"{素材内内容ID + 当前生成ID}"
    内参数组[130] = "\n                        }\n                    }\n                },\n              '505:07:embedded message': \n                {\n                  '31:00:embedded message': \n                    {\n                    },\n                  '501:01:Varint': 21,\n                  '502:02:Varint': 38,\n                  '503:03:embedded message': \n                    {\n                      '31:00:embedded message': \n                        {\n                          '02:00:Varint': "
    # 静态引用资产ID
    内参数组[131] = f"{素内容引用ID}"
    内参数组[132] = ",\n                          '03:01:embedded message': \n                            {\n                              '501:00:Varint': 18446744073709551615\n                            },\n                          '04:02:Varint': "
    # 填充颜色（ARGB）
    内参数组[133] = f"{ARGB颜色值[当前生成ID]}"
    # 05:03:Varint': 0应该是基础，1是拉伸
    内参数组[134] = ",\n                          '05:03:Varint': 0,\n                          '06:04:embedded message': \n                            {\n                            },\n                          '10:05:embedded message': \n                            {\n                            }\n                        },\n                      '501:01:Varint': 22,\n                      '502:02:Varint': 38,\n                      '503:03:Varint': 1,\n                      '504:04:embedded message': \n                        {\n                          '02:00:Varint': 1,\n                          '03:01:Varint': 8,\n                          '04:02:Varint': "
    # 容器内容ID
    内参数组[135] = f"{素材内内容ID + 当前生成ID}"
    内参数组[136] = "\n                        }\n                    }\n                }\n            }\n        }\n    },\n"





    引用参数2="  '03:"
    引用参数3=":string': '"
    引用参数4="-\\图元UI拟合素材组00.gia',\n"
    引用参数5="  '05:"
    引用参数6=":string': '"
    版本号="6.7.0"
    引用参数7="'\n}"

    

    # 写入文件流程：
    # 参数00
    # 素材组循环
    # 
    # 素材组循环结束
    
    # 素材内容循环
    # 
    # 素材内容循环结束
    
    # 引用参数2+排序ID+引用参数3+导出参数ID+引用参数4+引用参数5+排序ID+引用参数6+版本号+引用参数7

    # 预拼接模板 + StringIO 批量写入
    # 缓冲区
    buffer = StringIO()

    # 开始

    buffer.write(参数00)
    当前生成ID = 0
    for 当前生成ID in range(生成数量): # 生成循环，先生成素材组容器
        参数组[0] = f"{素材组段}{排序ID:02d}"
        参数组[2] = f"{索引起始值 + 当前生成ID}"
        # 参数组[4] = f"{素材内内容ID + 当前生成ID}"
        参数组[6] = f"{素材组名}{当前生成ID}"
        参数组[8] = f"{索引起始值 + 当前生成ID}"
        参数组[10] = f"{索引起始值 + 当前生成ID}"
        参数组[12] = f"{素唯一ID起始 + 当前生成ID}"
        参数组[14] = f"{索引起始值 + 当前生成ID}"
        # 参数组[16] = f"{素材内内容ID + 当前生成ID}"
        参数组[18] = f"{素材组名}{当前生成ID}"
        参数组[20] = f"{组缩X}"
        参数组[22] = f"{组缩Y}"
        参数组[24] = f"{组缩Z}"
        参数组[26] = f"{组锚MinX}"
        参数组[28] = f"{组锚MinY}"
        参数组[30] = f"{组锚MaxX}"
        参数组[32] = f"{组锚MaxY}"
        参数组[34] = f"{组位X}"
        参数组[36] = f"{组位Y}"
        参数组[38] = f"{组W}"
        参数组[40] = f"{组H}"
        参数组[42] = f"{组锚中心X}"
        参数组[44] = f"{组锚中心Y}"
        参数组[46] = f"{组保留未知5}"
        参数组[48] =  f"{组缩X}"
        参数组[50] =  f"{组缩Y}"
        参数组[52] =  f"{组缩Z}"
        参数组[54] = f"{组锚MinX}"
        参数组[56] = f"{组锚MinY}"
        参数组[58] = f"{组锚MaxX}"
        参数组[60] = f"{组锚MaxY}"
        参数组[62] =  f"{组位X}"
        参数组[64] =  f"{组位Y}"
        参数组[66] =  f"{组W}"
        参数组[68] =  f"{组H}"
        参数组[70] = f"{组锚中心X}"
        参数组[72] = f"{组锚中心Y}"
        参数组[74] =  f"{组保留未知5}"
        参数组[76] = f"{组缩X}"
        参数组[78] = f"{组缩Y}"
        参数组[80] = f"{组缩Z}"
        参数组[82] = f"{组锚MinX}"
        参数组[84] = f"{组锚MinY}"
        参数组[86] = f"{组锚MaxX}"
        参数组[88] = f"{组锚MaxY}"
        参数组[90] = f"{组位X}"
        参数组[92] = f"{组位Y}"
        参数组[94] = f"{组W}"
        参数组[96] = f"{组H}"
        参数组[98] = f"{组锚中心X}"
        参数组[100] = f"{组锚中心Y}"
        参数组[102] = f"{组保留未知5}"
        参数组[104] = f"{组缩X}"
        参数组[106] = f"{组缩Y}"
        参数组[108] = f"{组缩Z}"
        参数组[110] = f"{组锚MinX}"
        参数组[112] = f"{组锚MinY}"
        参数组[114] = f"{组锚MaxX}"
        参数组[116] = f"{组锚MaxY}"
        参数组[118] = f"{组位X}"
        参数组[120] = f"{组位Y}"
        参数组[122] = f"{组W}"
        参数组[124] = f"{组H}"
        参数组[126] = f"{组锚中心X}"
        参数组[128] = f"{组锚中心Y}"
        参数组[130] = f"{组保留未知5}"
        参数组[132] = f"{索引起始值 + 当前生成ID}"
        参数组[134] = f"{索引起始值 + 当前生成ID}"
        参数组[136] = f"{索引起始值 + 当前生成ID}"

        拼合参数 = "".join(参数组) # 拼接数组
        buffer.write(拼合参数)
        排序ID+=1


    生成素数量 = len(data_list) # 要装入的素材数
    当前生成ID = 0
    for 当前生成ID in range(生成素数量): # 生成循环，生成素材组内的内容
        # 获取一个元素
        元参=data_list[生成素数量-当前生成ID-1] 
        # 1. 获取 type
        item_type = 元参['type']
        # 2. 获取 data (列表)
        item_data = 元参['data']
        # 3. 获取 color (列表 [R, G, B, A])
        item_color_rgba = 元参['color']

        # 将 [R, G, B, A] 列表转换为 ARGB 格式的 32位整数
        Cr, Cg, Cb, Ca = item_color_rgba # 解包获取各通道值
        Cr, Cg, Cb, Ca = int(Cr), int(Cg), int(Cb), int(Ca) # 确保值在 0-255 范围内
        ARGB_int = (Ca << 24) | (Cr << 16) | (Cg << 8) | Cb

        if item_type == 0: # 矩形
            素内容引用ID = 100001 # 矩形
            X1, Y1, X2, Y2 = item_data
            x=float((X1+X2)/2)
            y=float((Y1+Y2)/2)
            w=float(X2-X1)
            h=float(Y2-Y1)
            # 大小
            素W=w * 全局缩放W
            素H=h * 全局缩放H
            # 位置（素材组位置信息，0.0,0.0为屏幕显示中心）
            素位X=(x * 全局缩放W) + 全局偏移X
            素位Y=(-y * 全局缩放H) + 全局偏移Y
            # 旋转
            素旋=float(0.0)
        elif item_type == 1: # 旋转矩形
            素内容引用ID = 100001 # 矩形
            X1, Y1, X2, Y2, Rto= item_data
            x=float((X1+X2)/2)
            y=float((Y1+Y2)/2)
            w=float(X2-X1)
            h=float(Y2-Y1)
            Rot=float(Rto) 
            if Rot>180:
                Rot=Rot-180
            # 大小
            素W=w * 全局缩放W
            素H=h * 全局缩放H
            # 位置
            素位X=(x * 全局缩放W) + 全局偏移X
            素位Y=(-y * 全局缩放H) + 全局偏移Y
            # 旋转
            素旋=-Rot
        elif item_type == 3: # 椭圆
            素内容引用ID = 100002 # 圆形
            X, Y, RX, RY= item_data
            x=float(X)
            y=float(Y)
            w=float(RX*2)
            h=float(RY*2)
            # 大小
            素W=w * 全局缩放W
            素H=h * 全局缩放H
            # 位置
            素位X=(x * 全局缩放W) + 全局偏移X
            素位Y=(-y * 全局缩放H) + 全局偏移Y
            # 旋转
            素旋=float(0.0)
        elif item_type == 4: # 旋转椭圆
            素内容引用ID = 100002 # 圆形
            X, Y, RX, RY, Rto= item_data
            x=float(X)
            y=float(Y)
            w=float(RX*2)
            h=float(RY*2)
            Rot=float(Rto) 
            if Rot>180:
                Rot=Rot-180
            # 大小
            素W=w * 全局缩放W
            素H=h * 全局缩放H
            # 位置
            素位X=(x * 全局缩放W) + 全局偏移X
            素位Y=(-y * 全局缩放H) + 全局偏移Y
            # 旋转
            素旋=-Rot
        elif item_type == 5: # 圆
            素内容引用ID = 100002 # 圆形
            X, Y, R= item_data
            x=float(X)
            y=float(Y)
            w=float(R*2)
            h=float(R*2)
            # 大小
            素W=w * 全局缩放W
            素H=h * 全局缩放H
            # 位置
            素位X=(x * 全局缩放W) + 全局偏移X
            素位Y=(-y * 全局缩放H) + 全局偏移Y
            # 旋转
            素旋=float(0.0)
        elif item_type == 6: # 线
            素内容引用ID = 100001 # 矩形
            素内容引用ID = 100001 # 矩形
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
            if Rot>180:
                Rot=Rot-180
            # 大小
            素W=w * 全局缩放W
            素H=h * 全局缩放H
            # 位置
            素位X=(x * 全局缩放W) + 全局偏移X
            素位Y=(-y * 全局缩放H) + 全局偏移Y
            # 旋转
            素旋=Rot
        elif item_type == 8: # 等腰三角
            素内容引用ID = 100003 # 三角形
            item_params = 元参['params']
            X, Y, dW, dH, Rto= item_params
            x=float(X)
            y=float(Y)
            w=float(dW)
            h=float(dH)
            Rot=float(Rto) 
            Rot=180.0-Rot
            # 大小
            素W=w * 全局缩放W
            素H=h * 全局缩放H
            # 位置
            素位X=(x * 全局缩放W) + 全局偏移X
            素位Y=(-y * 全局缩放H) + 全局偏移Y
            # 旋转
            素旋=Rot
        else:
            pass
            

        内参数组[0] = 素材内容段
        内参数组[1] = f"{排序ID:02d}"
        内参数组[3] = f"{素材内内容ID + 当前生成ID}"
        内参数组[5] = f"{素材内容名}{当前生成ID}"
        内参数组[7] = f"{素材内内容ID + 当前生成ID}"
        内参数组[9] = f"{素材内内容ID + 当前生成ID}"

        内参数组[10] =  f"{未知层ID参3}{未知层ID}{未知层ID参4}"
        未知层ID+=1

        # 内参数组[11] = f"{索引起始值 + 当前生成ID}"
        内参数组[11] = f"{索引起始值 + 0}"

        内参数组[13] = f"{素材内容名}{当前生成ID}"
        内参数组[15] = f"{素材内内容ID + 当前生成ID}"
        内参数组[17] = f"{素缩X}"
        内参数组[19] = f"{素缩Y}"
        内参数组[21] = f"{素缩Z}"
        内参数组[23] = f"{素锚MinX}"
        内参数组[25] = f"{素锚MinY}"
        内参数组[27] = f"{素锚MaxX}"
        内参数组[29] = f"{素锚MaxY}"
        内参数组[31] = f"{素位X}"
        内参数组[33] = f"{素位Y}"
        内参数组[35] = f"{素W}"
        内参数组[37] = f"{素H}"
        内参数组[39] = f"{素锚中心X}"
        内参数组[41] = f"{素锚中心Y}"
        内参数组[43] = f"{素旋}"
        内参数组[45] = f"{素缩X}"
        内参数组[47] = f"{素缩Y}"
        内参数组[49] = f"{素缩Z}"
        内参数组[51] = f"{素锚MinX}"
        内参数组[53] = f"{素锚MinY}"
        内参数组[55] = f"{素锚MaxX}"
        内参数组[57] = f"{素锚MaxY}"
        内参数组[59] = f"{素位X}"
        内参数组[61] = f"{素位Y}"
        内参数组[63] = f"{素W}"
        内参数组[65] = f"{素H}"
        内参数组[67] = f"{素锚中心X}"
        内参数组[69] = f"{素锚中心Y}"
        内参数组[71] = f"{素旋}"
        内参数组[73] = f"{素缩X}"
        内参数组[75] = f"{素缩Y}"
        内参数组[77] = f"{素缩Z}"
        内参数组[79] = f"{素锚MinX}"
        内参数组[81] = f"{素锚MinY}"
        内参数组[83] = f"{素锚MaxX}"
        内参数组[85] = f"{素锚MaxY}"
        内参数组[87] = f"{素位X}"
        内参数组[89] = f"{素位Y}"
        内参数组[91] = f"{素W}"
        内参数组[93] = f"{素H}"
        内参数组[95] = f"{素锚中心X}"
        内参数组[97] = f"{素锚中心Y}"
        内参数组[99] = f"{素旋}"
        内参数组[101] = f"{素缩X}"
        内参数组[103] = f"{素缩Y}"
        内参数组[105] = f"{素缩Z}"
        内参数组[107] = f"{素锚MinX}"
        内参数组[109] = f"{素锚MinY}"
        内参数组[111] = f"{素锚MaxX}"
        内参数组[113] = f"{素锚MaxY}"
        内参数组[115] =  f"{素位X}"
        内参数组[117] =  f"{素位Y}"
        内参数组[119] = f"{素W}"
        内参数组[121] = f"{素H}"
        内参数组[123] = f"{素锚中心X}"
        内参数组[125] = f"{素锚中心Y}"
        内参数组[127] = f"{素旋}"
        内参数组[129] = f"{素材内内容ID + 当前生成ID}"
        内参数组[131] = f"{素内容引用ID}"
        内参数组[133] = f"{ARGB_int}"
        内参数组[135] = f"{素材内内容ID + 当前生成ID}"

        拼合参数 = "".join(内参数组) # 拼接数组
        buffer.write(拼合参数)
        排序ID+=1

    buffer.write(f"{引用参数2}{排序ID:02d}{引用参数3}{导出参数ID}{引用参数4}{引用参数5}{排序ID+1:02d}{引用参数6}{版本号}{引用参数7}")

    # ========== 一次性写入文件 ==========
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(buffer.getvalue())
    print(f"本次生成：{生成数量}个素材组；{当前生成ID+1}个素材 数据写入{output_file}")



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

    生成素材组(data_list,output_file)








