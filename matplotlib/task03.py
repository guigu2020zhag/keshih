import matplotlib.pyplot as plt

# 设置全局中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 月份
months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']

# 2020年业务量数据
volume_2020 = [39, 20, 40, 38, 42, 43, 41, 41, 45, 48, 52, 50]

# 2021年业务量数据
volume_2021 = [45, 28, 48, 49, 50, 51, 50, 50, 51, 52, 70, 65]

# 创建折线图
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(months, volume_2020, marker='^', color='#8B0000', linestyle='--', linewidth=1.5, label='2020年业务量')
plt.plot(months, volume_2021, marker='D', color='#006374', linestyle='-', linewidth=1.5, label='2021年业务量')

# 添加网格线
plt.grid(True)

# 添加标题和标签
plt.title('2020、2021年物流行业的快递业务量（考生学号姓名）')
plt.xlabel('月份')
plt.ylabel('业务量（亿件）')

# 添加图例
plt.legend()

# 显示图形
plt.show()