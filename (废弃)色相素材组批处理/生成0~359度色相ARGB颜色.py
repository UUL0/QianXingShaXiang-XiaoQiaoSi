def hsl_to_rgb(h, s=1.0, l=0.5):
    """色相转RGB (HSL模型)"""
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2

    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    return int((r + m) * 255), int((g + m) * 255), int((b + m) * 255)


# 生成360个ARGB值
argb_array = []
for h in range(360):
    r, g, b = hsl_to_rgb(h)
    argb = (0xFF << 24) | (r << 16) | (g << 8) | b  # A=255, RGB
    argb_array.append(argb)
# 写入文件
with open("360color_argb.txt", "w", encoding="utf-8") as f:
    for i, val in enumerate(argb_array):
        # f.write(f"  {i:3d}°: {val:#010x}\n")
        f.write(f"{val}, ")
print("✅ 已写入 360color_argb.txt")

# 打印前10个和后10个
print("前10个：")
for i in range(10):
    print(f"  {i:3d}°: {argb_array[i]:#010x}")

print("\n后10个：")
for i in range(350, 360):
    print(f"  {i:3d}°: {argb_array[i]:#010x}")
