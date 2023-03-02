import numpy as np
import pandas as pd
if __name__ == '__main__':
    # 请生成一个100-200的numpy数字序列一维数组，要求步长为5
    arr=np.arange(100,201,5)
    print(arr)

    # 请将给定python元组(3,5,8,9,11)转为numpy一维数组
    arr2=np.array((3,5,8,9,11))
    print(arr2)

    # 生成一个包含从31-90的整数的二维数组，数组必须为6行，10列
    arr3=np.arange(31,91).reshape(6,10)
    print(arr3)

    # 请将上一题中的二维数组，转为pandas的dataframe结构，列名使用自然数索引
    df=pd.DataFrame(arr3)
    print(df)

    # 生成一个值全部为1的numpy二维数组，数组必须为5行，5列
    arr4=np.ones(25,dtype=int).reshape(5,5)
    print(arr4)

    # 1.   读取矿产品数据.xlsx文件，进行适当的数据预处理
    # 2.   在k值2-9之间循环KMeans算法，并使用calinski_harabasz_score评分
    # 3.   用绘图法找到最佳k值
    # 4.   使用最佳k值实现位置矿产品聚类，并使用散点图绘制聚类结果
