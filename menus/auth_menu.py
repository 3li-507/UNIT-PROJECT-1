from colorama import Fore,Style,Back
from classes.customer import Customer


# menus/auth_menu.py

def show_main_menu():
    """Display main menu options"""
    print("\n" + "="*20)
    print(f"  {Back.WHITE}BANK SYSTEM {Style.RESET_ALL}")
    print("="*20)
    print("1. Sign In")
    print("2. Sign Up")
    print("3. Exit")
    return input("Choose (1-3): ")

def sign_in():
    """Get sign in credentials"""

    try:
        customer_id = input("Enter ID: ")
        password = input("Enter password: ")

        return customer_id, password

    except:
        print("some error happened")
    


def sign_up():
    """Get new account information"""
    try:
        print("\n--- New Account ---")
        name = input("Enter your name: ")
        password = input("Enter password: ")
        confirm = input("Confirm password: ")
    
        if password != confirm:
            print(f"{Fore.RED} Passwords don't match!{Style.RESET_ALL}")
            return None
    
        return name, password  
    except:
        print("Some error happened")