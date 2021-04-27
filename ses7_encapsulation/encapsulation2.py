class P:
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x > 1000:
            self.__x = 1000
        elif x < 0:
            self.__x = 0
        else:
            self.__x = x

    def __str__(self): # informal tostring
        return f'{self.x}'

    def __repr__(self):  #  formal tostring
        return f'{self.__dict__}'

s="""
Hello
This
is
a
multi-line
comment
"""
print(s)
print('Multi-line comment without newlines: ', s.replace('\n', ' '))
