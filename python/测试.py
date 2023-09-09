import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 设置中文字体
font_path = "C:\Windows\Fonts\\msyh.ttc"  # 替换为你安装的中文字体文件的路径
chinese_font = fm.FontProperties(fname=font_path)

# 使用中文字体
plt.rcParams['font.family'] = chinese_font.get_name()

# 绘制图形
plt.plot(["啊", 2, 3], [1, 2, 3])
plt.xlabel('中文标签')
plt.ylabel('中文标签')
plt.title('中文标题')
plt.show()
