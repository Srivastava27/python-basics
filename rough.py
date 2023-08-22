# Library Management

# lib={
#     "BTech":["Signals","Networking","cloud","Cyber"],
#     "BCA":["Python","Java","Data warehouse"],
#     "BSc":["Physics","Chemistry","biology"]
# }

# branch=input("Enter your branch: ")

# # for key,value in lib.items():    #dont use
# #     print(key,value)

# if branch=="BTech" in lib.keys():
#     print("Books available are : " ,lib["BTech"])

# if branch=="BCA" in lib.keys():
#     print("Books available are : " ,lib["BCA"])

# if branch=="BSc" in lib.keys():
#     print("Books available are : " ,lib["BSc"])

# book=input("Enter the name of the book: ")

# print("OHK ! Issuing your book")

# name=input("Enter your name: ")

# date=int(input("Enter today's date: "))
# month=int(input("Enter the current month(in numbers): "))
# year=int(input("Enter current year: "))



# print("Your Details : ")
# print("Name: ", name)
# print("Book name: ", book)
# print("Issuing Date:  ",date,"-",month,"-",year)




# shoe analysis

shoe={
    6:6,
    7:10,
    8:12,
    9:4,
    10:14,
}


size=int(input("Enter the size of the shoes: "))


if size==6 in shoe.keys():
    print("Available number of packs are: ",shoe[6])

if size==7 in shoe.keys():
    print("Available number of packs are: ",shoe[7])

if size==8 in shoe.keys():
    print("Available number of packs are: ",shoe[8])

if size==9 in shoe.keys():
    print("Available number of packs are: ",shoe[9])

if size==10 in shoe.keys():
    print("Available number of packs are: ",shoe[10])



cust_order=int(input("Enter the number of packs you want to order: "))


# for size 6

# if cust_order<=shoe[6]:
#     print("Now the packs left for size 6: ",6-cust_order)

# if cust_order>shoe[6]:
#     print("We are not having sufficient stock")


# for size 7


# if cust_order<=shoe[7]:
#     print("Now the packs left for size 7: ",10-cust_order)

# if cust_order>shoe[7]:
#     print("We are not having sufficient stock")


# for size 8


# if cust_order<=shoe[8]:
#     print("Now the packs left for size 8: ",12-cust_order)

# if cust_order>shoe[8]:
#     print("We are not having sufficient stock")


# for size 9


# if cust_order<=shoe[9]:
#     print("Now the packs left for size 9: ",4-cust_order)

# if cust_order>shoe[9]:
#     print("We are not having sufficient stock")


# for size 10


# if cust_order<=shoe[10]:
#     print("Now the packs left for size 10: ",14-cust_order)

# if cust_order>shoe[10]:
#     print("We are not having sufficient stock")


if cust_order<=shoe[6] in shoe.keys():
    print("Stock left for size 6: ",6-cust_order)
elif cust_order<=shoe[7] in shoe.keys():
    print("Stock left for size 7: ",10-cust_order)
elif cust_order<=shoe[8] in shoe.keys():
    print("Stock left for size 8: ",12-cust_order)
elif cust_order<=size[9] in shoe.keys():
    print("Stock left for size 9: ",4-cust_order)
elif cust_order<=size[10] in shoe.keys():
    print("Stock left for size 10: ",14-cust_order)
else:
    print("We don't have sufficient stock")

print("Thank you , visit again!")





















