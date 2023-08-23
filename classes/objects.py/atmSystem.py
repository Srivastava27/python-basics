# Atm machine using classes and objects
class atmSystem:

    def __init__(self):
        self.account=int(input("Enter your account number: "))
        self.pin=int(input("Enter your pin number: "))
        self.name=input("Enter your Name: ")


    def checking(self):
        account_no=123456789
        pin=9876
        name="Vanshika"

        if self.account==account_no and self.pin==pin and self.name==name:
            print("OHK ! you can proceed further")
        else:
            print("your details are wrong")

    def details(self):

        amount=60000

        print("Amount in your account: ",amount)


        a=input("Press d for deposit and w for withdraw: ")
        if a=="w":
            x=int(input("Enter the amount you want to withdraw: "))
            print("Balance amount: ",amount-x)
        elif a=="d":
            y=int(input("Enter the amount you want to deposit: "))
            print("Balance amount: ",amount+y)
        else:
            print("Try again")





obj=atmSystem()
obj.checking()
obj.details()

