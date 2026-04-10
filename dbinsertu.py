# Accept the input from the user and insert in the table
import sqlite3

myconn = None

try:
    myconn = sqlite3.connect("Student.db")
    print("Database connected successfully...")

    mycursor = myconn.cursor()

    roll_no = int(input("Enter Roll no - "))
    name = input("Enter Name - ")

    mycursor.execute("""
    insert into stud (rollno, name)
    values (?,?)
    """, (roll_no, name))

    myconn.commit()
    print("Record inserted successfully...")

except sqlite3.IntegrityError:
    print("Error: Roll number already exists...")

except sqlite3.Error as e:
    print("Database Error -", e)

except ValueError:
    print("Invalid input! please enter correct data")

finally:
    if myconn:
        myconn.close()
        print("Database connection closed...")
