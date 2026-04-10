while True:

 try:
     x=int(input("Enter a number: "))
     y=int(input("enter another number: "))
     z=x/y
 except ZeroDivisionError:
     print("ERROR: The number cannot be divided by zero!!\n")
     continue
 except ValueError:
     print("ERROR: Enter a integer value!!!\n")
     continue
 else:
     print(z) 
