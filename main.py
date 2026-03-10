# main.py
from colorama import Fore , Back, Style

from menus.auth_menu import show_main_menu, sign_in, sign_up
from menus.customer_menu import show_customer_menu
from classes.customer import Customer
from utils.file_manager import load_data, save_data
from utils.id_generator import generate_customer_id

def main():
    """Main program loop"""
    #def show_customer_menu(customer):  
     #print(f"Debug (in menu): balance={customer.balance}")
    #  pass

while True:
    try:
        choice = show_main_menu()
        
        if choice == "1":
            # Sign In
            cust_id, password = sign_in()
            
            # Load customers from file
            customers_data = load_data("customers.json")
            found_customer = None
            
            for c_data in customers_data:
                if c_data["id"] == cust_id and c_data["password"] == password:
                    # Create Customer object with current balance
                    found_customer = Customer(
                        c_data["id"],
                        c_data["name"],
                        c_data["password"],
                        c_data.get("balance", 0.0)  # if there is no balance put 0.0
                    )
                    break
            
            if found_customer:
                print(f"\n Welcome back, {found_customer.name}!")
                # print(f"Debug- Balance from file: {c_data['balance']}")
                # print(f"Debug- Customer object balance: {found_customer.balance}")
                show_customer_menu(found_customer)
            else:
                print(f"\n{Fore.RED} Invalid ID or password{Style.RESET_ALL}")
        
        elif choice == "2":
            # Sign Up
            result = sign_up()
            
            if result:
                name, password = result
                
                # Generate new ID
                new_id = generate_customer_id()
                
                # Create new customer
                new_customer = Customer(new_id, name, password, 0.0)
                
                # Save to file
                customers = load_data("customers.json")
                customers.append(new_customer.to_dict())
                save_data("customers.json", customers)
                
                print(f"\n{Fore.GREEN}Account created successfully!{Style.RESET_ALL}")
                print(f"   Your ID is: {new_id}")
                print("   Please sign in with your new ID")
        
        elif choice == "3":
            print("\n Thank you for using our Bank System. Goodbye!")
            break
        
        input("\nPress Enter to continue...")
    except Exception as e:
            print(f"Error: {e}")
    except:
        print("Some error happened")

if __name__ == "__main__":
    main()