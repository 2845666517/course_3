import numpy as np
import pandas as pd
if __name__ == '__main__':
    # 请生成一个从10-20的一维数组，数组元素只能包含偶数
    arr=np.arange(10,21,2)
    print(arr)

    # 请将给定的数组np.array([100,103,106,108,112,116,118,136,138,139])中的奇数批量替换为33
    arr2=np.array([100,103,106,108,112,116,118,136,138,139])
    arr2[arr2 %2!=0]=33

    # 请生成一个从201-300的一维数组，并将这个一维数组转化为10行10列的二维数组
    arr3=np.arange(201,301).reshape(10,10)
    print(arr3)

    # 有两个数组，x=np.array([436,556,607,899]),y=np.array([556,559,607,936,966]),请使用合适的方法获取两个数组的公共项
    # 计算给定数组np.array([33,35,60,70,85])和np.array([44,51,65,73,80])之间的欧氏距离
    x = np.array([436, 556, 607, 899])
    y = np.array([556, 559, 607, 936, 966])
    same=np.intersect1d(x,y)
    print(same)

    # 1 读取图像聚类.xlsx数据，并转为Dataframe
    # 2 定义分数空列表与K值的取值范围(2-9)
    # 3 使用循环交叉验证的方式，遍历K，每次遍历都要求用KMeans算法训练、预测，并使用calinski_harabasz_score库对预测结果进行评价，将评价循环写入到上一题定义的分数空列表中
    # 4 使用matplotlib绘图法的plot方法，找到最高的分数所对应的K值，并最终确认K值"""