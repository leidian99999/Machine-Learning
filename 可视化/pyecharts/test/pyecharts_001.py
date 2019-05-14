from pyecharts import Bar

#定义标题
bar = Bar("我的第一个图表", "这里是副标题")

#使用主题
bar.use_theme('dark') #默认dark

#主要方法，用于添加图表的数据和设置各种配置项
bar.add("服装",
        ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
        [5, 20, 36, 10, 75, 90],
        is_more_utils=True)

#打印输出图表的所有配置项
#bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用

'''
默认将会在根目录下生成一个 render.html 的文件，
支持 path 参数，设置文件保存位置，如 render(r"e:\my_first_chart.html")，文件用浏览器打开。
'''
bar.render()    # 生成本地 HTML 文件

