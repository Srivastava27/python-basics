
# task 1
for i in range(1,10,2):
    print(i)

# task2
for x in range(10,81,3):
    print(x)

# task3
for x in range(80,54,-2):
    print(x)

# odd numbers
for x in range(1,20,2):
    print(x)

# even numbers
for x in range(2,20,2):
    print(x)


# tbl of any number
num=int(input("enter any number: "))
for x in range(1,11,1):
    print(num*x)


num=int(input("enter any number: "))
for x in range(1,16,1):

    if(x==11):
        break
    if(x==5):
        continue

    print(num , " * " , x , " = " , num*x)