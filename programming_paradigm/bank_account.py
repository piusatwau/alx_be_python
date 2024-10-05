class BankAccount:
    def __init__(self, initial_balance = 0):
        self.__account_balance = initial_balance
        
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
        print(f"Current balance: ${self.__account_balance:.2f}")

# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self.__account_balance = initial_balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__account_balance += amount
#             print(f"Deposited: ${amount}")  # Output only this line in the desired format
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.__account_balance:
#                 self.__account_balance -= amount
#                 print(f"You have successfully withdrawn ${amount}.")
#                 return True
#             else:
#                 print("Insufficient funds for this withdrawal.")
#                 return False
#         else:
#             print("Withdrawal amount must be positive.")
#             return False

#     def display_balance(self):
#         print(f"Current Balance: ${self.__account_balance}")
