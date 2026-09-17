class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\n Account '{self.name}' is created. \n Balance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\n Account '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposit Complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
            f"\n Sorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
        )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance -  amount
            print("withdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n***************\n Beginning Transfer...")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete")
        except BalanceException as error:
            print(f"\nTransfer interrupted.... {error}")

class InterestRewardsAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\ndeposit complete.")
        self.getBalance()

class SavingsAcc(InterestRewardsAcc):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\n withdraw completed")
        except BalanceException as error:
            print(f"\n withdraw interrupted: {error}")