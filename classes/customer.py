from classes.user import User

from colorama import Fore,Style

class Customer(User):

    def __init__(self,id,name,password,balance=0.0):

        #super() refers to Class User    
        super().__init__(id,name,password)

        # additional property for customer:
        
        self.balance=balance

        #print(f"DEBUG in Customer __init__: id={id}, balance={balance}")
        
        

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount

            return True,f'{Fore.GREEN}Deposited {amount} successfully. New balance: {self.balance}{Style.RESET_ALL}'
       
        return False,f'{Fore.RED}failed deposit{Style.RESET_ALL}'
    
    def withdraw(self,amount):
        
        if amount<=0:
            return False,f'{Fore.RED}amount must be <0{Style.RESET_ALL}'
        
        if self.balance<amount:
            return False,f"{Fore.RED}Insufficient balance. {Style.RESET_ALL}Current balance: {self.balance}"
        
        self.balance-=amount
        return True,f"{Fore.GREEN}Withdraw {amount} successfully.{Style.RESET_ALL} New Balance: {self.balance}"
    
    def show_balance(self):
        return f"Current balance: {self.balance}"
    
    def to_dict(self):

        return{
            "id":self.id,
            "name":self.name,
            "password":self.password,
            "balance":self.balance
        }