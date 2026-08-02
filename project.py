print("===== Welcome to Python ATM =====")

a = input("Enter your name: ")
b = int(input("Enter your PIN: "))
Pin = 123456
balance = 10000

if b == Pin:
    print("valid")
    while True :
        print("1. Check Balance 2. Deposit Money 3. Withdraw Money 4. Exit")   
        c = int(input("----"))
        if c == 1:
            print(balance)
        elif c == 2:
            d = int(input("Enter deposit amount =  "))
            balance = balance + d
            print(balance)
        elif c == 3:
            wa = int(input("Enter withdraw amount =  "))
            if wa <= balance :
                balance = balance - wa
                print(balance)
            else:
                print("Insufficient Balance")
        elif c == 4:
            print("Thank you for using Python ATM")
            break
else: 
    print("Invalid")