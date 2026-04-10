while True:
    try:
        x=int(input("enter a number: "))
        if (x<0):
            raise ValueError;
        else:
            print("the number is positive\n")
    except ValueError:
            print("ERORR: The number is negative!!!\n")
            continue
