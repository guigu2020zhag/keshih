import matplotlib.pyplot as plt

# 设置全局中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 周日期
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# 收盘价数据
closing_prices = [44.98, 45.02, 44.32, 41.05, 42.08, 42.08, 42.08]

# 创建绘图区域
plt.figure(figsize=(10, 6), dpi=100)
plt.subplot(111, position=[0.2, 0.2, 0.5, 0.5])

# 绘制折线图
plt.plot(weekdays, closing_prices, marker='o', linestyle='-', color='b')

# 设置x轴刻度标签倾斜角度为20
plt.xticks(rotation=20)

# 格式化y轴刻度标签为“￥收盘价”
plt.gca().yaxis.set_major_formatter('${:.2f}'.format)

# 调整刻度线样式
plt.tick_params(axis='both', direction='in', width=2)

# 添加网格线
plt.grid(True)

# 添加标题和标签
plt.title('某股票一周的收盘价')
plt.xlabel('周日期')
plt.ylabel('收盘价')

# 显示图形
plt.show()