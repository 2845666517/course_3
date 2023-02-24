import numpy as np
if __name__ == '__main__':
# 使用numpy完成以下需求
# 1．创建一个10*10的ndarray对象，且矩阵边界全为1，里面全为0
#     arr=np.ones(10*10).reshape(10,10)
#     arr[1:-1,1:-1]=0
#     print(arr)
# 2．创建所有 False的 2×2 NumPy 数组
#     arr2=np.array([False,False,False,False]).reshape(2,2)
#     print(arr2)

# 3．使用numpy获得2022年1月对应的所有日期
    days=np.arange('2022-01-01','2022-02-01',dtype='datetime64')
    print(days)


# 4．创建一个形态为 3x5 的 2 维数组，包含 1 和 10 之间的随机小数
    arr3=np.random.uniform(1,10,size=15).reshape(3,5)
    print(arr3)

# 5．创建全是1的3X3数组
    arr4=np.ones(9).reshape(3,3)
    print(arr4)

# 6．如何从数组np.array([1, 2, 0, 0, 4, 0])中找出非0元素的位置索引
    arr5=np.array([1, 2, 0, 0, 4, 0])
    index=np.where(arr5!=0)
    print(index)

# 7．创建一个5*3随机矩阵和一个3*2随机矩阵，求矩阵积
    arr5=np.random.random(15).reshape(5,3)
    arr6=np.random.random(6).reshape(3,2)
    ji=np.dot(arr5,arr6)
    print(ji)

# 8．使用numpy获取昨天、今天、明天的日期
    today=np.datetime64('today','D')
    print(today)
    tomorro=np.datetime64('today','D')+1
    print(tomorro)
    yestoday=np.datetime64('today','D')-1
    print(yestoday)
