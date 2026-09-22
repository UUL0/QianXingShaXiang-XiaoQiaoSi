# 使用的核心开源项目：
https://www.geometrize.co.uk/
-
https://www.samcodes.co.uk/project/geometrize-haxe-web/
-

一、拟合图片

geometrizeWeb6由geometrize-haxe-web修改增加等腰三角形选项
-
进入geometrizeWeb6内：

运行命令行：

npx http-server -p 8888 --mime-types .js=application/javascript

浏览器打开：

http://localhost:8888/

----------------

二、转换导出的JSON数据

适量修改py程序文件内的参数：

全局偏移X=-128.0

全局偏移Y=128.0

全局缩放W=0.5

全局缩放H=0.5

线宽=1.5


拖放JSON到bat/cmd文件上运行输出proto文件

----------------

proto到GIA的解、封装使用主页的gia-Protobuf

----------------

type	形状

0	矩形

1	旋转矩形

3	椭圆

4	旋转椭圆

5	圆

6	线段

8	等腰三角形

----------------------
相关程序代码均由AI创作





