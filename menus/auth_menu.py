
from classes.customer import Customer


# menus/auth_menu.py

def show_main_menu():
    """Display main menu options"""
    print("\n" + "="*40)
    print("     CENTRAL BANK SYSTEM")
    print("="*40)
    print("1. Sign In")
    print("2. Sign Up")
    print("3. Exit")
    return input("Choose (1-3): ")

def sign_in():
    """Get sign in credentials"""
    customer_id = input("Enter ID: ")
    password = input("Enter password: ")
    return customer_id, password

def sign_up():
    """Get new account information"""
    print("\n--- New Account ---")
    name = input("Enter full name: ")
    password = input("Enter password: ")
    confirm = input("Confirm password: ")
    
    if password != confirm:
        print("❌ Passwords don't match!")
        return None
    
    return name, password  