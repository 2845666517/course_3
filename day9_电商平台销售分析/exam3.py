import pandas as pd
from pyecharts.charts import Line, Bar, Pie, WordCloud
import pyecharts.options as opts

if __name__ == '__main__':
    df = pd.DataFrame({
        '采购小组': ['冰鲜类', '活鲜类', '国产一组', '国产二组', '进口鲜果', '猪肉',
                     '熟食调理组', '禽类副件组', '粉面丸类组', '肉蛋包点组', '叶菜结球组',
                     '根茎调味组', '瓜果组', '菌菇组'],
        '销售金额': [147, 124, 103, 108, 126, 187, 197, 157, 120, 104, 130, 146,
                     126, 129],
        '销售数量': [50, 48, 28, 43, 27, 40, 25, 26, 19, 49, 16, 23, 40, 20],
    })
    # 2．pd查看数据值的分布
    print(df)
    # 3．简单数据统计，获取销售金额的平均值
    print(df['销售金额'].mean())
    # 4．简单数据统计，获取销售数量的总和
    print(df['销售数量'].sum())
    # 5．对数据中的采购小组列数据使用pyecharts生成词云图
    word = (
        WordCloud()
        .add('', list(zip(df['采购小组'], df['销售数量'])))
    )
    word.render('./3-5.html')

    # 6．根据采购小组列，获取销售金额，可视化生成柱状图
    bar = (
        Bar()
        .add_xaxis(df['采购小组'].tolist())
        .add_yaxis('', df['销售金额'].tolist())
    )
    bar.render('./3-6.html')
    # 7．根据采购小组列，获取销售金额以及销售数量，可视化生成柱状图
    bar = (
        Bar()
        .add_xaxis(df['采购小组'].tolist())
        .add_yaxis('销售金额', df['销售金额'].tolist())
        .add_yaxis('销售数量', df['销售数量'].tolist(), is_selected=False)
    )
    bar.render('./3-7.html')

    # 8．将上述7中的改动一下，只展示销售金额

    # 9．根据采购小组列，获取销售金额，可视化生成饼图
    pie=(
        Pie()
        .add('',list(zip(df['采购小组'], df['销售金额'])))
    )
    pie.render('./3-9.html')
    # 10．根据采购小组，获取销售金额，销售数量，可视化生成多条折线图
    line=(
        Line()
        .add_xaxis(df['采购小组'].tolist())
        .add_yaxis('',df['销售金额'].tolist())
        .add_yaxis('', df['销售数量'].tolist())
    )
    line.render('./3-10.html')