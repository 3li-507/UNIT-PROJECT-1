class User:
    def __init__(self,id:str,name:str,password:str):
        self.id=id
        self.name=name
        self.password=password
        
    def check_password(self,entered_password):
        if self.password==entered_password:
            return True
        
        return False
    #retrun self.password == entered_password

