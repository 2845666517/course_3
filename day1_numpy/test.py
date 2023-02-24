import numpy as np

if __name__ == '__main__':
    arr=np.arange(10,18).reshape(2,4)
    arr2=np.ones((2,3))

    print(arr+arr2)