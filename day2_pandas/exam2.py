import pandas as pd
from sqlalchemy import create_engine

def add_sa(x):
    max_sa=int(x['薪资'].split('-')[0].replace('k',''))
    min_sa = int(x['薪资'].split('-')[1].replace('k', ''))
    return f'{(max_sa+min_sa)/2}k'

def add_ce(x):
    if x['经验范围']=='经验1-3年':
        x['经验类型']='初级开发'
    elif x['经验范围']=='经验3-5年':
        x['经验类型'] = '中级开发'
    else:
        x['经验类型'] = '高级开发'
    return f"{x['经验类型']}"

if __name__ == '__main__':
    # 1．读取附件中的lagou.json文件到df中
    df=pd.read_json('lagou.json')
    print(df)


    # 2．增加一个平均薪资列，为薪资范围的平均值
    df.loc[:,'平均薪资']=df.apply(add_sa,axis=1)
    print(df)


    # 3．增加一个经验类型列，如果经验为1-3年为初级开发，3-5年为中级开发，5年以上为高级开发
    df.loc[:,'经验类型']=df.apply(add_ce,axis=1)
    print(df)

    # 4．修改索引为4的数据，重新命名职位名称
    df.at[4,'职位名称']='web开发'
    print(df)


    # 5．删除经验范围列
    df1=df.drop('经验范围',axis=1)
    print(df1)

    # 6．删除经验在校，以及经验不限的数据
    df.drop(df[(df['经验范围']=='经验在校') | (df['经验范围']=='经验不限')].index,axis=0,inplace=True)
    print(df)

    # 7．将df写入到本地数据库mysql中，表自定义
    engine=create_engine('mysql+pymysql://root:root@127.0.0.1:3306/day2?charset=utf8')
    df.to_sql('table',con=engine,if_exists='replace')



    # 8．通过列表lt1 = ['python进阶', 'python数据分析', 'python基础', 'python数据采集']创建series结构数据se1
    lt1 = ['python进阶', 'python数据分析', 'python基础', 'python数据采集']
    se1=pd.Series(lt1)
    print(se1)
    # 9．通过列表lt2 = [['python进阶', '专高一'],['python数据分析', '专高三'], ['python基础', '专业四'], ['python数据采集', '专高四']]创建Dataframe结构数据df1
    lt2 = [['python进阶', '专高一'], ['python数据分析', '专高三'], ['python基础', '专业四'],['python数据采集', '专高四']]
    df1=pd.DataFrame(lt2)
    print(df1)


    # 10．获取df1中专高三的课程名称
    course=df1[0]
    print(course)
