import random
import sys


class ATM():
    def __init__(self, account_username, account_number, balance=0):
        self.account_username = account_username
        self.account_number = account_number
        self.balance = balance

    def account_details(self):
        print("***** Your account details ******")
        print(f"Your username: {self.account_username}")
        print(f"Your account number: {self.account_number}")
        print(f"Your balance: {self.balance}")

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.amount + self.balance
        print("Your new balance is:", self.balance)
        print()

    def withdrawal(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient funds! Please try again. ")
        else:
            self.balance = self.balance - self.amount
            print("Your new balance is:", self.balance)
        print()

    def check_balance(self):
        print("Your balance is:", self.balance)
        print()

    def transaction(self):
        print(""" ***** TRANSACTION STARTED, PLEASE SELECT FROM THE OPTIONS BELOW: ***** 
                        1. DEPOSIT 
                        2. WITHDRAWAL 
                        3. CHECK BALANCE 
                        4. SHOW ACCOUNT DETAILS 
                        5. EXIT""")
        while True:

            try:
                option = int(input("Select option 1, 2, 3, 4, or 5: "))
            except:
                print("Error: did not understand input. Please try again: ")
                continue
            else:
                if option == 1:
                    amount = int(input("How much would you like to deposit? "))
                    atm.deposit(amount)
                elif option == 2:
                    amount = int(input("How much would you like to withdrawal? "))
                    atm.withdrawal(amount)
                elif option == 3:
                    atm.check_balance()
                elif option == 4:
                    atm.account_details()
                elif option == 5:
                    print(f"""**** Printing receipt...*****
                            Transaction is now complete.
                            Transaction number: {random.randint(10000, 10000000)}
                            Account holder: {self.account_username.upper()}
                            Account number: {self.account_number}
                            Available balance: {self.balance}
                            Thank you for banking with us!""")
                    sys.exit()

print("""***** Welcome to the Bank of America! *****""")
print("Let's create your account! ")

account_username = input("Enter your name for the account: ")
account_number = int(input("Enter your account number: "))
print("Account created successfully!")

atm = ATM(account_username, account_number)

while True:
    trans = input("Would you like to start a transaction? (Enter 'y' for yes, 'n' for no): ")

    if trans == 'y':
        atm.transaction()
    elif trans == 'n':

        print("Thank you for banking with us! See you again soon!")
        break
    else:
        print("Error: did not understand response. Please enter 'y' or 'n'. ")
