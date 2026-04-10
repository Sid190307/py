import sqlite3

myconn = None

try:
    myconn = sqlite3.connect("Student.db")
    print("Database connection successful...")

    mycursor = myconn.cursor()

    mycursor.execute("""
    insert into stud (rollno, name)
    values (?,?)
    """, (101, "rohan"))

    myconn.commit()
    print("Record inserted successfully...")

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if myconn:
        myconn.close()
        print("Database connection closed")
