
from utils.file_manager import load_data

# utils/id_generator.py

def generate_customer_id(bank):
    """Generate new customer ID based on bank"""
    
    # Set prefix based on bank
    if bank == "red":
        prefix = "2"
    else:  # blue
        prefix = "4"
    
    # Load existing customers
    customers = load_data("customers.json")
    
    # Filter customers by bank prefix
    bank_customers = []
    for c in customers:
        if c["id"].startswith(prefix):
            bank_customers.append(c)
    
    # If no customers yet, start from 00001
    if not bank_customers:
        return f"{prefix}00001"
    
    # Find the highest number
    max_num = 0
    for c in bank_customers:
        # Extract numbers after prefix (400001 → 00001 → 1)
        num = int(c["id"][1:])
        if num > max_num:
            max_num = num
    
    # Increment by 1 for new id
    new_num = max_num + 1
    # before: 400001 after: 400002 and so on..
    
    # Return with 5-digit format
    return f"{prefix}{new_num:05d}"