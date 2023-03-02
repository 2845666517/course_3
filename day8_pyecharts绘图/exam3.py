import pandas as pd
from pyecharts.charts import Line,Bar,Pie,WordCloud

def func(x):
    money=x['薪资范围'].replace('k','').split('-')
    return (int(money[1])-int(money[0]))/2
def func1(x):
    return int(x['薪资范围'].replace('k','').split('-')[0])

def func2(x):
    return int(x['薪资范围'].replace('k','').split('-')[1])

if __name__ == '__main__':
    df=pd.read_csv('./job.csv')
    print(df.columns.tolist())
    # 1．获取所有行的数据
    # print(df)


    # 2．对python相关的岗位情况进行分析
    # 3．分析
    # 各个学历与薪资的关系，使用合适的组件可视化展示
    df['平均薪资']=df.apply(func,axis=1)
    df1=df.groupby(by='学历要求')['平均薪资'].sum()
    bar=Bar()
    bar.add_xaxis(df1.index.tolist())
    bar.add_yaxis('',df1.values.tolist())
    bar.render('./3_3.html')


    # 4．分析
    # 各种阶段的经验与薪资的关系，使用合适的组件可视化展示
    df2 = df.groupby(by='经验范围')['平均薪资'].sum()
    bar = Bar()
    bar.add_xaxis(df2.index.tolist())
    bar.add_yaxis('', df2.values.tolist())
    bar.render('./3_4.html')

    # 5．分析
    # 各个城市中薪资的平均值如何分布，使用合适的组件可视化展示
    df3 = df.groupby(by='城市名称')['平均薪资'].sum()
    bar = Bar()
    bar.add_xaxis(df3.index.tolist())
    bar.add_yaxis('', df3.values.tolist())
    bar.render('./3_5.html')

    # 6．分析
    # 北京市相同经验下本科学历与大专学历的薪资的占比情况，使用合适的组件可视化展示
    df4=df[(df['学历要求'].isin(['本科','大专'])) & (df['城市名称']=='北京')]
    df5=df4.groupby(by=['学历要求'])['平均薪资'].sum()
    bar = Bar()
    bar.add_xaxis(df5.index.tolist())
    bar.add_yaxis('', df5.values.tolist())
    bar.render('./3_6.html')

    # 7．分析
    # 每个城市的薪资的最大值与最小值的趋势变化，使用合适的组件可视化展示
    df['min'] = df.apply(func1, axis=1)
    df['max'] = df.apply(func2, axis=1)
    df7=df.groupby(by='城市名称').agg({'max':'max','min':'min'})
    line=Line()
    line.add_xaxis(df7.index.tolist())
    line.add_yaxis('max',df7['max'].tolist())
    line.add_yaxis('min',df7['min'].tolist())
    line.render('./3_7.html')
    print(df7)



    # 8．获取北京市所有公司的全称，使用合适的组件可视化展示
    df8=df.groupby(by='公司名称').count()
    word=WordCloud()
    word.add('',list(zip(df8.index.tolist(),df8.values.tolist())))
    word.render('./3_8.html')
