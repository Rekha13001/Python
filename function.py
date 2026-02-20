# Features added
# - PIN authentication
# - Input validation (no crashes)
# - Transaction history

# ATM Simulation with Authentication and Transaction History
# atm_project.py

def authenticate():
    CORRECT_PIN = "1234"
    attempts = 3

    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ").strip()
        if pin == CORRECT_PIN:
            print("Login successful!\n")
            return True
        else:
            attempts -= 1
            print(f"Wrong PIN. Attempts left: {attempts}")

    print("Account locked. Try again later.")
    return False


def deposit(balance, history):
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount.")
            return balance
        balance += amount
        history.append(f"Deposited ₹{amount}")
        print("Amount deposited successfully!")
    except ValueError:
        print("Please enter a valid number.")
    return balance


def withdraw(balance, history):
    DAILY_LIMIT = 50000

    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > balance:
            print("Insufficient balance.")
        elif amount > DAILY_LIMIT:
            print("Daily withdraw limit exceeded.")
        else:
            balance -= amount
            history.append(f"Withdrawn ₹{amount}")
            print("Amount withdrawn successfully!")
    except ValueError:
        print("Please enter a valid number.")
    return balance


def check_balance(balance):
    print(f"Current Balance: ₹{balance}")


def show_history(history):
    if not history:
        print("No transactions yet.")
    else:
        print("\nTransaction History:")
        for tx in history:
            print("-", tx)


def atm_menu():
    balance = 100000.0
    history = []

    if not authenticate():
        return

    while True:
        print("\nATM Menu")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            balance = deposit(balance, history)
        elif choice == 2:
            balance = withdraw(balance, history)
        elif choice == 3:
            check_balance(balance)
        elif choice == 4:
            show_history(history)
        elif choice == 5:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    atm_menu()
