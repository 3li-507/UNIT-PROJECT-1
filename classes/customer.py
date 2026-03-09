from classes.user import User

class Customer(User):

    def __init__(self,id,name,password,is_frozen:bool,balance=0):

        #super() refers to Class User    
        super().__init__(id,name,password)

        # additional property for customer:
        
        self.balance=balance
        
        

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount

            return True,f'Deposited {amount} successfully. New balance: {self.balance}'
       
        return False,f'failed deposit'
    
    def withdraw(self,amount):
        
        if amount<=0:
            return False,f'amount must be <0'
        
        if self.balance<amount:
            return False,f"Insufficient balance. Current balance: {self.balance}"
        
        self.balance-=amount
        return True,f"Withdraw {amount} successfully. New Balance: {self.balance}"
    
    def show_balance(self):
        return f"Current balance: {self.balance}"
    
    def to_dict(self):

        return{
            "id":self.id,
            "name":self.name,
            "password":self.password,
            "balance":self.balance
        }