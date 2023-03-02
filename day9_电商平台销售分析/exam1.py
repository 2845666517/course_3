import pandas as pd
from pyecharts.charts import Bar,Line,Pie,WordCloud
from pyecharts import options as opts
if __name__ == '__main__':
    # 1．读取附件，train.csv文件，pd查看数据集情况
    df=pd.read_csv('./train.csv')
    print(df.columns)
    # 2．pd查看数据值的分布
    # print(df)

    # 3．根据Ticket列进行分组，获取年龄的平均数
    df1=df.groupby('Ticket')['Age'].mean()

    # 4．根据Embarked列进行分组，获取SibSp列的总数
    df2 = df.groupby('Embarked')['SibSp'].sum()

    # 5．对数据中的Ticket列数据使用pyecharts生成词云图
    df3 = df.groupby('Ticket')['PassengerId'].count()
    word=WordCloud()
    word.add('',list(zip(df3.index.tolist(),df3.values.tolist())))
    word.render('./1-5.html')

    # 6．根据Embarked列进行分组，获取性别的占比，可视化生成饼图
    df4 = df.groupby('Embarked')['Sex'].count()
    pie = Pie()
    pie.add('', list(zip(df4.index.tolist(), df4.values.tolist())))
    pie.render('./1-6.html')

    # 7．统计性别列，可视化生成柱状图
    df5=df.groupby(by='Sex')['PassengerId'].count()
    bar=(
        Bar()
        .add_xaxis(df5.index.tolist())
        .add_yaxis('',df5.values.tolist())
    )
    bar.render('./1-7.html')

    # 8．根据Ticket列进行分组，获取该数据中国年龄的最大值，可视化生成折线图
    df6=df.groupby('Ticket')['Age'].max()
    line=(
        Line()
        .add_xaxis(df6.index.tolist())
        .add_yaxis('',df6.values.tolist())
    )
    line.render('./1-8.html')
    # 9．根据SibSp以及Parch，可视化生成多柱状图

    bar = (
        Bar()
        .add_xaxis(df['PassengerId'].tolist())
        .add_yaxis('', df['SibSp'].tolist())
        .add_yaxis('', df['Parch'].tolist())
    )
    bar.render('./1-9.html')

    # 10．根据Fare，SibSp，可视化生成多条折线图
    line = (
        Line()
        .add_xaxis(df['PassengerId'].tolist())
        .add_yaxis('', df['Fare'].tolist())
        .add_yaxis('', df['SibSp'].tolist())
    )
    line.render('./1-10.html')