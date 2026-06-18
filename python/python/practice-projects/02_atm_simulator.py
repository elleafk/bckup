from time import sleep
balance = 1000;
while True:
    print("ATM menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


    choice = input("Choose an option: ")


    if choice == "1":
        print("Your remaining balance is: "+ str(balance))
    elif choice == "2":
        amount = int(input("How much do you want to deposit? "))
        balance += amount
        print("You successfully deposited an amount of: " + str(amount))
        print("Your remaining balance now is: "+ str(balance))
    elif choice == "3":
        while True:
            amount = int(input("How much do you want to withdraw? "))
            if amount > balance:
                print("Your remaining balance is not enough for the requested amount! Please try again.")
            else:
                balance -=amount
                print("You successfully withdraw an amount of: " + str(amount))
                print("Your remaining balance now is: "+ str(balance))
                break
    elif choice == "4":
        print("Exiting...")
        sleep(3)
        break
    else:
        print("Enter a valid choice!")
