from abc import ABC, abstractmethod class
Bank(ABC):

    @abstractmethod
    def DepositAmount(self, amount):
        pass
    @abstractmethod
    def WithdrawAmount(self, amount):
        pass
    @abstractmethod
    def show_balance(self):
        pass
    
class BankAccount(Bank):

    def __init__(self, name, mobile, balance):
        self.name = name
        self.mobile = mobile
        self.balance = balance
 
    def DepositAmount(self, amount):
        self.balance += amount
        print(amount," deposited successfully")

    def WithdrawAmount(self,amount):
        if amount <= self.___balance:
            self.__balance -= amount
            print(amount," debited successfully from your account")
        else:
            print("Insufficient Balance!!!")

    def show_balance(self):
        print("Current balance: ",self.	balance)

name = str(input("Enter your name: "))
mobile = int(input("Enter your mobile number: "))
balance = int(input("Enter your balance: "))

account = BankAccount(name, mobile, balance)

while True:
    print("\nMENU")
    print("1. Deposit money")
    print("2. Withdraw Money")
    print("3. Show balance")
    print("4. Exit")

    ch = int(input("Enter the choice you want to perform: "))
 
    if ch == 1:
        amount = int(input("\nEnter the amount you want to deposit:"))

        account.DepositAmount(amount) account.show_balance()
    elif ch == 2:
 
        amount = int(input("\nEnter the amount you want to withdraw: "))

        account.WithdrawAmount(amount) account.show_balance()
    elif ch == 3:
        account.show_balance()
    elif ch == 4:
        print("GOODBYE!!")
        break
    else:
        print("INVALID CHOICE!!!!!ENTER THE CORRECT OPTION!!")
