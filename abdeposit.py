from abc import ABC, abstractmethod

class Atm( ABC ):

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

class BankAccount(Atm):
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance !")

        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")

    def deposit(self, amount):
        self.balance +=amount
        print (f"{amount} deposited successfully.")

    def check_balance(self):
        print(f"current Balance : {self.balance}")

account = BankAccount()

account.deposit(1000)
account.check_balance

account.withdraw(700)
account.check_balance()

account.withdraw(300)
account.check_balance()
