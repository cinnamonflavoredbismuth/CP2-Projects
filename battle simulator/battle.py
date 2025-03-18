#Cecily Strong Battle Simulator Level Handling
from helper_functions import options
from char_handling import edit_char
from char_handling import random_char
import random
char1=random_char()
char2=random_char()


#print(char1)
#1.2 leveling up multiplier

fakemon={
    'satan':{'type': 'fire',
            'weakness':'water',
            'attacks':{
                 'antichrist':2,
                 'gay people':3},
            'heal':{
                'sin, cos, tan':2
            }},
    'george w bush':{'type': 'grass',
            'weakness':['fire','electric'],
            'attacks':{
                 'destroy pipeline':2,
                 'legislate':3},
            'heal':{
                'veganize':2
            }},
    'fish':{'type':'water',
            'weakness':['grass','electric'],
            'attacks':{
                 'squirt':2,
                 'BONES':3},
            'heal':{
                'hydrate':2
    
            }},
            
    'pikachu':{'type': 'electric',
            'weakness':'fire',
            'attacks':{
                 'kill god':3,
                 'copyright strike':4},
            'heal':{
                'main character syndrome':3
            }},
}

def attack(p,spd,mltp,defe,str,type):
        #turning all my friggen variables into integers because they werent already ??
        spd=int(spd) #speed
        mltp=int(mltp) #multiplier AKA level
        defe=int(defe) #defense
        #basically, this is choosing a random number between your speed +x and -x, and adding or subracting the appropriate number if your fakemon is effective to the type or weak to the type
        atk_num = random.randrange(spd-mltp,spd+mltp)+type
        landed = (mltp*(1/3))+spd #this is to check if it landed at all
        super_effective=mltp*(2/3)+spd #this is to see if its super effective!
        if atk_num < defe: #doesn't land :(
            return p['hp'],"it did not land!"
        elif atk_num >= defe:
            if atk_num < landed: #didnt land
                p['hp'] = int(p['hp'])-(int(str)*(2/3)+int(type)) #subtracts the damage it dealt
                return p['hp'],'it landed!'
            elif atk_num >= super_effective: #super effective
                p['hp'] = int(p['hp'])-(int(str)*3/2+int(type)) #subtracts the damage it dealt
                return p['hp'],("it was super effective!")
            else: #normal attack
                p['hp'] = int(p['hp'])-(int(str)+int(type)) #subtracts the damage it dealt
                return p['hp'],("it was effective!")
        
def heal(char1,spd,mltp,defe,str,type):
        spd=int(spd)
        mltp=int(mltp)
        defe=int(defe)
        atk_num = random.randrange(spd-mltp,spd+mltp)+type
        landed = (mltp*(1/3))+spd
        super_effective=mltp*(2/3)+spd
        if atk_num < defe: #doesn't land :(
            return char1['hp'],"it did not work!"
        elif atk_num >= defe:
            if atk_num<landed:
                
                char1['hp']=int(char1['hp'])+(str*(2/3)+type)
                return char1['hp'],'it worked!'
            elif atk_num>=super_effective:
                char1['hp']+=(str*3/2+type)
                return char1['hp'],"it was super effective!"

            else:
                char1['hp']+=(str+type)
                return char1['hp'],"it was effective!"

def run(spd,mltp,type,p2_defe):
        spd=int(spd)
        mltp=int(mltp)
        type=int(type)
        p2_defe=int(p2_defe)
        run_num = random.randrange(spd-mltp,spd+mltp)+type
        if run_num < p2_defe:
            return False, "it did not work!"
        else:
            return True, "It worked!"

