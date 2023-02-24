import pandas as pd

def add_c(x):
    return x['Co']+x['No2']+x['So2']+x['O3']

def add_pm(x):
    if x['PM2.5']>5:
        x['pm2.5类型列']='重度污染'
    else:
        x['pm2.5类型列'] = '重度污染'

    return x['pm2.5类型列']


if __name__ == '__main__':
    # 1.读取附件中的北京空气质量指数.xlsx文件到df中
    df=pd.read_excel('北京空气质量指数.xlsx')
    print(df)

    # 2.增加一个统计列，co,no2,so2,o3的总和
    df['统计']=df.apply(add_c,axis=1)

    # 3.增加一个pm2.5类型列，如果最大值大于5，代表重度污染，小于等于5代表轻度污染
    df['pm2.5类型列'] = df.apply(add_pm, axis=1)
    print(df)

    # 4.修改万寿西宫的AQI指数数据，改为无
    df.loc[df['监测点']=='万寿西宫','AQI指数']='无'
    print(df)
    print('\n\n')


    # 5.将原有的列名，03，co修改为臭氧，一氧化碳
    df.rename(columns={'Co':'一氧化碳',  'No2':'No2','O3':'臭氧'},inplace=True)
    print(df)
    print('\n\n')

    # 6.删除昌平镇的数据
    df.drop(df[df['监测点']=='昌平镇'].index,inplace=True)
    print(df)


    # 7.将df写入到北京空气质量指数.html文件中
    df.to_html('北京空气质量指数.html')


    # 8.通过列表lt1 = ['列表', '字典', '字符串', '集合']创建series结构数据se1
    lt1 = ['列表', '字典', '字符串', '集合']
    se1=pd.Series(lt1)
    print(lt1)

    # 9.通过列表lt2 = [['列表', 'list'],['字典', 'dict'], ['字符串', 'str'], ['集合', 'set']]创建Dataframe结构数据df1
    lt2 = [['列表', 'list'], ['字典', 'dict'], ['字符串', 'str'], ['集合', 'set']]
    df1=pd.DataFrame(lt2)
    print(df1)


    df.to_json('test.json')

    # 10.判断df1中第1行第2列数据是否为list，是的话，返回答对了
    if df1.loc[0,1]=='list':
        print('答对了')
    else:
        print('答错了')
