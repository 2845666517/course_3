import pandas as pd
from pyecharts.charts import Line,Bar,WordCloud

if __name__ == '__main__':
    # 1．用df表示以下内容，字段从左往右依次是幸存与否，
    # 仓位等级，性别，年龄，堂兄弟姐妹数，父母子女数，票价，上船港口缩写，
    # 仓位等级，人员分类，是否成年男性，所在甲板，上船港口，是否幸存，是否单独乘船
    dic={'survied':[0,1,1,1,0],
         'pclass':[3,1,3,1,3],
         'sex':['male','female','female','female','male'],
         'age':[22.0,38.0,26.0,35.0,35.0],
         'sibsp':[1,1,0,1,0],'parch':[0,0,0,0,0],
         'fare':[7.2500,71.2833,7.9250,53.1000,80.0500],
         'embark':['S','C','S','S','S'],
         'class':['Third','First','Third','First','Third'],
         'who':['man','woman','woman','woman','man'],
         'deck':['NaN','C','NaN','C','NaN'],
         'embark_town':['Southampton','Cherbourg','Southampton','Southampton','Southampton'],
         'alive':['no','yes','yes','yes','no'],
         'alone':['False','False','Ture','False','Ture']}
    df=pd.DataFrame(dic)
    print(df)
    # 2．请分析
    # 不同仓位等级中幸存和遇难的乘客比例，选择合适的组件可视化展示
    df2=df.groupby('survied')['who'].count()

    line=Line()
    line.add_xaxis(df2.index.tolist())
    line.add_yaxis('幸存与否', df2.values.tolist())
    line.render('./2_2.html')

    # 3．请分析
    # 不同性别的幸存比例，选择合适的组件可视化展示
    df2 = df.groupby('sex')['survied'].count()

    line = Line()
    line.add_xaxis(df2.index.tolist())
    line.add_yaxis('性别的幸存比例', df2.values.tolist())
    line.render('./2_3.html')

    # 4．请分析
    # 幸存和遇难乘客的票价分布，选择合适的组件可视化展示
    df2 = df.groupby(by=['survied'])['fare'].sum()

    line = Line()
    line.add_xaxis(df2.index.tolist())
    line.add_yaxis('性别的幸存比例', df2.values.tolist())
    line.render('./2_4.html')

    # 5．请分析
    # 幸存和遇难乘客的年龄分布，选择合适的组件可视化展示
    df2 = df.groupby(by=['age'])['survied'].count()
    bar = Bar()
    bar.add_xaxis(df2.index.tolist())
    bar.add_yaxis('遇难乘客的年龄分布', df2.values.tolist())
    bar.render('./2_5.html')

    # 6．请分析
    # 不同上船港口的乘客仓位等级分布，选择合适的组件可视化展示
    df2 = df.groupby(by=['embark_town'])['pclass'].count()
    print(df2)
    line = Line()
    line.add_xaxis(df2.index.tolist())
    line.add_yaxis('遇难乘客的年龄分布', df2.values.tolist())
    line.render('./2_6.html')


    # 7．请分析
    # 幸存和遇难乘客堂兄弟姐妹的数量分布，选择合适的组件可视化展示
    df2 = df.groupby(by=['sibsp'])['survied'].count()
    print(df2)
    line = Line()
    line.add_xaxis(df2.index.tolist())
    line.add_yaxis('遇难乘客的年龄分布', df2.values.tolist())
    line.render('./2_7.html')

    # 8．请分析
    # 幸存和遇难乘客父母子女的数量分布，选择合适的组件可视化展示
    df2 = df.groupby(by=['survied'])['pclass'].count()
    print(df2)
    line = Line()
    line.add_xaxis(df2.index.tolist())
    line.add_yaxis('遇难乘客的年龄分布', df2.values.tolist())
    line.render('./2_8.html')


    # 9．请分析
    # 单独乘船与否和幸存之间有没有联系，选择合适的组件可视化展示
    df2 = df.groupby(by=['alone'])['survied'].count()
    print(df2)
    line = Line()
    line.add_xaxis(df2.index.tolist())
    line.add_yaxis('遇难乘客的年龄分布', df2.values.tolist())
    line.render('./2_9.html')
