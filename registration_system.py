print("User Registration System")
while True:
    username = input("Enter username: ")
    if len(username) <8:
        print("Username should be 8 characters long! Try again.")
    elif " " in username:
        print("Username could not contain spaces! Try again.")
    else:
        break
while True:
    password = input("Enter password: ")
    confirmpass = input("Confirm password: ")
    if len(password) <8:
        print("Password should be 8 characters long! Try again.")
    elif password != confirmpass:
        print("Password does not match! Try again")
    else:
        print("Registration Successful!")
        break
print("Login")
attempts = 0
while attempts <3:
    USERNAME = input("Username: ")
    PASSWORD = input("Password: ")
    
    if USERNAME == username and PASSWORD == password:
        print("Login Successful!")
        break
    
    attempts+=1
    if USERNAME != username and PASSWORD != password:
       print("Both username and password are incorrect! Try again")
    elif PASSWORD != password:
        print("Password is incorrect! Try again")
    else:
         print("Username is incorrect! Try again")
    print("Attempts remaining: "+ str(3-attempts))
    if attempts == 3:
        print("Account Locked!")
        


