#Cecily Strong Battle Simulator Level Handling
from helper_functions import options
from char_handling import export_chars
import random

loaded_chars=export_chars()
names=list(loaded_chars.keys())

#name1=random.choice(names)
name1=names[1]
char1={"name":name1,'lvl':loaded_chars[name1]['lvl'],'xp':loaded_chars[name1]['xp'],"fakemon":loaded_chars[name1]['fakemon'],"hp":loaded_chars[name1]['hp'],"str":loaded_chars[name1]['str'],'def':loaded_chars[name1]['def'],'spd':loaded_chars[name1]['spd']}

name2=names[0]
char2={"name":name2,'lvl':loaded_chars[name2]['lvl'],'xp':loaded_chars[name2]['xp'],"fakemon":loaded_chars[name2]['fakemon'],"hp":loaded_chars[name2]['hp'],"str":loaded_chars[name2]['str'],'def':loaded_chars[name2]['def'],'spd':loaded_chars[name2]['spd']}
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

def attack(char2,spd,mltp,defe,str,type):
        #basically, this is choosing a random number between your speed +x and -x, and adding or subracting the appropriate number if your fakemon is effective to the type or weak to the type
        spd=int(spd)
        mltp=int(mltp)
        defe=int(defe)
        atk_num = random.randrange(spd-mltp,spd+mltp)+type
        landed = (mltp*(1/3))+spd
        super_effective=mltp*(2/3)+spd
        if atk_num < defe: #doesn't land :(
            return char2['hp'],"it did not land!"
        elif atk_num >= defe:
            if atk_num<landed:
                char2['hp']=int(char2['hp'])-(int(str)*(2/3)+int(type))
                return char2['hp'],'it landed!'
            elif atk_num>=super_effective:
                char2['hp']=int(char2['hp'])-(int(str)*3/2+int(type))
                return char2['hp'],("it was super effective!")
            else:
                char2['hp']=int(char2['hp'])-(int(str)+int(type))
                return char2['hp'],("it was effective!")
        
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
    attacks=list(fakemon[p1['fakemon']]['attacks'])
    attacks_stats=[]
    for x in attacks:
        attacks_stats.append(f"ATTACK: {x} (atk:{fakemon[p1['fakemon']]['attacks'][x]})")
    heals=list(fakemon[p1['fakemon']]['heal'])
    heals_stats=[]
    for x in heals:
        heals_stats.append(f"HEAL: {x} (atk:{fakemon[p1['fakemon']]['heal'][x]})")

    choices=attacks+heals+["FLEE: run away"]+["EXIT: main menu"]

    choices_stats=attacks_stats+heals_stats+["FLEE: run away"]+["EXIT: main menu"]
    if fakemon[p2['fakemon']]['type'] in fakemon[p1['fakemon']]['weakness'] :
        type = 2
    elif fakemon[p1['fakemon']]['type'] in fakemon[p2['fakemon']]['weakness']:
        type = -2
    else:
        type=0


    options(choices_stats)
    try:
        if bot==True:
            x==random.randint(1,len(choices)-1)
        else:
            x = int(input(''))
        
        if choices[x-1] in attacks:
            str=int(char1['str'])+int(fakemon[p1['fakemon']]['attacks'][attacks[attacks.index(choices[x-1])]])
            print(f"{p1['fakemon']} used {choices[x-1]}!")
            list1 = attack(p2,p1['spd'],p1['lvl'],p1['def'],str,type)
            print(list1[1])
            p2['hp']=list1[0]

        elif choices[x-1] in heals:
            str=int(char1['str'])+int(fakemon[p1['fakemon']]['heal'][heals[heals.index(choices[x-1])]])
            print(f"{p1['fakemon']} used {choices[x-1]}!")
            list1 = heal(p1,p1['spd'],p1['lvl'],p1['def'],str,type)
            print(list1[1])
            p1['hp']=list1[0]
            
        elif choices[x-1]=="FLEE: run away":
            print(f"{p1['fakemon']} used {'run away'}!")
            list1 = run(p1['spd'],p1['lvl'],type,p2['def'])
            print(list1[1])
            run_away=list1[0]
            
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
        else:print("Not in list")
        turn(p1,p2,fakemon)
    except:print('not an integer')
    turn(p1,p2,fakemon)

def level_up(p):
    p['xp']=int(p['xp'])+random.randint(1,3) #xp gathering

    print("what do you want to upgrade?") #upgrading individual stats
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
        print(f"Your {p['fakemon']} Leveled up!")
        p['lvl']=int(p['lvl'])+1
    
    return p

def main(p1,p2,char1,char2,fakemon,bot1,bot2):
    print(f"You have encountered a wild {char2['name']}!")
    print(f"""Opponent stats:
fakemon:{char2['fakemon']}
lvl: {char2['lvl']}
hp: {char2['hp']}""")
    print(f"""Your Stats:
lvl: {char1['lvl']}
hp: {char1['hp']}""")
    if int(p1['hp']) <= 0:
        print(f"your {p1['fakemon']} has fainted!")
        p2['xp']=int(p2['xp'])+random.randint(1,3)
        return p2
    elif int(p2['hp']) <= 0:
        print(f"{p2}'s {p2['fakemon']} has fainted!")
        p1=level_up(p1)
        return p1
    else:
        exit=turn(p1,p2,fakemon,bot1)
        if exit==True:
            return
        else:
            main(p2,p1,char1,char2,fakemon,bot2)

main(char1,char2,char1,char2,fakemon,False,True)