while True:
    try:
        x=str(input("Enter a password: "))
        if (len(x)<5):
            raise Exception;
    except Exception:
        print("the password is too small\n")
        continue
    else:
        break
