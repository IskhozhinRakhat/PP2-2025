class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print(f"Your balance has been replenished! Your balance: {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print(f"insufficient funds for withdrawal! Your balance: {self.balance}")
        else:
            self.balance -= money
            print(f"Your balance after the money has been debited: {self.balance}")

    def __str__(self):
        return(f"Account owner: {self.owner}\nAccount balance: {self.balance}")
owner = input("Enter your name: ")
start_money = float(input("Enter your balance: "))
account = Account(owner, start_money)
print(account)

add_money = float(input("How much money do you want to deposit: "))
account.deposit(add_money)
add_money = float(input("How much money do you want to deposit: "))
account.deposit(add_money)

money = float(input("How much money do you want to withdraw: "))
account.withdraw(money)
money = float(input("How much money do you want to withdraw: "))
account.withdraw(money)

print(account)
