import matplotlib.pyplot as plt

# 设置全局中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 数据
categories = ['童装', '奶粉辅食', '孕妈专区', '洗护喂养', '宝宝尿裤', '春夏新品', '童车童床', '玩具文娱', '童鞋']
sales = [29665, 3135.4, 4292.4, 5240.9, 5543.4, 5633.8, 6414.5, 9308.1, 10353]

# 计算总销售额
total_sales = sum(sales)

# 计算销售额所占总销售额的百分比
percentages = [(sale / total_sales) * 100 for sale in sales]

# 设置图像大小和dpi
plt.figure(figsize=(10, 6), dpi=100)

# 绘制饼图
plt.pie(sales, labels=categories, autopct='%1.1f%%')

# 添加标题
plt.title('拼多多平台子类目的销售额（考生学号姓名）')

# 添加图例（两列显示）
plt.legend(categories, loc='upper right', bbox_to_anchor=(1.1, 1), ncol=2)

# 显示图形
plt.show()