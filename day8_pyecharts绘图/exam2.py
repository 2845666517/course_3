import pandas as pd
from pyecharts.charts import Line,Bar,Pie
if __name__ == '__main__':
    # 1．获取所有行的数据
    # 2．对上市公司的数据进行分析
    df = pd.read_json('./stock.json')
    print(df.columns)


    # 3．分析 # 上海市所有公司员工人数的情况，使用合适的组件可视化展示
    df1=df[df['市']=='上海市'].groupby(by='公司全称')['员工人数'].sum()
    bar=Bar()
    bar.add_xaxis(df1.index.tolist())
    bar.add_yaxis('',df1.values.tolist())
    bar.render('./2_3.html')

    df['注册资金(万元)']=df.apply(lambda x: float(x['注册资金(万元)'].replace(',','')),axis=1)
    # 4．分析
    # 每个省的注册资金最多的公司详情，使用合适的组件可视化展示
    df2=df.groupby(by=['省'])['注册资金(万元)'].max()
    bar=Bar()
    bar.add_xaxis(df2.index.tolist())
    bar.add_yaxis('',df2.values.tolist())
    bar.render('./2_4.html')

    # 5．分析
    # 随着上市日期的递进，注册资金与之的关系，使用合适的组件可视化展示
    df.sort_values(by=['上市日期'],inplace=True)
    df3=df.groupby(by='上市日期')['注册资金(万元)'].sum()
    bar = Bar()
    bar.add_xaxis(df3.index.tolist())
    bar.add_yaxis('', df3.values.tolist())
    bar.render('./2_5.html')

    # 6．分析
    # 各个身份以及各个市级，注册资金与员工人数的关系，使用合适的组件可视化展示
    df4=df.groupby(by=['省','市','员工人数'])['注册资金(万元)'].sum()
    print(df4.values.tolist())
    print(df4)
    bar = Bar()
    bar.add_xaxis(df4.index.tolist())
    bar.add_yaxis('', df4.values.tolist())
    bar.render('./2_6.html')

    # 7．分析
    # 北京市，上海市，深圳市的上市公司的注册资金的占比情况，使用合适的组件可视化展示
    df7=df.loc[df[df['市'].isin(['北京市','上海市','深圳市'])].index,:]
    df7=df7.groupby(by='市')['注册资金(万元)'].sum()
    pie=Pie()
    pie.add('北京市，上海市，深圳市的上市公司的注册资金的占比情况',list(zip(df7.index.tolist(),df7.values.tolist())))
    pie.render('./2_7.html')

    # 8．分析
    # 随着成立日期的递进，员工人数与之的关系，使用合适的组件可视化展示
    df.sort_values(by=['成立日期'], inplace=True)
    df8=df.groupby(by='成立日期')['员工人数'].sum()
    line=Line()
    line.add_xaxis(df8.index.tolist())
    line.add_yaxis('成立日期的递进，员工人数与之的关系',df8.values.tolist())

    line.render('./2_8.html')
