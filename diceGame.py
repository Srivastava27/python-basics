# Simple dice game with two players


print("choose number between 1 - 6")
pl1=int(input("pl1 turn: "))
pl2=int(input("pl2 turn: "))

if(pl1==6 and pl2==6):
    print("Game draw both players got: ", pl1)
elif(pl1>pl2):
    print("pl1 is winner by getting : ", pl1)
elif(pl2>pl1):
    print("pl2 is winner by getting: ", pl2)
else:
    print("No game plz m tired")

