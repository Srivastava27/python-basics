# Library Management

lib={
    "BTech":["Signals","Networking","cloud","Cyber"],
    "BCA":["Python","Java","Data warehouse"],
    "BSc":["Physics","Chemistry","biology"]
}

branch=input("Enter your branch: ")

# Btech=lib.keys()
# print(lib["BTech"])

# for i in lib.values():
#     print(i)


if branch=="BTech" in lib.keys():
    print("Books available are : " ,lib["BTech"])

if branch=="BCA" in lib.keys():
    print("Books available are : " ,lib["BCA"])

if branch=="BSc" in lib.keys():
    print("Books available are : " ,lib["BSc"])

book=input("Enter the name of the book: ")

print("OHK ! Issuing your book")

name=input("Enter your name: ")

date=21
month=8
year=2023



print("Your Details : ")
print("Name: ", name)
print("Book name: ", book)
print("Issuing Date:  ",date,"-",month,"-",year)
# print("Return date: ",date+7,"-",month,"-",year)











