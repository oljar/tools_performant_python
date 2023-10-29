from functools import wraps
import time

def decor(func):
    @wraps(func)
    def inner(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        stop = time.time()
        print (f'time decor{start-stop} ')
        return result
    return inner

