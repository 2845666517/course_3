import pandas as pd
from pyecharts.charts import Line,Bar,Pie,WordCloud
import pyecharts.options as opts
import numpy as np


def func(x):
    if str(x['价格']).isdigit():
        return int(x['价格'])
    else:
        return np.NAN

if __name__ == '__main__':
    # 1．读取附件，云南旅游数据.xlsx文件，pd查看数据集情况
    df=pd.read_excel('./云南旅游数据.xlsx')
    print(df.columns)

    # 2．pd查看数据值的分布
    # print(df)
    # 3．简单进行数据统计，获取价格的平均数
    df['价格'] = df.apply(func, axis=1)
    df1=df.dropna(how='any',axis=0)
    print(df1['价格'].mean())


    # 4．简单进行数据统计，获取出游人数的总数
    print(df['出游人数'].sum())

    # 5．对数据中的数值型数据使用pyecharts生成词云图，期望效果如下
    df2=df.groupby(by='景点名称')['点评数'].sum()
    word=(
        WordCloud()
        .add('',list(zip(df2.index.tolist(),df2.values.tolist())))
    )
    word.render('./2-5.html')


    # 6．根据服务保障列，可视化生成饼图，期望效果如下：
    df3 = df.groupby(by='服务保障')['景点名称'].count()
    pie = (
        Pie(init_opts=opts.InitOpts(width='1600px',height='800px',bg_color='yellow'))
        .add('',list(zip(df3.index.tolist(), df3.values.tolist())),center='50%,20%',radius='50%',
             label_opts=opts.LabelOpts(formatter='{b}:{d}%')
             )
        .set_colors(['#000000','#ff0000','brown','pink'])
    )
    pie.render('./2-6.html')













    # 7．统计目的地人数，可视化生成柱状图，期望效果如下：
    df4=df.groupby('供应商')['出游人数'].sum()
    bar=(
        Bar()
        .add_xaxis(df4.index.tolist())
        .add_yaxis('',df4.values.tolist())
        .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'),
                        visualmap_opts=opts.VisualMapOpts(is_show=True),
                         datazoom_opts=opts.DataZoomOpts(is_show=True),
                         toolbox_opts=opts.TooltipOpts(is_show=True),

                         )

    )
    bar.render('./2-7.html')

    # 8．根据出游人数，可视化生成折线图
    line = (
        Line()
        .add_xaxis(df4.index.tolist())
        .add_yaxis('', df4.values.tolist())
        .set_global_opts(title_opts=opts.TitleOpts(title='主标题', subtitle='副标题'),
                         visualmap_opts=opts.VisualMapOpts(is_show=True),
                         datazoom_opts=opts.DataZoomOpts(is_show=True),
                         toolbox_opts=opts.TooltipOpts(is_show=True))
    )
    line.render('./2-8.html')

    # 9．根据点评数以及评分，可视化生成多柱状图
    bar = (
        Bar()
        .add_xaxis(df.index.tolist())
        .add_yaxis('点评数', df['点评数'].tolist())
        .add_yaxis('评分', df['评分'].tolist())
        .set_global_opts(title_opts=opts.TitleOpts(title='主标题', subtitle='副标题'),
                         visualmap_opts=opts.VisualMapOpts(is_show=True),
                         datazoom_opts=opts.DataZoomOpts(is_show=True),
                         toolbox_opts=opts.TooltipOpts(is_show=True))

    )
    bar.render('./2-9.html')

    # 10．根据价格，出游人数，可视化生成多条折线图
    line1 = (
        Line()
        .add_xaxis(df.index.tolist())
        .add_yaxis('', df['价格'].tolist())
        .add_yaxis('', df['出游人数'].tolist())
    )
    line1.render('./2-10.html')
