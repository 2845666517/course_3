import time
import numpy as np
import pandas as pd
from pyecharts.charts import Line,Bar,Pie
from functools import wraps

def outer(fn):
    @wraps(fn)
    def inner():
        start=time.time()
        fn()
        print(time.time()-start)
    return inner
@outer
def fun1():
    lt = [i for i in range(0, 10000001,2)]
    return lt


@outer
def fun2():
    np1=np.arange(0,10000001,2)
    return np1.tolist()

@outer
def fun3():
    lt=list(range(1,1000001))
    lt2=filter(lambda x: x%2==0,lt)
    return lt2

if __name__ == '__main__':
    fun1()
    fun2()
    fun3()
    lt=[1,2,3,4,5]