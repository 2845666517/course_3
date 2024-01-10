import numpy as np
from collections import Counter
if __name__ == '__main__':
# 使用numpy的相关方法完成以下需求
# 1．创建数字从 0 到 9 的 1 维数组arr
    arr=np.arange(0,10)
    print(arr)
# 2．从 arr 中提取所有奇数
    arr1=arr[arr%2!=0]
    print(arr1)
# 3．将 arr 中的所有奇数替换成 -1
    arr[arr%2!=0]=-1
    print(arr)
# 4．将 arr  数组转换成 2 维数组arr2
    arr2=arr.reshape(2,5)
    print(arr2)
# 5．获取arr2的轴的数量
    zhou=np.ndim(arr2)
    print(zhou)
# 6．获取arr2的第1行第2列,
    num=arr2[1,2]
    print(num)
# 7．获取arr2的数组元素总个数
    arr_count=Counter(arr),
    print(arr_count)
# 8．获取arr2的元素类型,
    arr2_type=arr2.dtype
    print(arr2_type)
