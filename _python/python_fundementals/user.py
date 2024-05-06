class User:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        if self.balance > amount:
            self.balance -= amount
    def display_balance(self):
        print (f"User: {self.name}, {self.balance}")

    def transfer_money(self, other_user, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_user.balance += amount
            print(f"Transfer of {amount} to {other_user.name} successful.")
        else:
            print("Insufficient funds for transfer.")

saeed = User("Saeed","Saeed.com", 500)

majed = User("majed", "majed.cpm", 520)

ola= User("ola","ola.com",100000)

saeed.make_deposit(100)
saeed.make_deposit(200)
saeed.make_deposit(500)
saeed.make_withdrawal(1)
saeed.display_balance()

majed.make_deposit(1000)
majed.make_deposit(200)
majed.make_withdrawal(500)
majed.make_withdrawal(1)
majed.display_balance()


ola.make_deposit(1000)
ola.make_withdrawal(200)
ola.make_withdrawal(500)
ola.make_withdrawal(1)
ola.display_balance()

saeed.transfer_money(ola,200)
saeed.display_balance()