def turn(p1,p2,fakemon,bot):
    #Variable declarations because I was too lazy to convert all uses of them back when I changed the code
    attacks=list(fakemon[p1['fakemon']]['attacks'])
    attacks_stats=[]
    for x in attacks: #attack options
        attacks_stats.append(f"ATTACK: {x} (atk:{fakemon[p1['fakemon']]['attacks'][x]})")
    heals=list(fakemon[p1['fakemon']]['heal'])
    heals_stats=[]
    for x in heals: #Healing options
        heals_stats.append(f"HEAL: {x} (atk:{fakemon[p1['fakemon']]['heal'][x]})")
    choices=attacks+heals+["FLEE: run away"]+["EXIT: main menu"] #these are the attacks that the computer sees, it doesnt need to know how much damage things do, it just needs the name
    choices_stats=attacks_stats+heals_stats+["FLEE: run away"]+["EXIT: main menu"] #this is what is displayed in the fight menu screen

    if fakemon[p2['fakemon']]['type'] in fakemon[p1['fakemon']]['weakness'] :
        type = 2
    elif fakemon[p1['fakemon']]['type'] in fakemon[p2['fakemon']]['weakness']:
        type = -2
    else:
        type=0

    if bot==True: #is the player a bot? Its more likely than you think
            x==random.randint(1,len(choices)-1) #pick a random choice! it might not be staregically the best but bots don't care
    else:
        options(choices_stats)
        try:
            x = int(input(''))
        except:print('not an integer')

    if choices[x-1] in attacks: #this is the attack that it does!
        str=int(char1['str'])+int(fakemon[p1['fakemon']]['attacks'][attacks[attacks.index(choices[x-1])]]) #this is how much strength each fakemon has for the attack. basically base damage
        input(f"{p1['fakemon']} used {choices[x-1]}!") #displays that the fakemon did an attack
        list1 = attack(p2,p1['spd'],p1['lvl'],p1['def'],str,type) 
        input(list1[1])#message of effectiveness
        p2['hp']=list1[0] #changes hp
        return p2

    elif choices[x-1] in heals:
        str=int(char1['str'])+int(fakemon[p1['fakemon']]['heal'][heals[heals.index(choices[x-1])]]) #base heals for pokemon
        input(f"{p1['fakemon']} used {choices[x-1]}!") #displays that the fakemon did a thing
        list1 = heal(p1,p1['spd'],p1['lvl'],p1['def'],str,type) 
        input(list1[1])#message of effectiveness
        p1['hp']=list1[0] #changes hp
        return p1
        
    elif choices[x-1]=="FLEE: run away":
        input(f"{p1['fakemon']} used {'run away'}!")
        list1 = run(p1['spd'],p1['lvl'],type,p2['def'])
        input(list1[1])
        run_away=list1[0] #if the thing worked, then this is how the program knows
        return run_away
        
    elif choices[x-1]=="EXIT: main menu":
        return True
        #Failsafe. maybe ill put back later
        print("are you sure you want to go to the main menu?")
        options(['yes','no'])
        leave=int(input())
        if leave==1:
            return True
        else:
            turn(p1,p2,fakemon)
    else:
        print("Not in list")
        turn(p1,p2,fakemon)

    

def level_up(p):
    p['xp']=int(p['xp'])+random.randint(1,3) #xp gathering
    
    input("what do you want to upgrade?") #upgrading individual stats
    choices=['hp','str','def','spd']
    options(choices)
    try:
        choose=int(input())
        if choose>len(choices-1) or choose<len(choices-1):
            print("invalid option")
        else:
            p[choices[choose-1]]=int(p[choices[choose-1]])+1
    except:print('not a number')    

    if int(p['xp'])==int(p['lvl'])*1.2: #leveling up
        p['xp']=0
        input(f"Your {p['fakemon']} Leveled up!")
        p['lvl']=int(p['lvl'])+1

    edit_char(p,1)
    return p

def main(p1,p2,char1,char2,fakemon,bot1,bot2): #P1 is the current player, p2 is the other player, chars 1 and 2 are just staying the same for continuity reasons (who challenged who, ect), bot1 and bot2 are used to ask if player 1 or player two are a bot. theoretically, you could have two bots against each other, or 2 in person players. wild, huh

    # Shows all player stats
    input(f"You have encountered a wild {char2['name']}!")
    input(f"""Opponent stats:
fakemon:{char2['fakemon']}
lvl: {char2['lvl']}
hp: {char2['hp']}""")
    input(f"""Your Stats:
lvl: {char1['lvl']}
hp: {char1['hp']}""")
    
    def check(p1,p2): #this just checks if any of the fakemons hp is under 0
        if int(p1['hp']) <= 0:
            p2=level_up(p2)
            p1=level_up(p1)
            return True, f"{p1['fakemon']} has fainted!"
        else: return False,''
        
    lose=[check(p1,p2)[0],check(p2,p1)[0],check(p1,p2)[1],check(p2,p1)[1]]
    if True in lose:
        print(lose[2],lose[3])
        return
    else:
        exit=turn(p1,p2,fakemon,bot1,bot2) #actual fight function
        if exit==True: #this is just to be safe
            return 
        else:
            main(p2,p1,char1,char2,fakemon,bot2,bot1) #runs program again

#main(char1,char2,char1,char2,fakemon,False,True) #testing function