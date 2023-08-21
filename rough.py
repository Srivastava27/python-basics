# tup=(1,2,3,"Vanshika",True)

# print(tup)
# print(type(tup))


# print(tup[4])
# print(tup[:])
# print(tup[1:4])


# temp=list(tup)
# print(temp)


# temp.pop(1)
# print(temp)


# temp.append(7)
# print(temp)


# print(temp.index("Vanshika"))

# print(temp.count("Vanshika"))

# if "ansh" in "Vanshika":
#     print("yes")





# sets

# set={1,5,7,True,"Vanshu"}
# s2={3,6,8}

# print(set)
# print(type(set))

# set.update(s2)
# print(set)



# dictionary


# dict={
#     "value1":"Vanshika",
#     "value2":"srivastava",
#     1:"age",
#     2:"gender"
# }
# print(dict)
# print(type(dict))

# print(dict["value1"])
# print(dict["value2"])
# print(dict[1])
# print(dict[2])

# print(dict.items())
# print(dict.keys())
# print(dict.values())

# for i in dict.keys():
#     print(dict[i])

# for i , j in dict.items():
#     print(i,j)




# Library Management

lib={
    "BTech":["Signals","Networking","cloud","Cyber"],
    "BCA":["Python","Java","Data warehouse"],
    "BSc":["Physics","Chemistry","biology"]
}

branch=input("Enter your branch: ")

# Btech=lib.keys()
# print(lib["BTech"])

for i in lib.values():
    print(i)


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











