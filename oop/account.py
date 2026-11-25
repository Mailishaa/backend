class Account:
    def __init__(self,name,number,):
        self.name= name 
        self.number= number
        self.balance=0
        self.balance=2
        self.account_status = False
        
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited {amount}.new balance is {self.balance}")
        else:
            print(f"Deposite must be positive")
    def withdraw(self,amount):
        if amount>self.balance:
            print(f"Insufficient Balance")
        elif amount>0:
            self.balance-=amount
            print(f"withrawn{amount}.new balance is{self.balance}")
        else:
            print(f"Withrawal must be positive")
    def transfer(self,target_account,amount):
        if amount<=0:
            print("Balance is low, top up your account")
        else:
            self.balance-=amount
            target_account.balance+=amount

            print(f"Successful transfer.Your balance is{self.balance}")
    def loan(self, amount):
        if amount>0:
            self.balance+=amount
            print(f"Borrowed {amount}.new balance is {self.balance}")
        else:
            print(f"Amount must be positive")
    def freeze(self, status):
        self.account_status = status
        if self.account_status:
            print("frozen")
        else:
            print("active")
        
        


