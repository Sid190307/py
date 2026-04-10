import sqlite3

myconn = None

try:
    myconn = sqlite3.connect("Student.db")
    print("Connected to existing database...")

    mycursor = myconn.cursor()

    mycursor.execute("select * from stud")

    records = mycursor.fetchall()

    print("\nStudents Records")
    print("Roll No | Name")
    print("-" * 35)

    for row in records:
        print(row[0], "|", row[1])

except sqlite3.Error as e:
    print("Database Error :", e)

finally:
    if myconn:
        myconn.close()
        print("\nDatabase connection closed...")
