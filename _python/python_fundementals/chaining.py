class User:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance
        
    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.balance > amount:
            self.balance -= amount
        return self
        
    def display_balance(self):
        print (f"User: {self.name}, {self.balance}")
        return self

    def transfer_money(self, other_user, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_user.balance += amount
            print(f"Transfer of {amount} to {other_user.name} successful.")
        else:
            print("Insufficient funds for transfer.")
        return self

saeed = User("Saeed","Saeed.com", 500)

majed = User("majed", "majed.cpm", 520)

ola= User("ola","ola.com",100000)

saeed.make_deposit(100).make_deposit(200).make_deposit(500).make_withdrawal(1).display_balance().transfer_money(ola,200).display_balance()

majed.make_deposit(1000).make_deposit(200).make_withdrawal(500).make_withdrawal(1).display_balance()


ola.make_deposit(1000).make_withdrawal(200).make_withdrawal(500).make_withdrawal(1).display_balance()

