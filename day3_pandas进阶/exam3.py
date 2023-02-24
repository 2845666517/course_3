import pandas as pd
from sqlalchemy import create_engine

engine=create_engine('mysql+pymysql://root:root@localhost:3306/day2?charset=utf8')

if __name__ == '__main__':
    # 读取hotel.xlsx文件，文件包含全国各城市酒店及价格数据
    df = pd.read_excel('hotel.xlsx')
    print(df)

    # 按beds的降序，和originalPrice的升序，对酒店数据进行排序操作
    df.sort_values(by=['beds','originalPrice'],ascending=[False,True],inplace=True)
    print(df)

    # 将cityName等于”北京“，tuanType列的数据修改为”四星级“
    df.loc[df['cityName']=='北京','tuanType']='四星级'
    print(df)

    # 筛选出所有cityName为”澳门“的数据, 保留cityName，originalPrice这两列
    df = df.loc[df['cityName'] == '澳门', ['cityName', 'originalPrice']]
    print(df)

    # 将上面的筛选结果写入html文件
    df.to_html('hotel.html')

    # 将上面的结果写入到本地的mysql中
    df.to_sql('hotel',con=engine,if_exists='replace')

