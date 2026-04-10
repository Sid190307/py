while True:
    try:
        name=str(input("enter the name ofthe file you want to open: "))
        f=open(name,'r')
        contents=f.read()
    except FileNotFoundError:
        print("ERROR: File not found!!!!\n")
        continue
    else:
        print("the contents inside the file are: ",contents)
        f.close()
        break
    finally:
        print("Operation successful.")
        print("file closed successfully.\n")
        
    
        
 


 


 
 

