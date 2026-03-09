# menus/customer_menu.py
from utils.validators import validate_amount
from utils.file_manager import load_data, save_data
from classes.Transactions import Transaction

def show_customer_menu(customer):
    """Display customer menu and handle choices"""
    
    while True:
        print("\n" + "="*40)
        print(f"     Welcome {customer.name} 👋")
        print("="*40)
        print("1. 💰 Deposit")
        print("2. 💸 Withdraw")
        print("3. 📊 Show Balance")
        print("4. Transfer")
        print("5. Logout")
        print("="*40)
        
        choice = input("Choose (1-4): ")
        
        if choice == "1":
            deposit(customer)
        elif choice == "2":
            withdraw(customer)
        elif choice == "3":
            show_balance(customer)
        elif choice == "4":
            transfer(customer)
        elif choice == "5":
            print("👋 Logging out...")
            break
        else:
            print("❌ Invalid choice")
        
        input("\nPress Enter to continue...")

def deposit(customer):
    """Handle deposit operation"""
    print("\n--- Deposit ---")
    
    amount = input("Enter amount to deposit: ")
    
    if not validate_amount(amount):
        print("❌ Invalid amount. Please enter a positive number.")
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

        #to record transaction:deposit,withdraw,transfer:
        t = Transaction(customer.id, customer.id, amount, "deposit")
        transactions = load_data("transactions.json")
        transactions.append(t.to_dict())
        save_data("transactions.json", transactions)

        
        print(f"✅ {message}")
    else:
        print(f"❌ {message}")

def withdraw(customer):
    """Handle withdraw operation"""
    print("\n--- Withdraw ---")
    
    amount = input("Enter amount to withdraw: ")
    
    if not validate_amount(amount):
        print("❌ Invalid amount. Please enter a positive number.")
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
        
        print(f"✅ {message}")
    else:
        print(f"❌ {message}")

def show_balance(customer):
    """Display current balance"""
    print(f"\n💰 Current balance: {customer.balance} SAR")

def transfer(customer):
    """Handle transfer to another customer"""
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
        print("❌ Recipient not found")
        return
    
    # 3. إدخال المبلغ
    amount = input("Enter amount: ")
    if not validate_amount(amount):
        print("❌ Invalid amount")
        return
    
    amount = float(amount)
    
    # 4. التحقق من الرصيد
    if customer.balance < amount:
        print("❌ Insufficient balance")
        return
    
    # 5. تنفيذ التحويل
    customer.balance -= amount
    recipient["balance"] += amount
    
    # 6. تحديث الملف
    for c in customers_data:
        if c["id"] == customer.id:
            c["balance"] = customer.balance
            break
    
    save_data("customers.json", customers_data)
    
    print(f"\n✅ Transferred {amount} SAR to {recipient['name']}")
    print(f"   Your new balance: {customer.balance} SAR")