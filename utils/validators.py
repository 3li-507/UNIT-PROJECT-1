# utils/validators.py

def validate_password(password, confirm):
    """Check if passwords match"""
    return password == confirm

def validate_bank_choice(choice):
    """Validate bank selection (1 or 2)"""
    return choice in ["1", "2"]

def validate_amount(amount):
    """Validate transaction amount (positive number)"""
    try:
        amt = float(amount)
        return amt > 0
    except ValueError:
        return False

def validate_id(customer_id):
    """Validate ID format (6 digits, starts with 4 or 2)"""
    if len(customer_id) != 6:
        return False
    if not customer_id.isdigit():
        return False
    return customer_id[0] in ["2", "4"]