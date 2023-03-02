import pandas as pd
from datetime import datetime

if __name__ == '__main__':
    # 1
    # 读取uservs.csv文件，生成dataframe数据集df1，对df1数据各字段进行缺失值处理；
    df1=pd.read_csv('./uservs.csv')
    print(df1)

    # 2
    # 对数据进行清洗，去掉”用户行为“字段不属于（”pv”, ”cart”, ”fav”, ”buy”)四种值的数据
    df1.drop(df1[-df1['用户行为'].isin(['pv', 'cart', 'fav', 'buy'])].index,inplace=True)

    # 3
    # 对总体用户行为转化率进行计算，计算pv->buy、pv->cart_fav、cart_fav->buy的转化率
    df2=df1.groupby(by='用户行为')['用户id'].count()
    print(df2)
    buy_pv=df2['buy']/df2['pv']
    cart_fav_pv=(df2['cart']+df2['fav'])/df2['pv']
    buy_cart_fav=df2['buy']/(df2['cart']+df2['fav'])
    print(buy_pv,cart_fav_pv,buy_cart_fav)





    # 4
    # 根据用户ID和用户行为字段进行计算，生成用户行为偏好表，计算各个用户的各自的pv->buy、pv->cart_fav、cart_fav->buy的转化率
    users=df1['用户id'].unique()
    dic={}

    for i in users:
        dfs=df1.loc[df1[df1['用户id']==i].index,:]
        df3=dfs.groupby(by='用户行为')['用户id'].count()
        buy_pv = df3.get('buy',0) / df3.get('pv',0) if  df3.get('pv',0) else 0
        cart_fav_pv = (df3.get('cart',0) + df3.get('fav',0)) / df3.get('pv',0) if df3.get('pv',0) else 0
        buy_cart_fav = df3.get('buy',0) / (df3.get('cart',0) + df3.get('fav',0)) if (df3.get('cart',0) + df3.get('fav',0)) else 0
        dic[i]={'buy_pv':buy_pv,'cart_fav_pv':cart_fav_pv,'buy_cart_fav':buy_cart_fav}

    print(dic)




    # 5
    # 计算用户FRM模型，因为无客户单价数据，因此计算R和F。R使用与2017年12月3日最近购买的一次时间差，
    # F为下单数；计算R和F的均值，R_mean和F_mean。按照R和F的实际值与均值比较，分别计算4种行为的用户数量
    # types=df1['用户行为'].unique()
    # for i in types:
    #     df4=df1.loc[df1[df1['用户行为']==i].index,:]
    #
    #     r=df4.groupby(by='用户id').agg({'时间戳':'max'}).reset_index()
    #     F = df4.groupby(by='用户id').agg({'商品id': 'count'}).reset_index()
    #
    #     r['R']=(pd.to_datetime(datetime(2017,12,3,23))-pd.to_datetime(df1['时间戳'],unit='s')).dt.days
    #     R=r[['用户id','R']]
    #     print('=============')
    #     print(R)
    #     print('1=============')
    #     RF=pd.merge(R,F,left_on='用户id',right_on='用户id',how='inner')
    #     RF.rename(columns={'商品id':'F'},inplace=True)
    #     RF['R_mean']=RF['R'].mean()
    #     RF['F_mean']=RF['F'].mean()
    #     print(RF)

    # order_df = df1[df1['用户行为'] == 'buy']
    # r = order_df.groupby(by='用户id').agg({'时间戳': 'max'}).reset_index()
    # F = order_df.groupby(by='用户id').agg({'商品id': 'count'}).reset_index()

    # r['R'] = (pd.to_datetime(datetime(2017, 12, 3, 23)) - pd.to_datetime(df1['时间戳'], unit='s')).dt.days
    # R = r[['用户id', 'R']]
    # RF = pd.merge(R, F, left_on='用户id', right_on='用户id', how='inner')
    # RF.rename(columns={'商品id': 'F'}, inplace=True)
    # RF['R_mean'] = RF['R'].mean()
    # RF['F_mean'] = RF['F'].mean()
    # print(RF)








    # 6
    # 用户活跃时段分析，选择某一个日期，计算此日期内每1小时用户浏览量、用户加入购物车量、用户购买量，并用折线图进行可视化


    # 7
    # 定义所有用户行为称之为uv， 计算每日uv, pv数据，并任意选取连续10个日期的数据进行可视化
    # 8
    # 用户留存率分析，计算3日留存率，计算方式：n日留存率 = n日后还登录的用户数 / 第一天新增总用户数
    # 9
    # 商品购买频次分析，计算购买1次、2
    # 次。。。10
    # 次的商品数量分布数据，进行可视化
    # 10
    # 商品类别偏好分析，计算不同类别下商品的总销量以及包含的商品数，按销量排序
