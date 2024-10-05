class BankAccount:
    def __init__(self, intitial_balance = 0):
        self.__account_balance = intitial_balance
        
    def deposit(self, amount):
        self.__account_balance += amount
        
    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
            # print(f"You have succesfully withdrawn {amount}, your account balance is {account_balance}")
        else:
            return False
    def display_balance(self):
        print(f"Your account balance is ${self.__account_balance}")
