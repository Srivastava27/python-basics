#Simple Atm machine

def atmSystem(num1,num2=0,a=0):
    
    acc=123456789
    pin=3360
    if(num1==acc):
        print("you can proceed further")
    elif(num2==pin):
        print("you can proceed further")
    else:
        print("your verification failed")
    num2=int(input("enter your PIN: "))
    
    bal=60
    print("your total balance is : ", bal)
    
   
    a=int(input("enter your amount: "))
    if(a==60):
        print("your balance left is 0")
    elif(a<60):
        print("your balance left: ",bal-a)
    else:
        print("you don't have sufficient amount")
    

num1=int(input("enter your account number: "))
atmSystem(num1)