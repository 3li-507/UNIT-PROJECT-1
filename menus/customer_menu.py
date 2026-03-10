# menus/customer_menu.py
from colorama import Fore,Style,Back

from utils.validators import validate_amount
from utils.file_manager import load_data, save_data
from classes.Transactions import Transaction

def show_customer_menu(customer):
    """Display customer menu and handle choices"""
    
    while True:
            
        try:
            print("\n" + "="*20)
            print(f"   {Back.BLUE} Welcome {customer.name} {Style.RESET_ALL}")
            print("="*40)
            print(f"{Fore.MAGENTA}1.Deposit")
            print("2.Withdraw")
            print("3.Show Balance")
            print("4.Transfer")
            print(f"5.Logout{Style.RESET_ALL}")
            print("="*20)
        
            choice = input("Choose (1-5): ")
        
            if choice == "1":
                deposit(customer)
            elif choice == "2":
                withdraw(customer)
            elif choice == "3":
                show_balance(customer)
            elif choice == "4":
                transfer(customer)
            elif choice == "5":
                print(f"{Fore.CYAN}Logging out...{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}Invalid choice{Style.RESET_ALL}")
        
            input("\nPress Enter to continue...")
        except Exception as e:
            print(f"Error: {e}")
        except:
            print(f"{Fore.YELLOW}Some error happened{Style.RESET_ALL}")

def deposit(customer):
        """Handle deposit operation"""
        try:
            print("\n--- Deposit ---")
    
            amount = input("Enter amount to deposit: ")
    
            if not validate_amount(amount):
                print(f"{Fore.RED} Invalid amount. Please enter a positive number.{Style.RESET_ALL}")
                return 
    
            amount = float(amount)
            success, message = customer.deposit(amount)
    
            if success:
                # Update balance in JSON
                customers = load_data("customers.json")
                for c in customers:
                    if c["id"] == customer.id:
                        c["balance"] = customer.balance
                        break
                save_data("customers.json", customers)

                #to record transaction(deposit):
                t = Transaction(customer.id, customer.id, amount, "deposit")
                transactions = load_data("transactions.json")
                transactions.append(t.to_dict())
                save_data("transactions.json", transactions)

        
                print(f"{Fore.GREEN} {message}{Style.RESET_ALL}")
            else:
                print(f"{Fore.GREEN} {message}{Style.RESET_ALL}")

        except Exception as e:
            print(f"Error: {e}")
        except:
            print("Some error happened")

def withdraw(customer):
    """Handle withdraw operation"""
    try:
        print("\n--- Withdraw ---")
    
        amount = input("Enter amount to withdraw: ")
    
        if not validate_amount(amount):
            print(f"{Fore.RED} Invalid amount. Please enter a positive number.{Style.RESET_ALL}")
            return
    
        amount = float(amount)
        success, message = customer.withdraw(amount)
    
        if success:
            # Update balance in JSON
            customers = load_data("customers.json")
            for c in customers:
                if c["id"] == customer.id:
                    c["balance"] = customer.balance
                    break
            save_data("customers.json", customers)

            #to record transaction(Withdraw):
            t = Transaction(customer.id, customer.id, amount, "withdraw")
            transactions = load_data("transactions.json")
            transactions.append(t.to_dict())
            save_data("transactions.json", transactions)
        
            print(f"{Fore.GREEN} {message}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED} {message}{Style.RESET_ALL}")

    except Exception as e:
            print(f"Error: {e}")
    except:
        print("Some error happened")

def show_balance(customer):
    """Display current balance"""
    print(f"\n Current balance: {Fore.CYAN}{customer.balance} SAR{Style.RESET_ALL}")

def transfer(customer):
    """Handle transfer to another customer"""
    try:
        print("\n--- Transfer ---")
    
        # 1. 
        to_id = input("Enter recipient ID: ")
    
        # 2. 
        customers_data = load_data("customers.json")
        recipient = None
    
        for c in customers_data:
            if c["id"] == to_id:
                recipient = c
                break
    
        if not recipient:
            print(f"{Fore.RED} Recipient not found{Style.RESET_ALL}")
            return
    
        # 3. 
        amount = input("Enter amount: ")
        if not validate_amount(amount):
            print(f"{Fore.RED} Invalid amount{Style.RESET_ALL}")
            return
    
        amount = float(amount)
    
        # 4.
        if customer.balance < amount:
            print(f"{Fore.RED} Insufficient balance{Style.RESET_ALL}")
            return
    
        # 5. 
        customer.balance -= amount
        recipient["balance"] += amount
        
    
        # 6. 
        for c in customers_data:
            if c["id"] == customer.id:
                c["balance"] = customer.balance
                break
    
        save_data("customers.json", customers_data)
    #to record transaction(transfer):
        t = Transaction(customer.id, to_id, amount, "transfer")
        transactions = load_data("transactions.json")
        transactions.append(t.to_dict())
        save_data("transactions.json", transactions)
        
        # print(f"{Fore.GREEN} {message}{Style.RESET_ALL}")
        
        # print(f"{Fore.RED} {message}{Style.RESET_ALL}")
       
    
        print(f"\n{Fore.GREEN} Transferred {amount} SAR to {recipient['name']}{Style.RESET_ALL}")
        print(f"   Your new balance: {customer.balance} SAR")

    except Exception as e:
            print(f"Error: {e}")
    except:
        print("Some error happened")