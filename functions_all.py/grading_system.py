# Grading system using functions


def system(a):
    if(a>=90 and a<=100):
        print("A")
    elif(a>=80 and a<90):
        print("B")
    elif(a>=70 and a<80):
        print("C")
    else:
        print("D")


a=int(input("enter your percentage: "))
system(a)