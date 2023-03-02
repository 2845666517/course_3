import pandas as pd
from pyecharts.charts import Line,Bar,Pie,WordCloud

if __name__ == '__main__':
    # 1．读取附件tips.csv，用df表示以下内容，字段从左往右依次是总消费，小费，性别，吸烟与否，就餐星期，就餐时间，就餐人数
    df=pd.read_csv('./tips.csv')
    print(df)

    # 2．请分析
    # 小费和总消费之间的关系，选择合适的组件可视化展示
    x=df['tip'].tolist()
    y=df['total_bill'].tolist()
    bar=Bar()
    bar.add_xaxis(x)
    bar.add_yaxis('消费关系',y)
    bar.render('./1_2.html')

    # 3．请分析
    # 男性顾客和女性顾客，谁更慷慨，选择合适的组件可视化展示
    df1=df.groupby('sex')['tip'].sum()
    x = df1.index.tolist()
    y = df1.values.tolist()
    bar = Bar()
    bar.add_xaxis(x)
    bar.add_yaxis('慷慨', y)
    bar.render('./1_3.html')


    # 4．请分析
    # 抽烟与否是否会对小费金额产生影响，选择合适的组件可视化展示
    df2=df.groupby(by='smoker')['tip'].sum()
    line=Line()
    line.add_xaxis(df2.index.tolist())
    line.add_yaxis('', df2.values.tolist())
    line.render('./1_4.html')


    # 5．请分析
    # 工作日，什么时候顾客给的小费更慷慨，选择合适的组件可视化展示
    df3=df[-df['day'].isin(['Sun','Sat'])].reset_index()
    df4=df3.groupby(by='day')['tip'].sum()
    x=df4.index.tolist()
    y=df4.values.tolist()
    bar=Bar()
    bar.add_xaxis(x)
    bar.add_yaxis('',y)
    bar.render('./1_5.html')


    # 6．请分析
    # 午饭和晚饭，哪一顿顾客更愿意给小费，选择合适的组件可视化展示
    df5=df.groupby(by=['time'])['tip'].count()
    x = df5.index.tolist()
    y = df5.values.tolist()
    bar = Bar()
    bar.add_xaxis(x)
    bar.add_yaxis('', y)
    bar.render('./1_6.html')

    # 7．请分析
    # 就餐人数是否会对慷慨度产生影响，选择合适的组件可视化展示
    df6=df.groupby(by=['size'])['tip'].sum()
    x = df6.index.tolist()
    y = df6.values.tolist()
    bar = Bar()
    bar.add_xaxis(x)
    bar.add_yaxis('', y)
    bar.render('./1_7.html')


    # 8．请分析
    # 性别 + 抽烟的组合因素对慷慨度的影响，选择合适的组件可视化展示
    df7=df.groupby(by=['sex','smoker'])['tip'].sum()
    x = df7.index.tolist()
    y = df7.values.tolist()
    bar = Bar()
    bar.add_xaxis(x)
    bar.add_yaxis('', y)
    bar.render('./1_8.html')

    # 9．请分析
    # 周末，什么时候顾客给的小费更慷慨，选择合适的组件可视化展示
    df3 = df[df['day'].isin(['Sun', 'Sat'])].reset_index()
    df4 = df3.groupby(by='time')['tip'].sum()
    x = df4.index.tolist()
    y = df4.values.tolist()
    bar = Bar()
    bar.add_xaxis(x)
    bar.add_yaxis('', y)
    bar.render('./1_9.html')
