# classes/transaction.py
from datetime import datetime

class Transaction:
    def init(self, from_id, to_id, amount, trans_type):
        self.from_id = from_id
        self.to_id = to_id
        self.amount = amount
        self.type = trans_type  # "deposit", "withdraw", "transfer"
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self):
        return {
            "from_id": self.from_id,
            "to_id": self.to_id,
            "amount": self.amount,
            "type": self.type,
            "date": self.date
        }