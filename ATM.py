print("         The Bank Of India")
customers = [[10001,"dhaya",1500,3207],[10002,"kuberan",2000,3075]]

def deposit(AccNumber):
    amount = int(input("    Enter Deposit Amount : "))
    for customer in customers:
        if customer[0] == AccNumber:
            Old_Balance = customer[2]
            New_Balance = Old_Balance + amount
            customer[2] = New_Balance
            print("\n\tAmount Deposited\n\tBalance : ",New_Balance,"\n\n")
        
def withdraw(AccNumber):
    print("***Withdraw***")
    
def balance(AccNumber):
    print("***Withdraw***")
    
chance = 3
found=0
while True:
    print("="*40)
    AccNumber = int(input("    Enter Your Account Number : "))
    for customer in customers :
        if customer[0] == AccNumber:
            found=1
            while chance <=3 :
                pin = int(input("    Enter Pin Number : "))
                chance -= 1
                if chance == 0:
                    print("    Maximum Chances Exceed, Try Tomorrow ")
                    break
                else:
                    if customer[3] == pin:
                        print("-"*40)
                        print("\t1.Withdraw\n\t2.Deposit\n\t3.Balance\n\t4.Exit")
                        option=input("    Select The Program : ")
                        if option.upper() == "EXIT" or option == "4":
                            break
                        elif option == "1":
                            withdraw(AccNumber)
                        elif option == "2":
                            deposit(AccNumber)
                        elif option == "3":
                            balance(AccNumber)
                        else:
                            print("    Select the Appropriate Option")
                    else:
                        print("    Incorrect Password, Try Again ")
        if found == 0:
            print("    CUSTOMER NOT FOUND")


