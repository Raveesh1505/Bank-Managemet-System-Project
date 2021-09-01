from connection_db import *

def customer_search():
    conn, c = connect_db()
    print("Search Parameter:")
    print("")
    print("1. Search record by name")
    print("")
    print("2. Search record by account number")
    print("")
    print("3. Search record by user ID")
    print("")
    print("4. Search by email ID")
    print("")
    search_param = int(input("Enter the suitable option number (1, 2 or 3): "))
    print("")
    
    if search_param == 1:
        name_input = input("Enter your registered full name: ")
        name = name_input.upper()
        c.execute("""SELECT NAME, PHONE, EMAIL, ADDRESS, ACC_TYPE, ACC_NUMBER, USER_ID, BALANCE FROM BANK_DETAILS WHERE NAME = ?;""", (name,))
        res_1 = c.fetchall()
        for column in res_1:
            print("Name: ", column[0])
            print("Phone: ", column[1])
            print("E-Mail: ", column[2])
            print("Address: ", column[3])
            print("Account Type: ", column[4])
            print("Account Number: ", column[5])
            print("User ID: ", column[6])
            print("Balance: ", column[7])

    elif search_param == 2:
        acc_number_input = input("Enter your account number: ")
        acc_number = acc_number_input.upper()
        c.execute("SELECT NAME, PHONE, EMAIL, ADDRESS, ACC_TYPE, ACC_NUMBER, USER_ID, BALANCE FROM BANK_DETAILS WHERE ACC_NUMBER = ?", (acc_number,))
        res_2 = c.fetchall()
        for column in res_2:
            print("Name: ", column[0])
            print("Phone: ", column[1])
            print("E-Mail: ", column[2])
            print("Address: ", column[3])
            print("Account Type: ", column[4])
            print("Account Number: ", column[5])
            print("User ID: ", column[6])
            print("Balance: ", column[7])

    elif search_param == 3:
        user_id = input("Enter your User ID: ")
        c.execute("SELECT NAME, PHONE, EMAIL, ADDRESS, ACC_TYPE, ACC_NUMBER, USER_ID, BALANCE FROM BANK_DETAILS WHERE USER_ID = ?", (user_id,))
        res_3 = c.fetchall()
        for column in res_3:
            print("Name: ", column[0])
            print("Phone: ", column[1])
            print("E-Mail: ", column[2])
            print("Address: ", column[3])
            print("Account Type: ", column[4])
            print("Account Number: ", column[5])
            print("User ID: ", column[6])
            print("Balance: ", column[7])

    elif search_param == 4:
        email_input = input("Enter your registered email ID: ")
        email = email_input.upper()
        c.execute("SELECT NAME, PHONE, EMAIL, ADDRESS, ACC_TYPE, ACC_NUMBER, USER_ID, BALANCE FROM BANK_DETAILS WHERE EMAIL = ?", (email,))
        res_4 = c.fetchall()
        for column in res_4:
            print("Name: ", column[0])
            print("Phone: ", column[1])
            print("E-Mail: ", column[2])
            print("Address: ", column[3])
            print("Account Type: ", column[4])
            print("Account Number: ", column[5])
            print("User ID: ", column[6])
            print("Balance: ", column[7])

    else:
        print("Invalid input. Please try again.")