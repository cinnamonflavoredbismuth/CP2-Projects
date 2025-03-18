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
from char_handling import export_char
from char_handling import display_chars
from char_handling import random_char
from helper_functions import options

def new_game():
    input("hello, I am dr. Tree, the valleys one and only reputable professor (press enter to continue text)")
    name=input("what is your name?\n")
    input("you have just reached the ripe old age of ten, you know what that means?")
    input("you own a monster and get to fend for yourself on your own!")
    input("isn't that fun?")
    input("now, as for your monster, you were here first! so you get to choose")
    input("do you want a:")
    def check():
        options(['satan','george w bush','fish'])
        try:
            choice=int(input())
            if choice==1:
                return'satan'
                
            elif choice==2:
                return'george w bush'
            elif choice==3:
                return'fish'
            elif choice==4:
                input("wow, you really do think you're the main character, huh")
                input("well, you're right!")
                input("you get pikachu!")
                return'pikachu'
            else: input("not an option, buddy [ERROR with FAKEMON SELECTION]")
            check()
        except: input('thats not even a number [ERROR with FAKEMON SELECTION]')
        check()
    fakemon=check()
    input("now, since you are 10, you suck at basically everything")
    input("but don't worry!")
    input("your fakemon does too!")
    input("you start at level 0 for most everything")
    character={'name':name,'xp':0,'lvl':0,'fakemon':fakemon,'hp':5,'str':0,'def':1,'spd':1}
    print(f"name: {character['name']}, lvl: {character['lvl']}, xp: {character['xp']}, fakemon: {character['fakemon']}, hp: {character['hp']}, str: {character['str']}, def: {character['def']}, spd: {character['spd']}")
    input("but do not fret!")
    input("you can still level up by battling!")
    input("Well, thats it for me")
    print("bye!")
    
    return character

def main(fakemon):
    print("would you like to:")
    options(["new character","single player","two player","see all players","Exit"])
    try:
        choose=int(input())
        if choose == 1:
            new_char(new_game())
            main(fakemon)
        elif choose == 2:
            p1=export_char(input("what is the name of your character?"))
            if p1==False: 
                print("your character is not in the list, make a new one?")
                main(fakemon)
            else:
                bot=random_char()
                fight(p1,bot,p1,bot,fakemon,False,True)
                main(fakemon)
        elif choose == 2:
            p1=export_char(input("what is the name of your character?"))
            if p1==False: 
                print("your character is not in the list, make a new one?")
                main(fakemon)
            else:
                p2=export_char(input("what is the name of your character?"))
                if p2==False: 
                    print("your character is not in the list, make a new one?")
                    main(fakemon)
                else:
                    fight(p1,p2,p1,p2,fakemon,False,False)
                    main(fakemon)
        elif choose == 4:
            display_chars()
            input()
            main(fakemon)
        elif choose == 5:
            return
        else: 
            print('not one of the listed options [ERROR with MAIN]') 
            main(fakemon)
    except:
        print("thats not a number [ERROR with MAIN]")
        main(fakemon)

main(fakemon)