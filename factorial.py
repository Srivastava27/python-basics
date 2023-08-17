# factorial series

num=int(input("enter a number: "))
fact=1
if(num<0):
    print("factorial doesn't exist")
elif(num==0 or num==1):
    print("factorial is", 1)
else:
    for x in range(1,num+1,1):
        fact=fact*x
    print(fact)