import time

balance = 5000


def ATM():
    currentBalance = balance
    while (True):
        print("""Welcome to The Bank
        Please enter one of the following choices:
        [C]heck balance
        [W]ithdraw
        [D]eposit
        [T]ransfer
        [E]xit """)

        choice = input("> ")

        if choice.upper() == "C":  # check balance
            check(currentBalance)

        elif choice.upper() == "W":  # withdraw
            while (True):
                cash = int(input("Enter the amount to withdraw or [0] to go back> "))
                if cash == 0:
                    break
                elif cash % 50 == 0:
                    if cash > 0:
                        currentBalance = withdraw(cash, currentBalance)
                        break
                    else:
                        print("Please enter an integer value")
                else:
                    print("You only can withdraw 50 SAR multiples.")

        elif (choice.upper() == "D"):  # deposit
            while (True):
                cash = int(input("Enter the amount to deposit or [0] to go back> "))
                if cash == 0:
                    break
                elif cash % 50 == 0:
                    currentBalance = deposit(cash, currentBalance)
                    break
                else:
                    print("Please only deposit 50 SAR  bills or higher.")
                    time.sleep(1)


        elif (choice.upper() == "T"):  # transfer
            cash = int(input("Enter the required amount to transfer> "))
            if cash <= currentBalance:
                transfer(cash, currentBalance)


        elif (choice.upper() == "E"):  # exiting
            print("Exiting...")
            time.sleep(1)
            print("Thank you for using The Bank.")
            time.sleep(2)
            break

        else:
            print("Incorrect Input.")
            time.sleep(1)


def check(currentBalance):
    print("Your account balance is", currentBalance, "SAR")
    time.sleep(1)
    return 0


def withdraw(cash, currentBalance):
    if (cash <= currentBalance):
        currentBalance -= cash
        print(f"Dispensing the amount {cash}")
        time.sleep(1)
        print(f"Remaining balance is: {currentBalance}")
        time.sleep(1)
    else:
        print("Insufficient funds!")
        time.sleep(1)
        print("Try another option or [E]ixt")
        time.sleep(1)
    return currentBalance


def deposit(cash, currentBalance):
    currentBalance += cash
    print(f"Depositing the amount {cash}")
    time.sleep(1)
    print(f"Current balance is: {currentBalance}")
    time.sleep(1)
    return currentBalance


def transfer(cash, currentBalance):
    while (True):
        account = input("Enter account number> ")
        if len(account) < 12 or len(account) > 12:
            print("Incorrect account number. The account number must be 12 numbers.")
        else:
            currentBalance -= cash
            print(f"The amount transferred is {cash}")
            time.sleep(1)
            print(f"Remaining balance is: {currentBalance}")
            time.sleep(1)
            break

    return currentBalance


ATM()
