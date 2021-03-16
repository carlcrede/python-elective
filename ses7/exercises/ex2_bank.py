import sys

class Bank:
    def __init__(self):
        self.__accounts = []

    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, accounts):
        # check if accounts is list or account object
        if isinstance(accounts, list):
            for account in accounts:
                if self.customer_has_account(account):
                    print('Customers can only have one account.')
                else: 
                    self.__accounts.append(account)

        elif isinstance(accounts, Account):
            if self.customer_has_account(accounts):
                print('Customers can only have one account.')
            else:
                self.__accounts.append(accounts)

        else:
            print('Invalid argument. Should be an account or a list of accounts.')

    def customer_has_account(self, account):
        return account in self.__accounts

    def __repr__(self):
        return f'{self.__dict__}'

class Account:
    def __init__(self, num, customer):
        self.num = num
        self.customer = customer

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num
    
    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self._customer = customer

    def __repr__(self):
        return f'{self.__dict__}'

class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age < 18:
            print('You need to be 18 to be a customer. Come back when you are old enough.')
            sys.exit()
        else:
            self.__age = age

    def __repr__(self):
        return f'{self.__dict__}'


b = Bank()
c1 = Customer('Carl', 25)
c2 = Customer('Sigrid', 22)
a1 = Account(7372, c1)
a2 = Account(5264, c2)
