from pyecharts import options as opts
from pyecharts.charts import Pie, Map, Page

# 圆环图数据
districts = ['开福区', '岳麓区', '天心区', '芙蓉区', '浏阳市', '长沙县', '雨花区']
user_counts = [100, 70, 68, 40, 50, 10, 30]

# 创建圆环图
pie = (
    Pie()
    .add(
        series_name="用户地域分布",
        data_pair=[(districts[i], user_counts[i]) for i in range(len(districts))],
        radius=["40%", "70%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="虎扑社区长沙市用户地域分布环形图（考生学号姓名）",
            pos_left="center",
            pos_top="5%",
        ),
        legend_opts=opts.LegendOpts(pos_right=10, pos_top=80, orient='vertical'),
    )
)

# 创建地图
map_data = [(districts[i], user_counts[i]) for i in range(len(districts))]
map_chart = (
    Map()
    .add("用户数量", map_data, "长沙")
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="虎扑长沙市用户地域分布图（考生学号姓名）", pos_left="center", pos_top="5%"
        ),
        visualmap_opts=opts.VisualMapOpts(max_=max(user_counts)),
    )
)

# 将图表放入同一个页面
page = Page(layout=Page.SimplePageLayout)
page.add(pie)
page.add(map_chart)

# 保存为 HTML 文件
page.render("user_distribution.html")