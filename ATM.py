print("    The bank Of India    ")
customers=[["dhaya",1500],["aswin",2000]]
cus_name=["aswin","dhaya"]

def deposit():
    Name=input("Enter Customer Name : ")
    if Name in cus_name:
        amount=int(input("Enter Deposit Amount : "))
        for cus in customers:
            for name in cus:
                   if name==Name:
                       x=customers.index(name)
                       return x
        Bal=customers[x][1]
        Bal=Bal+amount
        customers[x][1]=Bal
        printf("Aount Withdrawed") 
    else:
        print("Customer Not Found")
        
def withdraw():
    print("***Withdraw***")
    
def balance():
    print("***Balance***")
    
while True:
    print("\n\t1.Withdraw\n\t2.Deposit\n\t3.Balance\n\t4.Exit")
    option=input("Select The Program : ")
    if option.upper()=="EXIT" or option=="4":
        break
    elif option=="1":
        withdraw()
    elif option=="2":
        deposit()
    elif option=="3":
        balance()
    else:
        print("Select the Appropriate Option")


