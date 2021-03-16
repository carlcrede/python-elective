class P:
    def __init__(self, name, alias):
        self.name = name  # public access
        self.__alias = alias  # private access / can only be used within class

    def who(self):
        print('name : ', self.name)
        print('alias : ', self.__alias)

p = P('Carl', 'CCH')
print(p.name)
try:
    print(p.alias)  # wont work
except Exception as e:
    print('Error: ', e)

p.who() # works, because alias is ised within class