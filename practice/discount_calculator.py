#This program calculates discount amount based on purchase tier
#There are basically 3 tiers

while True:
    
    print("1. gold")
    print("2. silver")
    print("3. bronze")
    print("4. Exit")

    price = 5000
    gold = 0.2*price
    silver = 0.1*price
    bronze = 0.15*price

    choice = int(input("Choose your tier: "))

    if choice == 1:
        print(f"your discount amount is ${gold}")
    elif choice == 2:
        print(f"your discount amount is ${silver}")
    elif choice == 3:
        print(f"your discount amount is ${bronze}")
    elif choice == 4:
        print("Thank you for choosing to shop with us, See you next time")
    else:
        print("invalid selection")
        break