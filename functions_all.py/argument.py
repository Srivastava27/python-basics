#tuple

def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is : ", sum/len(numbers))

average(6,7)
average(6,7,9)
average(6,7,8,5,4)