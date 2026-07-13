'''-----------------------ATM BILLING SYSTEM USING MULTIPLE USERS-----------------------'''
users={"Kashish":{"password":1234,"balance":1000},
"Ekam":{"password":1234,"balance":2000},
"Sakshi":{"password":1234,"balance":500},
"Neha":{"password":1234,"balance":30000
}
}
name=(input("Enter your Username:"))
if name in users:
    pswd=int(input("Enter Password:"))
    if users[name]["password"]==pswd:
        print("--------OPTIONS---------\n 1.Check Balance \n 2.Deposit \n 3.Withdrawl \n 4.EXIT")
        while True:
            choice=int(input("Enter Your Choice(1-4) : "))
            if (choice==1):
                print("Current Balance:",users[name]["balance"])
            elif(choice==2):
                deposit=int(input("Enter Your Amount To Deposit:"))
                users[name]["balance"]+=deposit
                print("After Deposit",users[name]["balance"])
            elif(choice==3): 
                withdrwal=int(input("Enter Your Amount for Withdrawl:"))
                if (users[name]["balance"]>withdrwal):
                    users[name]["balance"]-=withdrwal
                    print("After Withdrwal Current Balance:",users[name]["balance"])
                else:
                    print("Not Sufficient Balance")
            elif(choice==4):
                exit()
            else:
                print("Enter Valid Choice(1-4)")
                break
    else:
        print("Invalid Password")
else:
    print("Invalid Username")
