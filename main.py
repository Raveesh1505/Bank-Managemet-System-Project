from cash_deposit import *
from cash_withdrawal import *
from connection_db import *
from new_acc import *
from customer_search import *

connect_db()
opt = ""

while opt != "Exit":
    # Main menu and final script
    print()
    print ("WELCOME TO THE BANK!")
    print("")
    print("MAIN MENU")
    print("")
    print("1. Customer search")
    print("")
    print("2. Register new account")
    print("")
    print("3. Deposit Cash")
    print("")
    print("4. Withdraw cash")
    print("")
    opt = input("Enter the suitable option (1, 2, 3 or 4) to proceed further:")

    # Defining every option

    if opt in ("1", "1."):
        print("")
        print("EXISTING CUSTOMER SEARCH")
        print("")
        customer_search()
        print("")
    elif opt in ("2", "2."):
        print("")
        print("NEW CUSTOMER REGISTRATION")
        new_acc()
        print("")
    elif opt in ("3", "3."):
        print("")
        print("CASH DEPOSIT")
        print("")
        cash_deposit()
        print("")
    elif opt in ("4", "4."):
        print("")
        print("CASH WITHDRAW")
        print("")
        cash_withdraw()
        print("")
    else:
        print("Invalid input or system error. Please try again.")