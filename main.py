
# Snake water and gun game
import random


def game(comp, User):
    if comp == User:
        print("Draw, both chossed same!!")
    elif comp == 's':
        if User == 'w':
            print("Snake driked water, Comp Win!!")
        elif User == 'g':
            print("You Killed Snake, Win!!")
    elif comp == 'w':
        if User == 's':
            print("Snake driked water,You Win!!")
        elif User == 'g':
            print("Gun Sinked in Water,Comp Win!!")
    elif comp == 'g':
        if User == 's':
            print("You were killed, Comp Win!!")
        elif User == 'w':
            print("Gun Sinked in Water,You Win!!")


randNo = random.randint(1, 3)  # between 1-3 numbers will be generated
print("Comp Turn: Snake(s) Water(w) or Gun(g)?: ")
if randNo == 0:
    comp = 's'
elif randNo == 1:
    comp = 'w'
elif randNo == 2:
    comp = 'g'

User = input("Your's Turn: Snake(s) Water(w) or Gun(g)?: ")

print(f"You choosed: {User}\n")
print(f"Comp choosed: {comp}\n")
game(comp, User)
