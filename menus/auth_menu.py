
from classes.customer import Customer


# menus/auth_menu.py

def show_main_menu():
    """Display main menu options"""
    print("\n" + "="*20)
    print("     CENTRAL BANK SYSTEM")
    print("="*20)
    print("1. Sign In")
    print("2. Sign Up")
    print("3. Exit")
    return input("Choose (1-3): ")

def sign_in():
    """Get sign in"""
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
        print("Password don't match!")
        return None
    
    print("Choose bank:")
    print("1. Blue Bank (ID starts with 4)")
    print("2. Red Bank (ID starts with 2)")
    bank_choice = input("Choose (1-2): ")
    
    
    if bank_choice=="1":
        bank="blue"
    elif bank_choice=="2":
        bank="red"
    else:
        print("Please choose only 1 or 2")
    
    return name, password, bank