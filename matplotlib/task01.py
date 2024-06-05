import matplotlib.pyplot as plt

# 设置全局中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 数据
subjects = ['语文', '数学', '英语', '物理', '化学', '生物']
avg_scores_male = [85.5, 91, 72, 59, 66, 55]
avg_scores_female = [94, 82, 89.5, 62, 49, 53]

# 设置图像大小和dpi
plt.figure(figsize=(10, 6), dpi=100)

# 绘制柱形图
bar_width = 0.35
index = range(len(subjects))
plt.bar(index, avg_scores_male, bar_width, label='男生')
plt.bar([i + bar_width for i in index], avg_scores_female, bar_width, label='女生')

# 设置x轴刻度标签
plt.xticks([i + bar_width/2 for i in index], subjects)

# 添加标题和标签
plt.title('高二男生、女生的平均成绩（考生学号姓名）')
plt.ylabel('平均成绩（分）')
plt.legend()

# 显示图形
plt.show()