# Retrieve only one record from the table using fetchone() method
import sqlite3

myconn = None

try:
    myconn = sqlite3.connect("Student.db")
    print("Connected to existing database...")

    mycursor = myconn.cursor()

    roll_no = int(input("Enter Roll no - "))

    mycursor.execute("""
        select * from stud where rollno = ?
    """, (roll_no,))

    record = mycursor.fetchone()

    if record:
        print("\nStudent Record Found:")
        print("\nRoll no :", record[0])
        print("\nName    :", record[1])
    else:
        print("\nRecord not found...")

except ValueError:
    print("Invalid roll no...")

except sqlite3.Error as e:
    print("Database Error :", e)

finally:
    if myconn:
        myconn.close()
        print("\nDatabase connection closed")
