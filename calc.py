while True:
    x=int(input("enter the first number: "))
    y=int(input("enter the second number: "))
    o=str(input("enter the operation to be done: ")) 
    match o:
        case '+':
            print("addition :",x+y)
        case '-':
            print("subtraction :",x-y)
        case '*':
            print("multiplication :",x*y)
        case '/':
            try:
                print("division :",x/y)
            except ZeroDivisionError:
                print("ERROR: Division by zero not allowed!!!\n")
                continue
            case '%':
                print("modulus :",x%y)
            case _:
                print("ERROR: enter a valid operation!!!")
     print("\n")

            


 
 


 

 

