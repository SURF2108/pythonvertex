'''
WAP ,based on a custom map, to create a treasure hunt game
where the player's each move is enquired for movement,
and at the end of the journey, three doors are presented out of which, 
one is to be chosen to get the treasure.

if even a single step is incorrect, GAME OVER
'''
import random

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

p = ['l','r']
reach_doors = 0
b = list()
for i in range(5):
    b.append(random.choice(p))
print(b)
p1 = input('Enter a move as left(l) or right(r): ')
if p1 == b[0]:
    p2 = input('Fantastic! Enter your next move as left(l) or right(r): ')
    if p2 == b[1]:
        p3 = input('Excellent! Enter your next move as left(l) or right(r): ')
        if p3 == b[2]:
            p4 = input('Marvellous! Enter your next move as left(l) or right(r): ')
            if p4==b[3]:
                p5 = input('Splendid! Enter your next move as left(l) or right(r): ')
                if p5==b[4]:
                    print("Amazing!")
                    reach_doors = 1
                else:
                    print("YOU LOSE >_<")
            else:
                    print("YOU LOSE >_<")
        else:
                    print("YOU LOSE >_<")
    else:
                    print("YOU LOSE >_<")
else:
                    print("YOU LOSE >_<")

if reach_doors == 1:
    print("You have reached the final level of this game\n")
    f = random.choice([1,2,3])
    print(f)
    d = int(input('''There are three doors in front of you:
1.Left
2.Middle
3.Right

Select a door according to its index: '''))

    if d == f:
        print("You Win!!!! UwU")
    else:
        print("You Lose........-_-")