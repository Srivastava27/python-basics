# restaurant


rest={
    "noodles":150,
    "burger":50,
    "momos":60,
    "paneer":150,
    "kofta":120,
    "dal":100,
    "roti":10,
    "parantha":20

}

print("Order your delicious food ! here's our menu: ")



for i,j in rest.items():
    print(i,": ",j,"/-")


item=input("Enter the item you want to order: ")
item2=input("Anything else you want: ")

if item=="noodles" and item2=="no":
    print("your bill is: ",rest["noodles"])
elif item=="burger" and item2=="no":
    print("your bill is: ",rest["burger"])
elif item=="momos" and item2=="no":
    print("your bill is: ",rest["momos"])
elif item=="paneer" and item2=="no":
    print("your bill is: ",rest["paneer"])
elif item=="kofta" and item2=="no":
    print("your bill is: ",rest["kofta"])
elif item=="dal" and item2=="no":
    print("your bill is: ",rest["dal"])
elif item=="roti" and item2=="no":
    print("your bill is: ",rest["roti"])
elif item=="parantha" and item2=="no":
    print("your bill is: ",rest["parantha"])
else:
    print("your bill is: ",rest[item]+rest[item2])





print("ohk your order will be ready in just 10 min... Kindly wait")


























