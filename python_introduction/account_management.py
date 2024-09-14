# This simple python prgram helps one manage their bank account on ATM
'''
person walks to atm machine
selects option button
list of options is displayed 
    1. check account balance
    2. deposit money
    3. withdraw money
    4. print a mini bank statement
    5. exit
person can check any security concerns with their bank account


PLAN
we need account balance variable
starts with 0
when money is deposited it increases by deposit amout i.e deposit amount plus the previous balance
when money is withdrawn, account balance decreases i.e initial minus the value entered for withdraw


'''

residual_balance = 0

print("1. Check account balance")
print("2. Deposit money")
print("3. Withdraw money")
print("4. Print mini bank statemen")
print("5. Exit")

option = input(print("Select option to continue: "))
if option == "1":
    print(f"Your account balance is ${residual_balance}")


