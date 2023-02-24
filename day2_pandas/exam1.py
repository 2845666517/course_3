import pandas as pd

def add_column(x):
    a=x['气温'].split('/')[0].replace('℃','')
    b = x['气温'].split('/')[1].replace('℃', '')
    return f'{int(a)-int(b)}℃'

def class_wen(x):
    max_ = int(x['气温'].split('/')[0].replace('℃', ''))
    if max_>20:
        return f'高温'
    else:
        return f'低温'


def update_w(x):
    if x['日期']=='2020年10月31日':
        x['天气状况']='晴'
    return x['天气状况']


if __name__ == '__main__':
    # 1．读取附件中的天津天气2020年10月.csv文件到df中
    df=pd.read_csv('天津天气2020年10月.csv')
    print(df)

    # 2．增加一个气温差值列，气温最大值和最小值的差值
    df.columns=df.loc[0]
    df.drop(index=0,inplace=True)
    df.loc[:,'气温差']=df.apply(add_column,axis=1)
    print(df)

    # 3．增加一个气温类型列，如果最大值大于20，代表高温，小于等于20代表低温
    df.loc[:,'气温类']=df.apply(class_wen,axis=1)
    print('\n\n')
    print(df)
    print('\n\n')


    # 4．修改2020年10月31日的数据，天气改为晴
    df['天气状况']=df.apply(update_w,axis=1)
    print(df)
    print('\n\n')

    # 5．将原有的列名，日期修改为date
    df.rename(columns={'日期':'date'},inplace=True)
    print(df)

    print(df[df['date']=='2020年10月1日'].index)

    # 6．删除2020年10月1日的数据
    df.drop(df[df['date']=='2020年10月1日'].index,inplace=True)
    print('\n\n')
    print(df)

    # 7．将df写入到天津天气2020年10月.html文件中
    df.to_html('天津天气2020年10月.html')

    # 8．通过列表lt1 = ['西游记', '水浒传', '三国演义', '红楼梦']
    # 创建series结构数据se1
    lt1 = ['西游记', '水浒传', '三国演义', '红楼梦']
    se1=pd.DataFrame(lt1)
    print(se1)

    # 9．通过列表lt2 = [['西游记', '吴承恩'],['水浒传', '施耐庵'], ['三国演义', '罗贯中'], ['红楼梦', '曹雪芹']]创建Dataframe结构数据df1
    lt2 = [['西游记', '吴承恩'], ['水浒传', '施耐庵'], ['三国演义', '罗贯中'], ['红楼梦', '曹雪芹']]
    df1 = pd.DataFrame(lt2)
    print(df1)


    # 10．获取df1中第1行第2列数据
    data1=df1.iat[0,1]
    print(data1)
