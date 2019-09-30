name=input("Please enter your name:")
surname=input("Please enter your surname:")
balance=float(input("Please enter your balance:"))

def atm(name , surname , balance):
    while True:
        print("Welcome" , name , surname , "\nWhat would you like to do today?")
        print("1 for Account Balance")
        print("2 for Cash Deposit")
        print("3 for cash Withdraw")
        print("0 to Quit")        
        selection=int(input("Please enter your selection:"))
        
        if selection== 1:
            print("Your Account Balance is:" , balance)
        elif selection== 2:
            Deposit=float(input("How much are you depositing:"))
            if Deposit > 0 :
                balance= balance + Deposit
                valid_deposit(Deposit)
            else :
                valid_deposit(Deposit)                
        elif selection== 3:
            withdraw=float(input("Please enter the value you want to withdraw:"))
            if withdraw > 0 and withdraw < balance :
                valid_withdrawal(balance, withdraw)
                balance= balance-withdraw
            elif balance < withdraw :
                print("There isn't enough money in you account")
            else :
                print("Please enter a valid amount")
        elif selection== 0:
            print("Thank you for using my ATM")
            return
        else :
            return
    return
#2
def valid_deposit(Deposit):
    if Deposit > 0 :
        return True
    else :
        print("Please enter a valid amount")
        return
#3
def valid_withdrawal(balance, withdraw):
    if withdraw <= balance :
        print("You will receive the following:")
        cash_given(withdraw)
        return
    else :
        print("Please enter a valid amount")
        return    
#4
def cash_given(withdraw):
    types=[200, 100, 50, 20, 10, 5, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    for i in types:
        if withdraw >= 0.0:
            t= int(withdraw//i)
            print(t , "-" , i)
            withdraw= float(withdraw - t*i)
        else :
            print("Please enter a valid amount")
            return
    return
            
print(atm(name , surname , balance))