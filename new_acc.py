from connection_db import *

def new_acc():
    print("PERSONAL DETAILS")
    print("")
    name_input = input("Enter your full name: ")
    name = name_input.upper()
    phone = input("Enter your phone number: ")
    email_input = input("Enter your E-Mail ID: ")
    email = email_input.upper()
    print("")
    print("ADDRESS DETAILS")
    print("")
    hno = input("Address line 1: ")
    city = input("Residing city: ")
    state = input("Residing state: ")
    pincode = input("Pincode: ")
    address = hno.upper() + ", " + city.upper() + ", " + state.upper() + ", " + pincode
    print("")
    print("ACCOUNT DETAILS")
    print("")
    acc_type_input = input("Enter your account type: ")
    acc_type = acc_type_input.upper()
    acc_number = "BA" + name[0:2].upper() + "00" + phone[0:3] + city[0:2].upper() + "AC"
    print("")
    print("Your account number is ", acc_number, ". Please keep it safe for future reference.")
    print("")
    print("SET YOUR LOGIN DETAILS")
    print("")
    userid = input("Enter your prefered User ID: ")
    pin = input("Set your 4 digit pin: ")
    print("")
    print("Your User-ID is ", userid, " and 4 digit secure PIN is ", pin, ". Please keep it safe for future reference.")

    # Inserting details into the database

    conn, c = connect_db()

    c.execute("""INSERT INTO BANK_DETAILS (NAME, PHONE, EMAIL, ADDRESS, ACC_TYPE, ACC_NUMBER, USER_ID, PIN, BALANCE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (name, phone, email, address, acc_type, acc_number, userid, pin, "0"))
    conn.commit()
    print("Registered successfully!!! Please have a look at your details below:")
    print("")
    c.execute('SELECT * FROM BANK_DETAILS WHERE ACC_NUMBER = ?', (acc_number,))
    res = c.fetchall()
    for column in res:
        print("Name: ", column[0])
        print("Phone: ", column[1])
        print("E-Mail: ", column[2])
        print("Address: ", column[3])
        print("Account Type: ", column[4])
        print("Account Number: ", column[5])
        print("User ID: ", column[6])
        print("Balance: ", column[8])