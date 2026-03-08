from classes.user import User

class Customer(User):

    def __init__(self,id,name,password,is_frozen:bool,bank,balance=0):

        #super() refers to Class User    
        super().__init__(id,name,password)

        # additional properties for customer:
        self.bank=bank
        self.balance=balance
        self.is_frozen=False

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount

            return f'Deposited {amount} successfully. New balance: {self.balance}'
       
        return f'failed deposit'
    
    def withdraw(self,amount):
        
        if amount<=0:
            return f'amount must be <0'
        
        if self.is_frozen==True:
            return f"Your account is frozen. You can't withdraw"
        
        if self.balance<amount:
            return f"Insufficient balance. Current balance: {self.balance}"
        
        self.balance-=amount
        return f"Withdraw {amount} successfully. New Balance: {self.balance}"
    
    def show_balance(self):
        return f"Current balance: {self.balance}"