email = "pahatijanelle@gmail.com"
password = "janelle07"


attempt =0


while attempt <3:
    enteredemail = input("Email: ")
    enteredpass = input("Password: ")
   
    if enteredemail == email and enteredpass == password:
        print("Login Successful!")
        break
   
    attempt+=1
    print("Attempts remaining:", 3 - attempt)
    if enteredemail != email and enteredpass != password:
        print("The email and password you entered are incorrect! Please try again.")
    elif enteredemail != email:
        print("The email you entered is incorrect! Please try again.")
    else:
        print("The password you entered is incorrect! Please try again.")
    if attempt == 3:
        print("Account Locked!")
