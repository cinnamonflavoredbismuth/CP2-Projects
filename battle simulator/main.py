#Cecily Strong Battle Simulator
from battle import fakemon
from battle import main as fight
from char_handling import *
from helper_functions import *

def new_game():
    input("hello, I am dr. Tree, the valleys one and only reputable professor (press enter to continue text)")
    name=input("what is your name?\n")
    txt=["you have just reached the ripe old age of ten, you know what that means?","you own a monster and get to fend for yourself on your own!","isn't that fun?","now, as for your monster, you were here first! so you get to choose"]
    print_lots(txt)
    def check():
        print("do you want a:")
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
    txt=["now, since you are 10, you suck at basically everything","but don't worry!","your fakemon does too!","you start at level 0 for most everything"]
    print_lots(txt)
    character={'name':name,'xp':0,'lvl':1,'fakemon':fakemon,'hp':5,'str':0,'def':1,'spd':1}
    print(f"name: {character['name']}, lvl: {character['lvl']}, xp: {character['xp']}, fakemon: {character['fakemon']}, hp: {character['hp']}, str: {character['str']}, def: {character['def']}, spd: {character['spd']}")
    txt=["but do not fret!","you can still level up by battling!","Well, thats it for me"]
    print_lots(txt)
    
    return character



def main(fakemon):
    print("FAKEMON: THE GAME\n")
    print("would you like to:")
    options(["new character","single player","two player","see all players","see chart for character stats","statistical anylysis for your character", "statistical analysis of all characters","Exit"])
    try:
        choose=int(input())
        if choose == 1: #new character
            new_char(new_game())
            main(fakemon)
        elif choose == 2: #single player
            p1=export_char(input("what is the name of your character?\n"))
            if p1==False: 
                print("your character is not in the list, make a new one?")
                main(fakemon)
            else:
                bot=random_char()
                fight(p1,bot,p1,bot,fakemon,False,True)
                main(fakemon)
        elif choose == 3: #two player
            p1=export_char(input("what is the name of your character?\n"))
            if p1==False: 
                print("your character is not in the list, make a new one?")
                main(fakemon)
            else:
                p2=export_char(input("what is the name of your character?\n"))
                if p2==False: 
                    print("your character is not in the list, make a new one?")
                    main(fakemon)
                else:
                    fight(p1,p2,p1,p2,fakemon,False,False)
                    main(fakemon)
        elif choose == 4: #see all players
            input(frame_chars())
            main(fakemon)
        elif choose == 5: #graph
            p=export_char(input("what is the name of your character?\n"))
            if p==False: 
                print("your character is not in the list, make a new one?")
                main(fakemon)
            else:
                chart(p)
                main(fakemon)
        elif choose == 6: #statisical anylisis
            p=export_char(input("what is the name of your character?\n"))
            if p==False: 
                print("your character is not in the list, make a new one?")
                main(fakemon)
            else:
                input(mmm_char(p))
                main(fakemon)
        elif choose == 7: #all characters statistics
            input(frame_mmm())
            main(fakemon)
        elif choose == 8: #exit
            return
        else: 
            print('not one of the listed options [ERROR with MAIN]') 
            main(fakemon)
    except:
        print("thats not a number [ERROR with MAIN]")
        main(fakemon)

main(fakemon)