# Library Management

lib={
    "BTech":["Signals","Networking","cloud","Cyber"],
    "BCA":["Python","Java","Data warehouse"],
    "BSc":["Physics","Chemistry","biology"]
}

branch=input("Enter your branch: ")


if branch=="BTech" in lib.keys():
    print("Books available are : " ,lib["BTech"])

if branch=="BCA" in lib.keys():
    print("Books available are : " ,lib["BCA"])

if branch=="BSc" in lib.keys():
    print("Books available are : " ,lib["BSc"])

book=input("Enter the name of the book: ")

print("OHK ! Issuing your book")

name=input("Enter your name: ")

date=int(input("Enter today's date: "))
month=int(input("Enter the current month(in numbers): "))
year=int(input("Enter current year: "))



print("Your Details : ")
print("Name: ", name)
print("Book name: ", book)
print("Issuing Date:  ",date,"-",month,"-",year)
