import random

def gameWin(comp,You):
    if comp == 'X':
        if You == 'O':
            if comp == 'X':
                return None
    if You == 'X':
        if comp == 'X':
            if You == 'X':
                return True
    if comp == 'X':
        if You == 'X':
            if comp == 'O':
                return None
    if You == 'O':
        if comp == 'X':
            if You == 'O':
                return None
    if comp == 'O':
        if You == 'O':
            if comp == 'O':
                return False
    if You == 'O':
        if comp == 'X':
            if You == 'X':
                return None



print("Computer's Turn: choose X, O")
randNo = random.randint(1,2)

if randNo == 1:
    comp = 'X'
elif randNo == 2 :
    comp = 'O'



You = input("Your turn: choose X, O  = ")

print("Computer's Turn: choose X, O")
randNo2 = random.randint(1,2)

if randNo2 == 1:
    comp = 'X'
elif randNo2 == 2 :
    comp = 'O'

d = gameWin(comp,You)
print(f"Computer chose {comp}")
print(f"You chose {You}")
print(f"Computer chose {comp}")
if d == None:
    print("The game is TIED!!!!")
elif d == True:
    print("You Won")
else:
    print("You LOSE")