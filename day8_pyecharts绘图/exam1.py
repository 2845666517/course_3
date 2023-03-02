import pandas as pd
from pyecharts.charts import Line,Bar,Pie,WordCloud,EffectScatter
from pyecharts import options as opts
if __name__ == '__main__':
    # 1．获取所有行的数据
    df=pd.read_json('./douban.json')
    print(df.columns)
    # 2．对豆瓣top250进行分析
    # 3．分析
    # 评分在9分以上所有电影的评论人数的占比情况，使用合适的组件可视化展示
    df1=df[df['电影评分']>9]
    df2=df.groupby(by='电影名称')['电影评论人数'].sum()
    pie=Pie()
    pie.add('评分在9分以上所有电影的评论人数的占比情况',list(zip(df2.index.tolist(),df2.values.tolist())))
    pie.render('./1_3.html')

    # 4．分析
    # 每个国家所有电影的评论人数的总和，使用合适的组件可视化展示
    df3=df.groupby(by='上映国家')['电影评论人数'].sum()
    pie = Pie()
    pie.add('每个国家所有电影的评论人数的总和', list(zip(df3.index.tolist(), df3.values.tolist())))
    pie.render('./1_4.html')

    # 5．分析
    # 中国大陆上映的电影的每部电影的评论人数与评分的关系，使用合适的组件可视化展示
    df4=df[df['上映国家'].str.contains('中国大陆')].groupby(by='电影评分')['电影评论人数'].sum()
    bar=Bar()
    bar.add_xaxis(df4.index.tolist())
    bar.add_yaxis('中国大陆上映的电影的每部电影的评论人数与评分的关系',df4.values.tolist())

    bar.render('./1_5.html')



    # 6．获取所有导演的资料，使用合适的组件可视化展示
    df5=df.groupby(by='电影导演')['电影名称'].count()
    word=WordCloud()
    word.add('导演的资料',list(zip(df5.index.tolist(),df5.values.tolist())))
    word.render('./1_6.html')

    # 7．分析
    # 1994
    # 年以后上映的电影排名与评分的关系，使用合适的组件可视化展示
    df6=df[df['上映时间']>1994].groupby(by='排名')['电影评分'].sum()
    line=Line()
    line.add_xaxis(df6.index.tolist())
    line.add_yaxis('',df6.values.tolist())
    line.set_colors('red')
    line.set_global_opts(
        title_opts=opts.TitleOpts(title='主题周',subtitle='主题日')
    )
    line.render('./3_7.html')

    # 8．分析
    # 每个导演导演电影的次数之间的关系，使用合适的组件可视化展示
    df8 = df.groupby(by='电影导演')['电影名称'].count()
    print(df8)
    bar = Bar()
    bar.add_xaxis(df8.index.tolist())
    bar.add_yaxis('导演导演电影的次数之间的关系', df8.values.tolist())

    bar.render('./1_8.html')
