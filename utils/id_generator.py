
# utils/id_generator.py
from utils.file_manager import load_data

def generate_customer_id():
    """Generate new customer ID (starts from 100001)"""
    
    # Load existing customers
    customers = load_data("customers.json")
    
    # If no customers yet, start from 100001
    if not customers:
        return "100001"
    
    # Find the highest ID
    max_id = 0
    for c in customers:
        try:
            num = int(c["id"])
            if num > max_id:
                max_id = num
        except:
            continue
    
    # Return next ID
    return str(max_id + 1)