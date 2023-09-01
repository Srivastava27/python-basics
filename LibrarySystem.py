# Library Management

lib={
    "BTech":["Signals","Networking","cloud","Cyber"],
    "BCA":["Python","Java","Data warehouse"],
    "BSc":["Physics","Chemistry","biology"]
}

branch=input("Enter your branch(BTech,BCA,BSc): ")
print(" ")


if branch=="BTech" in lib.keys():
    print("Books available are : " ,lib["BTech"])

if branch=="BCA" in lib.keys():
    print("Books available are : " ,lib["BCA"])

if branch=="BSc" in lib.keys():
    print("Books available are : " ,lib["BSc"])
print(" ")

book=input("Enter the name of the book: ")

print(" ")

print("OHK ! Issuing your book")

print(" ")

name=input("Enter your name: ")

print(" ")

date=int(input("Enter today's date: "))
month=int(input("Enter the current month(in numbers): "))
year=int(input("Enter current year: "))

print(" ")

print("Your Details : ")
print(" ")
print("Name: ", name)
print(" ")
print("Book name: ", book)
print(" ")
print("Issuing Date:  ",date,"-",month,"-",year)

print(" ")

if date==30 or date==31:
    print("Return Date: ",14,"-",month+1,"-",year)
elif date==1:
    print("Return Date: ",date+13,"-",month,"-",year)
elif date<30 or date<31:
    print("Please return the book after 14 days")
else:
    print("return the book after 14 days")

print(" ")

print("If someone failed to return the book in 14 days , fine of 10/- per day will be charged")