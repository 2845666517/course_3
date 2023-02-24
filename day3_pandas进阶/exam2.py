import pandas as pd
from sqlalchemy import create_engine


engine=create_engine('mysql+pymysql://root:root@localhost:3306/day2?charset=utf8')

if __name__ == '__main__':
    # 读取附件中电子病历.xlsx文件
    df=pd.read_excel('电子病历.xlsx')
    print(df,'\n\n')

    # 判断文件是否有缺失值并过滤掉该记录即可
    df.drop(df[df.isnull().any(axis=1) == True].index, inplace=True, axis=0)
    print(df)

    # 按”等级要求“的降序，和”分值“的升序，对电子病历进行排序
    df.sort_values(by=['等级要求','分值'],ascending=[False,True],inplace=True)
    print(df)

    # 将上面整理后df，重新写入到电子病历.json文件中
    df.to_json('电子病历.json')

    # 将上面整理后df，写入到本地的mysql数据库中
    df.to_sql('电子病历',con=engine,if_exists='replace')

