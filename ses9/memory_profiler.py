""" 
Python has a build in module called resource. 
This is a unix system only module. Luckily we are all on a 
unix based system when we use docker for python development.

Task:

Your job is, to write a decorator function 
that can messure the memory usage of any piece of code 
"""


from resource import *
import time

""" time.sleep(3)
print(getrusage(RUSAGE_SELF)) """

def memory_profiler(func):
    def wrapper(*args, **kwargs):
        print('Evaluating memory usage...')
        print(getrusage(RUSAGE_SELF))
        return func(*args, **kwargs)
    return wrapper

@memory_profiler
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
    

# resource for all resource fields: https://docs.python.org/3/library/resource.html#resource-usage