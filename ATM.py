print("         The Bank Of India")
customers = [[10001,"Dhayananth",1500,3207],[10002,"Kuberan",2000,3075],
             [10003,"Sriraman",2000,3155],[10004,"Vasanth",1000,3167],
             [10005,"Balasakthi",3000,3019],[10006,"Chandru",2500,3025]]

def deposit(AccNumber):
    amount = int(input("    Enter Deposit Amount : "))
    for customer in customers:
        if customer[0] == AccNumber:
            Old_Balance = customer[2]
            New_Balance = Old_Balance + amount
            customer[2] = New_Balance
            print("\n\tAmount Deposited\n\tBalance : ",New_Balance,"\n\n")
        
def withdraw(AccNumber):
    amount = int(input("    Enter Withdrawl Amount : "))
    for customer in customers:
        if customer[0] == AccNumber:
            Old_Balance = customer[2]
            New_Balance = Old_Balance - amount
            customer[2] = New_Balance
            print("\n\tAmount Withdrawed\n\tBalance : ",New_Balance,"\n\n")

def pinchange(AccNumber):
    value=0
    old=input("    Enter Old Password : ")
    x = len(old)
    if x == 4:
        for pin in customers:
            if pin[3] == int(old):
                value=1
                new = int(input("    Enter New Password : "))
                pin[3] = new
                print("    Password Changed")
        if value == 0:
            print("    Incorrect Password")
    else:
        print("    Pin Number Should be 4-Digit") 
        
def balance(AccNumber):
    for customer in customers:
        if customer[0] == AccNumber:
            print("\n    Name    : ",customer[1])
            print("    Balance : ",customer[2])    
chance = 3
found=0
while True:
    print("="*40)
    AccNumber = int(input("    Enter Your Account Number : "))
    for customer in customers :
        if customer[0] == AccNumber:
            found=1
            while True :
                pin = int(input("    Enter Pin Number : "))
                if customer[3] == pin:
                    print("-"*40)
                    print("\t1.Withdraw\n\t2.Deposit\n\t3.Balance\n\t4.Pin Change\n\t5.Exit")
                    option=input("    Select The Program : ")
                    if option.upper() == "EXIT" or option == "5":
                        break
                    elif option == "1":
                        withdraw(AccNumber)
                        break
                    elif option == "2":
                        deposit(AccNumber)
                        break
                    elif option == "3":
                        balance(AccNumber)
                        break
                    elif option == "4":
                        pinchange(AccNumber)
                        break
                    else:
                        print("    Select the Appropriate Option")
                else:
                        chance -= 1
                        print("    Incorrect Password, Try Again ")
                
                if chance == 0:
                    print("    Maximum Chances Exceed, Try Tomorrow ")
                    break
                    
        if found == 0:
            print("    CUSTOMER NOT FOUND")


