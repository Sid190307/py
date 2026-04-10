while True:
    try:
        l=[1,2,3,5]
        print("list l: ",l)
        x=int(input("Enter the list index of the item youwant to print: "))
        print(l[x])
        print()
    except IndexError:
        print("ERROR: Enter the correct list index\n")
        continue
    except ValueError:
        print("ERROR: Enter a integer value\n")
        continue
    else:
        break
        


 


 


