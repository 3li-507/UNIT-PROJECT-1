from datetime import datetime

class Transaction:
    def __init__(self, from_id, to_id, amount, transaction_type="transfer"):
        self.transaction_id=self.generate_id()
        self.from_id = from_id
        self.to_id = to_id
        self.amount = amount
        self.type = transaction_type
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
        self.status = "completed"
        #transfer between different banks include VAT
        self.vat = 0.0    

    def generate_id(self):
        """Generate simple transaction ID"""
        
        timestamp = datetime.now().strftime("%H%M%S")
        return f"TXN{timestamp}"