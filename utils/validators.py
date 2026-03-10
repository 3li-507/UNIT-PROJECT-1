# utils/validators.py

def validate_password(password, confirm):
    """Check if passwords match"""
    try:
        if not password or not confirm:
            return False
        return password == confirm
    except Exception:
        return False

def validate_amount(amount):
    """Validate transaction amount (positive number)"""
    try:
        if not amount:
            return False
        
        amount = amount.strip()
        if not amount:
            return False
        amt = float(amount)
        return amt > 0
    except (ValueError, TypeError):
        return False

def validate_id(customer_id):
    """Validate ID format (6 digits)"""
    try:
        if not customer_id:
            return False
        customer_id = customer_id.strip()
        if not customer_id:
            return False
        if len(customer_id) != 6:
            return False
        if not customer_id.isdigit():
            return False
        return True  
    except Exception:
        return False

def validate_choice(choice, min_val=1, max_val=6):
    """Validate menu choice is within range"""
    try:
        if not choice:
            return False
        choice = choice.strip()
        if not choice:
            return False
        num = int(choice)
        return min_val <= num <= max_val
    except (ValueError, TypeError):
        return False