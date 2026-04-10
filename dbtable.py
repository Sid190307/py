import sqlite3

myconn = None

try:
    myconn = sqlite3.connect("Student.db")
    print("Database connected successfully!!")

    mycursor = myconn.cursor()

    mycursor.execute("""
    create table if not exists stud (
        rollno integer primary key,
        name Text NOT NULL
    )
    """)

    myconn.commit()
    print("student table created successfully!")

except sqlite3.Error as e:
    print("Database Error:", e)

finally:
    if myconn:
        myconn.close()
        print("Database connection closed")
