# Take the input from the user and Update the table
import sqlite3

myconn = None

try:
    myconn = sqlite3.connect("Student.db")
    print("Connected to existing database")

    mycursor = myconn.cursor()

    roll_no = int(input("Enter Roll Number to update: "))
    new_name = input("Enter New Name: ")

    mycursor.execute("""
    UPDATE stud
    SET name = ?
    WHERE rollno = ?
    """, (new_name, roll_no))

    myconn.commit()

    # check if record was updated or not
    if mycursor.rowcount > 0:
        print("Record updated successfully")
    else:
        print("No record found for Roll Number", roll_no)

except ValueError:
    print("Invalid input! Please enter correct data types.")

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if myconn:
        myconn.close()
        print("Database connection closed")
