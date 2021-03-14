"""
Create a Bank, an Account, and a Customer class.

All classes should be in a single file.

The bank class should be able to hold many account.

You should be able to add new accounts.

The Account class should have relevant details.

The Customer class Should also have relevant details.

Stick to the techniques we have covered so far.

Add the abillity for your __init__ method to handle different inputs (parameters).

"""


class Bank:

    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

class Account:
    def __init__(self, num, customer):
        self.num = num
        self.customer = customer

class Customer:
    def __init__(self, name):
        self.name = name

    

