import math

def calculate_isosceles_properties(x1, y1, x2, y2, x3, y3):
    """
    输入等腰三角形三个顶点坐标，计算以高垂线中点为旋转中心的相关几何信息。
    
    参数:
    x1, y1: 顶点1坐标
    x2, y2: 顶点2坐标
    x3, y3: 顶点3坐标
    
    返回:
    dict: 包含 'center_x', 'center_y' (高的中点/旋转中心), 
          'base' (底边长), 'height' (高), 
          'angle_rad' (高的方向角-弧度), 'angle_deg' (高的方向角-角度)
    """
    
    # 1. 定义辅助函数：计算两点间距离
    def dist(xa, ya, xb, yb):
        return math.sqrt((xa - xb)**2 + (ya - yb)**2)
    
    # 2. 计算三边长度
    # c_side 是 AB 边 (对顶点 C)
    # b_side 是 AC 边 (对顶点 B)
    # a_side 是 BC 边 (对顶点 A)
    c_side = dist(x1, y1, x2, y2) # AB
    b_side = dist(x1, y1, x3, y3) # AC
    a_side = dist(x2, y2, x3, y3) # BC
    
    # 设置一个微小的误差阈值，用于浮点数比较
    epsilon = 1.0 # 1e-9
    
    apex_x, apex_y = 0, 0       # 顶角顶点坐标
    base_p1_x, base_p1_y = 0, 0 # 底边端点1
    base_p2_x, base_p2_y = 0, 0 # 底边端点2
    base_len = 0                # 底边长度
    
    is_isosceles = False
    
    # 3. 判断哪条是底边 (寻找两条相等的腰)
    # 情况1: AB == AC (A是顶点, BC是底)
    if abs(c_side - b_side) < epsilon:
        apex_x, apex_y = x1, y1
        base_p1_x, base_p1_y = x2, y2
        base_p2_x, base_p2_y = x3, y3
        base_len = a_side
        is_isosceles = True
    # 情况2: BA == BC (B是顶点, AC是底)
    elif abs(c_side - a_side) < epsilon:
        apex_x, apex_y = x2, y2
        base_p1_x, base_p1_y = x1, y1
        base_p2_x, base_p2_y = x3, y3
        base_len = b_side
        is_isosceles = True
    # 情况3: CA == CB (C是顶点, AB是底)
    elif abs(b_side - a_side) < epsilon:
        apex_x, apex_y = x3, y3
        base_p1_x, base_p1_y = x1, y1
        base_p2_x, base_p2_y = x2, y2
        base_len = c_side
        is_isosceles = True
        
    if not is_isosceles:
        raise ValueError("输入的坐标不构成等腰三角形（没有两条边长度相等）")
        
    # 4. 计算底边中点 (Foot of the altitude, 因为等腰三角形三线合一)
    mid_base_x = (base_p1_x + base_p2_x) / 2.0
    mid_base_y = (base_p1_y + base_p2_y) / 2.0
    
    # 5. 计算高 (顶点到底边中点的距离)
    height_val = dist(apex_x, apex_y, mid_base_x, mid_base_y)
    
    # 6. 计算高的中点 (即旋转中心)
    # 旋转中心 O = (顶点 + 底边中点) / 2
    center_x = (apex_x + mid_base_x) / 2.0
    center_y = (apex_y + mid_base_y) / 2.0
    
    # 7. 计算旋转角度
    # 这里定义为“高”这一向量（从底边中点指向顶点，或者从顶点指向底边中点）与X轴正方向的夹角
    # 通常对称轴的方向向量可以取 V = (apex - mid_base)
    dx = apex_x - mid_base_x
    dy = apex_y - mid_base_y
    
    # atan2 返回弧度值，范围 [-pi, pi]
    angle_rad = math.atan2(dy, dx)
    angle_deg = math.degrees(angle_rad)
    
    return {
        "center_x": center_x,
        "center_y": center_y,
        "base": base_len,
        "height": height_val,
        "angle_rad": angle_rad,
        "angle_deg": angle_deg
    }

# --- 测试示例 ---
if __name__ == "__main__":
    # 示例1: 标准等腰三角形，顶点(0, 4), 底边(-3, 0) 到 (3, 0)
    # 预期: 底=6, 高=4, 中点(0, 2), 角度90度 (垂直向上)
    try:
        res = calculate_isosceles_properties(0, 4, -3, 0, 3, 0)
        print(f"测试1结果:")
        print(f"旋转中心 (X, Y): ({res['center_x']:.4f}, {res['center_y']:.4f})")
        print(f"底边长度: {res['base']:.4f}")
        print(f"高: {res['height']:.4f}")
        print(f"旋转角度 (度): {res['angle_deg']:.4f}")
        print("-" * 30)
    except ValueError as e:
        print(e)

    # 示例2: 斜放的等腰三角形
    # 顶点(1, 1), 底边(0, 0) 和 (2, 0) -> 这是一个等腰直角三角形的变体? 
    # AB=sqrt(2), AC=sqrt(2), BC=2. 
    # 顶点(1,1), 底边中点(1,0). 高=1. 高中点(1, 0.5). 角度90度.
    try:
        res2 = calculate_isosceles_properties(412,340,151,188,383,91)
        print(f"测试2结果:")
        print(f"旋转中心 (X, Y): ({res2['center_x']:.4f}, {res2['center_y']:.4f})")
        print(f"底边长度: {res2['base']:.4f}")
        print(f"高: {res2['height']:.4f}")
        print(f"旋转角度 (度): {res2['angle_deg']:.4f}")
    except ValueError as e:
        print(e)
