class Bank:
    def __init__(self,name):
        self.name=name
        self.__accounts=[]
        print(f"Welcome to {self.name}")
    def showAccounts(self):
        for x in self.__accounts:
            print(f"Showing accounts {x}")
    def openAccount(self,name,number,atype):
        print("Ready to open an account")
        self.name=input("Account name: ")
        self.number=input("Account number: ")
        self.atype=input("Account type (savings or checking): ")
        print("Account created")
        print(f"{self.name} [{self.number}] P{self.atype}")
    def closeAccount(self):
        None
    def deposit(self,amount):
        self.amount=input
        self.__balance+=amount
        print("")
    def addInterest(self):
        None
    def __del__(self):
        del self.__accounts
        print("All of your accounts have been deleted")

class Account:
    def __init__(self,name,number):
        self.name=name
        self.number=number
        self.__balance=balance
    def getBalance(self):
        print(self.__balance)
    def deposit(self,amount):
        print("Ready to deposit an amount")
        self.amount=float(input("Enter amount to deposit: "))
        print(f"You are about to deposit an amount of P {self.amount}")
        MARKIPLIER=input("Enter account number: ")
        self.__balance+=amount
        print("Deposit successful")
        print(f"{self.name} [{self.number}] P{self.atype}")
    def withdraw(self,amount):
        print("Ready to withdraw an amount")
        self.amount=float(input("Enter amount to withdraw: "))
        print(f"You are about to withdraw an amount of P {self.amount}")
        MARKIPLIER=input("Enter account number: ")
        self.__balance-=amount
        print("Deposit successful")
        print(f"{self.name} [{self.number}] P{self.atype}")
    def __str__(self):
        return f"{self.name} [{self.number}] P{self.atype}""
    def __del__(self):
        del self.name
        print("Your account has now been deleted")
class SavingsAccount:
    def __init__(self):
        self.__interest=0.05
    def addInterest(self):
        None
        
mbtc=Bank("Metrobank")
mbtc.openAccount()
mbtc.openAccount()
mbtc.showAccounts()
mbtc.deposit()
mbtc.deposit()
mbtc.addInterest()
mbtc.closeAccount()
