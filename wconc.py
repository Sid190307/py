class Students: pass

def display_info(name,rollno):
    print("the name of the student is ",name," and the roll no is ",rollno)

    s1 = Students() s2 = Students()

    s1.name = "Ramesh"
    s1.rollno = 21

    s2.name = "Suraj"
    s2.rollno = 45

    display_info(s1.name,s1.rollno)
    display_info(s2.name,s2.rollno)
