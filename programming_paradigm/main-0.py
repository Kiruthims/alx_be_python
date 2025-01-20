import sys
from bank_account import BankAccount

def main():
    # Initialize the bank account with a default balance
    account = BankAccount(100)  # Example starting balance


    if len(sys.argv) < 2:
        print("Usage: python3 main-0.py <command>:<amount>")
        print("Commands: deposit:<amount>, withdraw:<amount>, display")
        sys.exit(1)


    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Handle the different commands
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command or missing amount.")

if __name__ == "__main__":
    main()


