#fibonacci series

# num=int(input("enter any number: "))
# x=0
# if(num<=0):
#     print("no series exist")
# elif(num==1 or num==2):
#     print("series will be" , 1)
# else:
#     for i in range(3,num,1):
#         x=(
#     print(x)

n=10
a,b=0,1

count=0
while(count<=10):
    print(a,end=" ")
    next_fib=a+b
    a,b=b,next_fib
    count=count+1
