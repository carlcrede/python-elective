import time

""" Create a decorator function that slows down your code by 1 second for 
each step. Call this function slowdown()

For this you should use the ‘time’ module.

When you got the ‘slowdown code’ working on this recursive function, 
try to create a more (for you) normal function that does the 
countdown using a loop, and see what happens if you 
decorate that function with you slowdown() function. """


def slowdown(func):
    def wrapper(n):
        time.sleep(1)
        return func(n)
    return wrapper

@slowdown
def countdown(n):
     if not n:   # 0 is false, not false is true
         return n
     else:
         print(n, end=' ')
         return countdown(n-1) # call the same function with n as one less

@slowdown
def countdown_iter(n):
    for i in reversed(range(n+1)):
        print(i, end=' ')