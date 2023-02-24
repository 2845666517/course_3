import numpy as np
import pandas as pd
if __name__ == '__main__':
    # （一）使用numpy和pandas三方库等，实现以下要求，代码放在week1.py文件中：
    # 1.使用["cat","dog","deer","fish","monkey"]生成一个numpy数组
    np01=np.array(["cat","dog","deer","fish","monkey"])
    print(np01,'\n')

    # 2.生成一个元素值全为5、长度为20的一维数组
    np02=np.ones(20,dtype=int)
    np02[:]=5
    print(np02)

    # 3.对第2题中的一维数组增加一维，形成形状为(20，1）的数组
    np03=np02.reshape(20,1)
    print(np03)

    # 4.生成一个形状为（3，3，3）、元素值依次为1-27的三维数组
    np04=np.arange(27).reshape(3,3,3)
    print(np04)
    print('\n')
    # 5.选取第4题中的数组的第0-2行、1-2列，打印筛选后的值
    np05=np04[0:2,:,1:]
    print(np05)

    # 6.使用[["li",80,70,100],["yang",70,80,99],["zhang",60,70,100]]
    # 数据初始化一个pandas的dataframe数据集，列名依次为["uid","en","cn","ma"]
    df1=pd.DataFrame(data=[["li",80,70,100],["yang",70,80,99],["zhang",60,70,100]],columns=["uid","en","cn","ma"])
    print(df1)

    # 7.使用[["li",80,70,100],["yang",70,80,99],["zhang",60,70,100]]
    # 数据初始化一个pandas的dataframe数据集，列名依次为["uid","en","cn","ma"]， 初始化方法不能与第6题使用的方法相同
    print('=======================')
    lt1=[["li",80,70,100],["yang",70,80,99],["zhang",60,70,100]]
    new_lt1=list(zip(*lt1))
    lt2=["uid","en","cn","ma"]
    dic={lt2[i]:new_lt1[i] for i in range(len(lt2))}
    # print(dic)
    df2=pd.DataFrame(dic)


    # 8.使用 {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat',
    # 'snake', 'cat', 'dog', 'dog'], 'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5,
    # np.nan, 7, 3]} 作为数据，使用 ['a', 'b', 'c', 'd', 'e', 'f', 'g',
    # 'h', 'i', 'j']作为索引初始化一个dataframe数据集
    df3=pd.DataFrame(data={'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat',
    'snake', 'cat', 'dog', 'dog'], 'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5,
    np.nan, 7, 3]},index=['a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j'])
    print(df3)

    # 9.对第8题中的数据集的age字段值按照均值进行空值填充处理
    df3.fillna(value=int(df3['age'].mean()),inplace=True)
    print(df3)

    # 10.对第9题中处理后的数据集按照age字段进行降序排序，打印排序后结果
    df3.sort_values(by=['age'],ascending=False,inplace=True)
    print('========================')
    print(df3)


