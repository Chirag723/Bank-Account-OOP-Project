from bank_accounts import *

chirag = BankAccount(1000, "chirag")
sara = BankAccount(1000, "sara")

sara.deposit(500)

sara.withdraw(500)

sara.transfer(100, sara)

Jim = InterestRewardsAcc(1000, "Jim")

Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, chirag)

blaze = SavingsAcc(1000, "blaze")
blaze.getBalance()
blaze.deposit(100)
blaze.transfer(1000, sara)