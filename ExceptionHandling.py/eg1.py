# try:
#     num=int(input("enter a number: "))
#     res=10/num
#     print("result: ",res)
# except:
#     print("Enter a valid number")


# Email validation


# gmail="@gmail.com"
# space=" "
# email=input("Enter the email: ")
# if gmail not in email:
#     raise NameError("Can't sign in , Invalid format")
# elif space in email:
#     raise TabError("space is not allowed")
# elif gmail==email:
#     raise NameError("Can't sign in , Invalid format")
# else:
#     print("you are signed in as : ",email)


import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

# Test the email validation function
email_input = input("Enter an email address: ")
if is_valid_email(email_input):
    print("Valid email")
else:
    print("Invalid email")


# str=""
# list=["0","1","2","3","4","5","6","7","8","9","@",""]

# print(str[0]==list[1])
# for i in list:
#     # print(i)
#     if str[0]==i:
#         print("invalid")
#         break;
# if(str[0]==list):
#     print("Valid")
# else:
#     print("Invalid")

# try:
#     if(str[0]!="@" or str[0]!=list)



# try: 
    
#     num1=input("Enter your email: ")
    # email="a","b","c","d","1","2"
    # domain="@gmail.com"
    # at=int("@")
    # dot="."

    # if email and domain in num1:    
    # if (num1==str,"@","gmail" or "Yahoo",".","com"):
    # if "@" and "." and "com" in num1:
    # if at>0 and dot>at+1 and dot<len(num1):
        # print("Valid email")
    # else:
    #     raise ValueError("negative numbers cannot be used")

# except:
#     print("Invalid Format")


# Atm System

# num1=int(input("Enter your account no: "))
# num2=int(input("enter your PIN: "))
# acc=123456789
# pin=3360
# acc=123456789
# pin=3360
# if(num1==acc):
#     print("you can proceed further")
# elif(num2==pin):
#     print("you can proceed further")
# else:
#     print("your verification failed")



# amount=60000

# print("Amount in your account: ",amount)


# a=input("Press d for deposit and w for withdraw: ")
# if a=="w":
#     x=int(input("Enter the amount you want to withdraw: "))
#     print("Balance amount: ",amount-x)
# elif a=="d":
#     y=int(input("Enter the amount you want to deposit: "))
#     print("Balance amount: ",amount+y)
# else:
#     print("Try again")


