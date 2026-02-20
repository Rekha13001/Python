balance = 100000.0

while True:
    print("\nATM Menu: ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    action = input("Enter action : ").strip() #strip() removes leading and trailing whitespace from starting and ending of the string

    if action == "1":
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount! Try again.")
            continue
        balance += amount
        print("Amount deposited successfully!")

    elif action == "2":
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds!")
        else:
            balance -= amount
            print("Amount withdrawn successfully!")

    elif action == "3":
        print("Your current balance is :", balance)

    elif action == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid action. Please try again.")
