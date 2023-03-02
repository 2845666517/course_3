import pandas as pd
import numpy as np

if __name__ == '__main__':
    # 输入数字n，创建数字从 1 到 n 的 1 维数组arr，将 arr 中的所有奇数替换成 -1
    n=input('输入n:')
    arr=np.arange(1,int(n)+1)
    arr[arr%2!=0]=-1
    print(arr)


    # 给定数组[1, 2, 3, 4, 5]，获取到平均值，将平均值插入到每个元素直接得到新的数组
    np1=np.array([1, 2, 3, 4, 5])
    np2=np.insert(np1,np.arange(1,len(np1)),np1.mean())
    print(np2)
    # 创建一个5*5的随机值数组，并找到最大值，并替换为0
    arr2=np.random.random(25).reshape(5,5)
    arr2[arr2==np.max(arr2)]=0
    print(arr2)
    # 使用numpy获取昨天、今天、明天的日期
    today=np.datetime64('today')
    yesterday=np.datetime64('today')-1
    tomorro = np.datetime64('today') + 1
    print(tomorro,today,yesterday)

    # 创建一个5*3随机矩阵和一个3*2随机矩阵，求矩阵积
    arr3=np.random.randint(1,10,size=15).reshape(5,3)
    arr4 = np.random.randint(1, 10, size=6).reshape(3, 2)
    ji=np.dot(arr3,arr4)
    print(ji)


    # 对附件中数据集testSet.txt进行聚类
    # a)  导入必要的库
    # b)  通过迭代寻找k个类簇的一种划分方案，使得用这k个类簇的均值来代表相应各类样本时所得的总体误差最小
    # c)  重复下面过程直到收敛
    # d)  用测试数据及测试kmeans算法，获取分类结果