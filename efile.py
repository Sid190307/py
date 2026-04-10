while True:

    try:
        name = input("Enter the path/name of the file: ")
        file = open(name, "r")
        contents = file.read()

        print("The contents of the file are: ")
        print(contents)

        file.close()


        file.read()

    except FileNotFoundError:
        print("ERROR: File does not exist!!!\n")
        continue

    except IsADirectoryError:
        print("ERROR: The path you entered is a directory, not a file!!\n")
        continue

    except PermissionError:
         print("ERROR: You don't have permission to read this file!!!\n")
         continue
    except IOError:
        print("ERROR: Some input/output error occurred!!!\n")
        continue

    except OSError as e:
        print("ERROR:", e, "\n")
        continue
    finally:
        print("File closed successfully!!\n") 
