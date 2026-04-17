import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Srivarsha@1234",
    database="atm"
)

print("Connected successfully!")


cursor = conn.cursor()





# cursor.execute("select * from accounts;")

# rows = cursor.fetchall()

# for row in rows:
#     print(row)


# cursor.execute("SHOW TABLES")

# for table in cursor:
#     print(table)

# conn.close()

# cursor.execute("""
# SELECT * FROM products
# ORDER BY price DESC
# LIMIT 1
# """)

# print("Highest price:", cursor.fetchall())


# User input
acc_no = int(input("Enter account number: "))

while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

 # Check balance
    if choice ==1:
        cursor.execute("select balance from accounts where acc_no = %s",(acc_no,))
        balance= cursor.fetchone()[0]
        print("Your balance is:", balance)
        
# Deposit
    elif choice == 2:
        amount = float(input("enter amount to deposit:"))
        cursor.execute("update accounts set balance = balance + %s where acc_no = %s",(amount,acc_no))
        conn.commit()   
        print("Amount deposited successfully!")

# Withdraw
    elif choice == 3:
        amount = float(input("enter amount to withdraw:"))
        cursor.execute("select balance from accounts where acc_no = %s",(acc_no,))
        balance= cursor.fetchone()[0]
        if balance >= amount:
            cursor.execute("update accounts set balance = balance - %s where acc_no = %s",(amount,acc_no))
            conn.commit()   
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")

    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")  
        
        
    
        