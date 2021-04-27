import time as t


""" Your job is, to write a decorator function that can time any piece of code. """

""" start = time.time()
with open('log.txt', 'a') as f:
    for i in range(10000):
        f.write(str(i))

end = time.time()
print(end - start) """

def time(func):
    def wrapper(*args, **kwargs):
        start = t.time()
        value = func(*args, **kwargs)
        end = t.time()
        print(f'Time to execute function: {end - start}')
        return value
    return wrapper

@time
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
    


