from classes.customer import Customer
from colorama import Style,Fore,Back

# from classes.transaction import Transaction

#customer=Customer(1,"ali","ali123",False,"Red",0)
# customer=Customer(1,"ali","ali123",False,"Red",0)

# message=customer.deposit(500)
# print(message)

# print(customer.deposit(0))

# print("\n\n"+customer.withdraw(200))

# print(customer.show_balance())

# t1 = Transaction("400001", "400001", 1000, "deposit")
# t2 = Transaction("400001", "400001", 200, "withdraw") 
# t3 = Transaction("400001", "200001", 500, "transfer")
# print(f"{t1.from_id} , {t1.to_id} ,{t1.amount} {t1.type}")
# print(f"{t2.from_id} , {t2.to_id} ,{t2.amount} {t2.type}")
# print(f"from: {t3.from_id}  to: {t3.to_id} amount:{t3.amount} type:{t3.type}")





# t1 = Transaction("400001", "400002", 500, "transfer")
# print("Transaction ID:", t1.transaction_id)
# print("From:", t1.from_id)
# print("To:", t1.to_id)
# print("Amount:", t1.amount)
# print("Type:", t1.type)
# print("Date:", t1.date)
# print("Status:", t1.status)
# print("-"*10)


# t2 = Transaction("400001", "400001", 1000, "deposit")
# print("\nDeposit transaction:")
# print("ID:", t2.transaction_id)
# print("Amount:", t2.amount)
# print("*"*30)

# from utils.validators import *

# print(validate_password("123", "123"))  # True
# print(validate_bank_choice("1"))        # True
# print(validate_amount("500"))            # True
# print(validate_id("400001"))             # True
# print(validate_id("123"))                # False
# x=5
# print(f"{x:03d}")



# from currency_converter import CurrencyConverter

# c=CurrencyConverter()

# print(c.convert(100,'SAR','USD'))


# main.py (مؤقت للاختبار)
# from classes.customer import Customer
# from menus.customer_menu import deposit

# # إنشاء عميل تجريبي
# test_customer = Customer("400001", "أحمد", "1234", "blue", 5000)

# # اختبار الإيداع
# deposit(test_customer)

# # شوف الرصيد بعد الإيداع
# print(f"\nFinal balance: {test_customer.balance} {test_customer.currency}")
# test.py
# from classes.customer import Customer
# from menus.customer_menu import deposit
# from utils.file_manager import load_data

# # اقرأ الرصيد من الملف
# customers = load_data("customers.json")
# test_customer = None

# for c in customers:
#     if c["id"] == "400001":
#         test_customer = Customer(
#             c["id"],
#             c["name"],
#             c["password"], 
#             c["bank"],
#             c["balance"]  # الرصيد الحقيقي من الملف
#         )
#         break

# if test_customer:
#     print(f"Before deposit: {test_customer.balance} {test_customer.currency}")
#     deposit(test_customer)
    
#     # اقرأ الملف مرة ثانية عشان نشوف الرصيد الجديد
#     customers_after = load_data("customers.json")
#     for c in customers_after:
#         if c["id"] == "400001":
#             print(f"After deposit (from file): {c['balance']} {test_customer.currency}")
#             break
# else:
#     print("Customer 400001 not found!")

# test.py
print("Testing...")
from menus.auth_menu import show_main_menu
print("Import successful")
choice = show_main_menu()
print(f"You chose: {choice}")