import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


if __name__ == '__main__':
    # 1．请利用matplotlib编写一个程序，显示y = x * x + 18
    # 这条抛物线
    # x=[i for i in range(10)]
    # y=[i**2+18 for i in x]
    # plt.plot(x,y)
    # plt.show()
    # 2．用df表示以下航班乘客变化分析内容
    df=pd.DataFrame(
        {'year':[1949,1949,1949,1949,1949],
         'month':['January','February','March','Apri','May'],
         'passengers':[112,118,132,129,121]}
    )


    # 3．利用matplotlib分析年度乘客总量变化情况（折线图）
    # df2=df.groupby(by='year')['passengers'].sum()
    # plt.plot(df2.index.tolist(),df2.values.tolist(),marker='s')
    # plt.show()

    # 4．利用matplotlib分析年度乘客总量变化情况（柱状图）
    df3=df.groupby(by='year')['passengers'].sum()
    plt.bar(df3.index.tolist(),df3.values.tolist())
    plt.savefig('1111.png')
    plt.show()


    # 5．利用matplotlib分析乘客在一年中各月份的分布（折线图）
    # df2 = df.groupby(by='month')['passengers'].sum()
    # plt.plot(df2.index.tolist(), df2.values.tolist(), marker='s')
    # plt.show()


    # 6．利用matplotlib分析乘客在一年中各月份的分布（柱状图）
    df3 = df.groupby(by=['month'])['passengers'].sum()
    plt.bar(df3.index.tolist(), df3.values.tolist())
    plt.show()

    # 7．利用seaborn分析年度乘客总量变化情况（折线图）
    # sns.lineplot(data=df, x='year', y='passengers')
    # plt.show()
    # print(df)

    # 8．利用seaborn分析年度乘客总量变化情况（柱状图）
    sns.barplot(x=df3.index.tolist(), y=df3.values.tolist())
    plt.show()

    # 9．利用seaborn分析乘客在一年中各月份的分布（折线图）
    sns.lineplot(data=df, x='month', y='passengers')
    plt.show()

    # 10．利用seaborn分析乘客在一年中各月份的分布（柱状图）
    sns.lineplot(x=df3.index.tolist(),y=df3.values.tolist())
    plt.show()
