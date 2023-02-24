import pandas as pd

if __name__ == '__main__':
    # 1．读取附件中的北京空气质量指数.csv文件到df中
    df=pd.read_csv('北京空气质量指数.csv')
    print(df)


    # 2．判断文件中是否有缺失值
    print(df.isnull())

    # 3．过滤掉全为缺失值的那一行
    df1=df.drop(df[df.isnull().any(axis=1) == True].index)
    print(df1)

    # 4．进行数据清洗动作
    df.drop(df[df.isnull().any(axis=1) == True].index,inplace=True)
    print(df)

    # 5．分别按PM10，PM2
    # .5
    # 两列进行排序
    df.sort_values(by=['PM10','PM2.5'],ascending=[True,True])

    # 6．将排序后的df，原有的列名Co，No2，So2，O3修改为一氧化碳，二氧化氮，二氧化硫，臭氧
    df.rename(columns={'Co':'一氧化碳','No2':'二氧化氮','So2':'二氧化硫','O3':'臭氧'},inplace=True)
    print(df)

    # 7．将上面整理后df，重新写入到北京空气质量指数.json文件中
    df.to_json('./北京空气质量指数.json')

    # 8．将上述的df写入到本地的html文件，通过浏览器展示
    df.to_html('./北京空气质量指数.html')
