import time
from functools import wraps
def count_time(fn):
    @wraps(fn)
    def inner():
        start=time.time()
        fn()
        end=time.time()
        return end-start
    return inner

@count_time
def func():
    lt = [i for i in range(1, 1 + 1000000,2)]
    for i in lt:
        print(i)
if __name__ == '__main__':
    print(func())