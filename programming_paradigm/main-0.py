import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command> <amount (optional)>")
        sys.exit(1)

    command = sys.argv[1].lower()

    # Create a bank account object
    account = BankAccount()

    # Handling different commands
    if command == "deposit":
        if len(sys.argv) == 3:
            try:
                amount = float(sys.argv[2])
                account.deposit(amount)  # Make sure this is the only place the method is called
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        else:
            print("Usage: python main-0.py deposit <amount>")
    
    elif command == "withdraw":
        if len(sys.argv) == 3:
            try:
                amount = float(sys.argv[2])
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        else:
            print("Usage: python main-0.py withdraw <amount>")
    
    elif command == "balance":
        account.display_balance()

    else:
        print(f"Unknown command: {command}")
        print("Available commands: deposit, withdraw, balance")

if __name__ == "__main__":
    main()
