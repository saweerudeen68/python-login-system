user =  input("Enter Email:")
if '@' in user:
    password = input("Enter password:")
    if user == "vscode@gmail.com" and password == "12345":
        print("login successful")
    elif user == "vscode@gmail.com" and password !="12345":
        print ("Incorrect passwrod")
        password =input("Enter correct passwrod:")
        if password == "12345":
            print("Finally login successful")
        else:
            print("Still incorrect")

    else:
        print ("Invalid credentials")
else:
    print ("email is incorrect")