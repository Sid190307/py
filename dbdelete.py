# Accept the Roll No from the user and delete record from the table
import sqlite3

myconn = None

try:
    myconn = sqlite3.connect("Student.db")
    print("Connected to existing database")

    mycursor = myconn.cursor()

    roll_no = int(input("Enter Roll Number to delete: "))

    mycursor.execute("""
        DELETE FROM stud
        WHERE rollno = ?
    """, (roll_no,))

    myconn.commit()

    if mycursor.rowcount > 0:
        print("Record deleted successfully")
    else:
        print("No record found for Roll Number", roll_no)

except ValueError:
    print("Invalid input! Roll number must be an integer.")

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if myconn:
        myconn.close()
        print("Database connection closed")
