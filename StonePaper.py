
'''print("Rules are : ")
print("siccor = 0")
print("stone = 1")
print("paper = 2")
pl1 = int(input("p1 choice : "))
pl2 = int(input("p2 choice : "))

if(pl1==0 and pl2==1):
    print("pl2 is winner ")
elif(pl1==1 and pl2==2):
    print("pl2 is winner ")
elif(pl1==2 and pl2==0):
    print("pl2 is winner ")
else:
    print("p1 wins ")'''


# print("stone / paper / scissor")
# print("rules: ")
# print("scissor=0")
# print("stone=1")
# print("paper=2")

# pl1=int(input("p1 turn: "))
# pl2=int(input("p2 turn: "))

# if(pl1==0 and pl2==1):
#     print("pl2 wins ", pl2 )
# elif(pl1==1 and pl2==2):
#     print("pl2 wins")
# elif(pl1==2 and pl2==0):
#     print("pl2 wins")
# elif(pl1==pl2):
#     print("draw")
# else:
#     print("pl1 wins")




print("stone / paper / scissor")
print("rules: ")
print("scissor=0")
print("stone=1")
print("paper=2")
print('\n')

pl1 = int(input("p1 turn: "))
pl2 = int(input("p2 turn: "))
print('\n')


if(pl1==0):
    print("p1 choise is scissor")
elif(pl1==1):
    print("p1 choise is stone")
elif(pl1==2):
    print("p1 choise is paper")

if(pl2==0):
    print("pl2 choise is scissor")
elif(pl2==1):
    print("pl2 choise is stone")
elif(pl2==2):
    print("pl2 choise is paper")

print('\n')

if(pl1==0 and pl2==1):
    print("pl2 wins")
elif(pl1==1 and pl2==2):
    print("pl2 wins")
elif(pl1==2 and pl2==0):
    print("pl2 wins")
elif(pl1==pl2):
    print("draw")
else:
    print("pl1 wins" , pl1)


