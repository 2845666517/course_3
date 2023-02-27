import pandas as pd
import PIL


if __name__ == '__main__':
    # （二）使用适当的python库进行综合数据分析，代码保存为week2.py：
    # # 11.读取diamonds.csv生成数据集df，对数据集的数据质量进行评价
    df=pd.read_csv('./diamonds.csv')
    print(df,'\n\n')

    # # 12.对数据集中符合连续型数据的字段进行统计性描述
    print(df.describe())

    # # 13.根据cut字段计算每一个等级（clarity字段）钻石的数量
    df2=df.groupby(by='clarity').count()
    print(df2)

    # # 14.根据color字段进行分组，统计carat字段最大值、最小值、均值
    print('=================')
    df3=df.groupby(by='color').agg({'carat': ['max', 'min', 'mean']})
    print(df3)

    # # 15.先按字段color、再按字段cut分组，计算carat字段的总和
    df4=df.groupby(by=['color','cut'])['carat'].sum()
    print('======================')
    print(df4)


    # # 16.筛选carat字段值大于3.5的数据，生成新的数据集，保存为excel文件
    df5=df.loc[df[df['carat']>3.5].index]
    print(df5)


    # # 17.根据price字段值进行处理，生成一个新列level，price大于等于2000时，level值设置为1，否则设置为0
    df.loc[:,'level']=df.apply(lambda x: 1 if x['price']>=2000 else 0,axis=1)
    print(df)

    # # 18.对第17题的数据，筛选carat字段值大于3.2、level字段值为1的数据，保存到excel文件
    df.loc[df[(df['carat']>3.2) & (df['level'])==1].index,:].to_excel('./18.xlsx')

    # # 19.对df数据集按照carat、price字段进行升序排序，保存到excel文件
    df.sort_values(by=['carat','price']).to_excel('./19.xlsx')

    # 20.删除字段x,y,z，生成新的数据集，保存到excel文件
    df.drop(['x','y','z'],axis=1,inplace=True)
    print(df)
    