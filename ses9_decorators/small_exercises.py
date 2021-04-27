from datetime import datetime

""" Write a decorator that writes to a log file the time stamp 
of each time this function is called.

Change the log decorator to also printing the values 
of the argument together with the timestamp.

Print the result of the decorated function to the log file also.

Create a new function and call it printer(text) 
that takes a text as parameter and returns the text. 
Decorate it with your logfunction. Does it work? """

def log(func):
    def wrapper(*args):
        result = func(*args)
        with open('log.txt', 'a') as f:
            f.write(f'Timestamp: {datetime.now()}\nArgs: {args}\nResult: {result}\n\n')
        return result
    return wrapper

@log
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

@log
def printer(text):
    return f'From printer: {text}\n'

