#Cecily Strong Battle Simulator
"""Character Creation and Management:

Create new characters with attributes (name, health, strength, defense, speed)
Save characters to a CSV file
Load characters from a CSV file
Display character information

Battle System:

Implement a turn-based battle system between two characters
Calculate damage based on character attributes
Include a simple leveling system where characters gain experience after battles

Program Structure:

Use inner functions for main features (character creation, battle system, menu)
Implement helper functions for repetitive tasks (save/load, display character info)
Create a main menu for user interaction

File Operations:

Save character data to a CSV file
Load character data from a CSV file

Additional Features (Optional): (NOTE: only awarded IF all 20 of the required points are earned, they cannot make up for lost points)

Implement character classes (warrior, mage, rogue) with unique attributes 
Implementation of basic character classes (e.g. warrior, mage, rouge) with slight variations in starting attributes (1 point)
Implement character classes with unique abilities or skills (2 points)

Add a simple inventory system 
Allow characters to hold items (1 point)
Inventory with equippable items that affect character stats (2 points)
Advanced inventory system with item crafting or combining (3 points)

Create special abilities for characters
Implement one or two special abelites for characters (1 point)
Implement a diverse set of special abilities that significantly impact battles (2 points)

Enhanced Battle System
Add status effects (e.g. poison, stun, frozen) to the battle system
Implement a more complex battle system with multiple characters per side (3 points)"""
from battle import fakemon
from battle import main as fight
from char_handling import new_char
from char_handling import edit_char
from char_handling import export_char
from char_handling import display_chars
from helper_functions import options



def main_menu():
    print("would you like to:")
    options(["load game","start new game","see all players"])
    try:
        choose=int(input())
        if choose == 1:
            name=input("what is the name of your character?")
            player=export_char(name)
            if player==False: 
                print("your character is not in the list, make a new one?")
                main_menu()
        elif choose == 2:
            new_game()
        elif choose == 3:
            display_chars()
        else: print('not one of the listed options')

    except:
        print("thats not a number")
        main_menu()
def game():
    pass
def new_game():
    print("hello, I am dr. Tree, the valleys one and only reputable professor")
    name=input("what is your name?")
    print("you have just reached the ripe old age of ten, you know what that means?")
    print("you get a monster and get to fend for yourself on your own!")
    print("isn't that fun?")
    print("now, as for your monster, you were here first! so you get to choose")
    print("do you want a:")
    options(['satan','george w bush','fish'])
    try:
        choice=int(input())
        if choice==1:
            fakemon='satan'
        elif choice==2:
            fakemon='george w bush'
        elif choice==3:
            fakemon='fish'
        elif choice==4:
            print("wow, you really do think you're the main character, huh")
            print("well, you're right!")
            print("you get pikachu!")
            fakemon='pikachu'
        else: print("not an option, buddy")
    except: print('thats not even a number, dumbass')
    print("now, since you are 10, you suck at basically everything")
    print("but don't worry!")
    print("your fakemon does too!")
    print("you start at level 0 for basically everything")
    character={'name':name,'xp':0,'lvl':0,'fakemon':fakemon,'hp':5,'str':0,'def':1,'spd':1}
    print("but do not fret!")
    print("you can still ")