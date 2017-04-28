# decorator

import os
import functools
import time

# 不带参数的decorater

"""
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print ("call %s()"%func.__name__)
        return func(*args, **kw)
    return wrapper
"""

# 带参数的decorator
def log(text):
    #判断text是log的参数还是函数名,callable 为True说明是函数名，反之是log参数
    if callable(text):
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print ("call %s()"%text.__name__)
            return text(*args, **kw)
        return wrapper 
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print("%s: call %s"%(text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator

@log
def now():
    print("2016-11-19");

@log("Time")
def nowTime():
    print("time is %d"%(time.time()))

def f(farg, **kw):
	print("farg = %d"%(farg))
	for key in kw:
		print("kw key = %s, value = %s"%(key, kw[key]))

def main():
    f(1,arg2 = 'two',arg3 = 'three',arg4 = 4)
    now()
    nowTime()

if __name__ == "__main__":
    main()

