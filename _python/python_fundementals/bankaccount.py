class Bankaccount:
    def __init__ (self,balance=0,int_rate=0.01):
        self.balance= balance
        self.int_rate=int_rate
        
    def deposit (self,amount):
        self.balance+=amount
        return self
    
    def withdrawal (self,amount):
        if self.balance>amount:
            self.balance-=amount
        return self
    
    def display_account_info (self):
        print ( f"Balance: {self.balance}, Interest rate: {self.int_rate}")
        return self
    
    def yield_interest(self):
        if self.balance>0:
            self.balance+= self.balance * self.int_rate
        return self

theFrog=Bankaccount()
user2= Bankaccount()

theFrog.deposit(100).deposit(200).deposit(300).withdrawal(150).yield_interest().display_account_info()
user2.deposit(1000).deposit(2000).withdrawal(300).withdrawal(200).withdrawal(100).withdrawal(50).yield_interest().display_account_info()


