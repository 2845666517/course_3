import math

import numpy as np
from collections import Counter

if __name__ == '__main__':
# 4．有两个数组，x=np.array([436,556,607,899]),y=np.array([556,559,607,936,966]),请使用合适的方法获取两个数组的公共项
    x=np.array([436,556,607,899])
    y=np.array([556,559,607,936,966])
    arr6=np.intersect1d(x,y)
    print(arr6)




# 5．计算给定数组np.array([33,35,60,70,85])和np.array([44,51,65,73,80])之间的欧氏距离
#     arr7=np.array([33,35,60,70,85])
#     arr8=np.array([44,51,65,73,80])
#     res=np.sqrt(np.sum(np.square(arr8-arr7)))
#     print(res)


# 6．输入数字n，创建数字从 1 到 n 的 1 维数组arr，将 arr 中的所有奇数替换成 -1
#     arr4=np.arange(1,21)
#     arr4[arr4%2!=0]=-1
#     print(arr4)

# 7．给定数组[1, 2, 3, 4, 5]，获取到平均值，将平均值插入到每个元素直接得到新的数组
    arr = np.array([1, 2, 3, 4, 5])
    arr6=np.insert(arr, np.arange(1, len(arr)), arr.mean())
    print(arr6)
# 8．创建一个5*5的随机值数组，并找到最大值，并替换为0
#     arr5=np.random.randint(1,10,size=25).reshape(5,5)
#     print(arr5.max())
#     arr6=arr5[arr5==arr5.max()]=0
#     print(arr5)
