class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}  

    def create_account(self, account_id, initial_balance=0):
        if account_id not in self.accounts:
            self.accounts[account_id] = BankAccount(account_id, initial_balance)
            
    def get_account(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id]
        else:
            print(f"Account {account_id} not found.")
            return None

    def make_deposit(self, account_id, amount):
        account = self.get_account(account_id)
        if account:
            account.deposit(amount)
            print(f"Deposit of {amount} to account {account_id} successful.")

    def make_withdrawal(self, account_id, amount):
        account = self.get_account(account_id)
        if account:
            if account.withdrawal(amount):
                print(f"Withdrawal of {amount} from account {account_id} successful.")
            else:
                print(f"Withdrawal from account {account_id} failed due to insufficient funds.")

    def display_accounts(self):
        print(f"User: {self.name}'s Accounts:")
        for account_id, account in self.accounts.items():
            print(account.display_account_info())

class BankAccount:
    def __init__(self, account_id, balance=0):
        self.account_id = account_id
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
    
    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
    
    def display_account_info(self):
        return f"Account ID: {self.account_id}, Balance: {self.balance}"

