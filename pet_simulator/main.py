#Cecily Strong Pet Simulator
"""
Class Implementation:
    Create a Pet class with attributes such as name, species, age, hunger, happiness, and energy
    Implement methods for feeding, playing, and putting the pet to sleep
    Include a method to check and display the pet's status
Pet Interactions:
    Develop a system where each action (feeding, playing, sleeping) affects multiple attributes
    Implement a time system where each action advances time
    Create different food types that affect hunger and happiness differently
User Interface:
    Design a text-based menu for interacting with pets
    Allow users to create multiple pets and switch between them
    Include options to perform various actions with the selected pet
Game Logic:
    Implement a health attribute that changes based on how well the pet is cared for
    Create events that occur randomly (e.g., pet gets sick, finds a toy)
    Add a leveling system where pets can learn new skills as they grow
Data Management:
    Implement a simple save/load system to store pet data between sessions
"""
import random
import csv

#Helpers
def int_input(msg): #has you choose until you use an integer
    while True:
        try:
            output=int(input(msg))
            break
        except ValueError:
            input("Invalid Input, please use integers")
    return output

def print_list(list):
    for x in list:
        print(f"{list.index(x)}: {x}")


#Classes (for accounts, items, player, ect)
class pet:
    def __init__(self,name,species,age,hunger,happiness,energy,skills,time):
        self.name=name
        self.species=species
        self.age=str(age)
        self.hunger=str(hunger)
        self.happiness=str(happiness)
        self.energy=str(energy)
        self.time=str(time)
        self.skills=skills
    def __str__(self):
        print(f"""    {self.name}
        Species: {self.species}
        Age: {self.age} day(s)
        Hunger: {self.hunger}
        Happiness: {self.happiness}
        Energy: {self.energy}
        Time: {self.time}""")
        print("        Skills:")
        try:
            for x in self.skills:
                print(f"           {x}")
        except: print(self.skills)

        return '' 
    def time_up(self,number):
        self.hunger=int(self.hunger)-number
        self.energy=int(self.energy)-number
        self.happiness=int(self.happiness)-number
        self.time=int(self.time)+number
    def skill_up(self):
        skill_options=['Fetch','Hunt a rat','eat trash','Grab the mail','Lick your shoes','Use the toilet like a human','Write a manuscript','Memorize To Be or Not To Be','Speak','Roll over','Stare at ghosts in the corner']
        item=random.choice(skill_options)
        self.skills.append(item)
        skill_options.remove(item)
    def default(self):
        self.age=0
        self.hunger=20
        self.happiness=20
        self.energy=20
        self.skills=['']
        self.skill_up()
        self.time=0
    def feed(self,food):
        self.hunger=int(self.hunger)+int(food.level)
        self.happiness=int(self.happiness)+int(food.happiness)
        self.time_up(1)
    def play(self,toy):
        self.energy=int(self.energy)-1
        self.happiness=int(self.happiness)+int(toy.level)
        self.hunger=int(self.hunger)-1
        self.time_up(1)
    def sleep(self,bed):
        self.energy=int(self.energy)+int(bed.level)
        self.age=int(self.age)+1
        self.time_up(5)

    def export(self):
        skills='/'.join(self.skills)
        return f"{self.name}-{self.species}-{self.age}-{self.hunger}-{self.happiness}-{self.energy}-{skills}-{self.time}"

class item:
    def __init__(self,name,use,level,happiness):
        self.name=name
        self.use=use 
        self.level=level
        self.happiness=happiness
    def __str__(self):
        print(f"""{self.name}
    Class: {self.use}
    Level: {self.level}
    Happiness: {self.happiness}""")
        return''
    def export(self):
        return f"{self.name}-{self.use}-{self.level}-{self.happiness}"


class player:
    def __init__(self,name,pets,items):
        self.name=name
        self.pets=pets
        self.items=items
    def new_pet(self,pet):
        self.pets.append(pet)
    def new_item(self,item):
        self.items.append(item)
    def remove_item(self,item):
        self.items.remove(item)
    def remove_pet(self,pet):
        self.pets.remove(pet)
    def __str__(self):
        print(f"""{self.name}
Pets:""")
        for x in self.pets:
            print(f'    {x.name}')
        print('Items:')
        for x in range(len(self.items)):
            print(f'    {self.items[x].name} (lvl {self.items[x].level})')
        return ''
    def default(self):
        self.coins=20
        self.items=[item('basic bed','bed',1,1),
       item('basic food','food',1,1),
       item('basic toy','toy',1,1),
       item('wet_food','food',2,0),
       item('dry food','food',0,2)]
    def export(self):
        exported_item=[]
        for x in self.items:
            exported_item.append(x.export())
        exported_pet=[]
        for x in self.pets:
            exported_pet.append(x.export())
        items=';'.join(exported_item)
        pets=';'.join(exported_pet)
        return [self.name,pets,items,]


#Save/load handling
def load(name):
    with open("pet_simulator/accounts.csv","r",newline='') as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            if len(row)<0:
                pass
            else:
                if row[0] == name:
                    char=row
                    pets1=(char[1].split(';'))
                    pets=[]
                    for x in pets1:
                        traits=x.split('-')
                        pets.append(pet(traits[0],traits[1],traits[2],traits[3],traits[4],traits[5],traits[6].split('/'),traits[7]))
                    items1=(char[2].split(';'))
                    items=[]
                    for x in items1:
                        traits=x.split('-')
                        items.append(item(traits[0],traits[1],traits[2],traits[3]))
                   
                    char[1]=pets
                    char[2]=items
                    return char
        else: return False
 
def save(acc):
    accounts=[]  
    account=acc.export()
    with open("pet_simulator/accounts.csv","r",newline='') as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == acc.name:
                accounts.append({'name':account[0],'pets':account[1],'items':account[2]})
            else:
                accounts.append({'name':row[0],'pets':row[1],'items':row[2]})
    with open("pet_simulator/accounts.csv","w",newline='') as file:
        writer=csv.DictWriter(file,fieldnames=['name','pets','items'])
        writer.writeheader()
        writer.writerows(accounts)

def new_acc(acc):
    with open("pet_simulator/accounts.csv","a",newline='') as file:
        writer=csv.writer(file)
        if load(acc.name) == False:
            writer.writerow(acc.export())
        else:
            return False

def default_account(name,pet_name,species):
    account=player(name,[pet(pet_name,species,0,0,0,0,[],0)],0)
    account.default()
    return account


def login():
    print(f'Welcome to your pet simulator!')
    print(f'do you have an account?')
    print_list(['yes','no'])
    choice=int_input('')
    if choice==0:
        account=input('what is the name of your account?')
        loaded=load(account)
        if loaded==False:
            print(f'you do not have an account, make a new one?')
            login()
        else:
            acc=player(loaded[0],loaded[1],loaded[2])
            print(f"welcome back, {acc.name}!")
            print('your pets missed you')
            print('lets check up on them!')
            return acc
    elif choice==1:
        account=default_account(input('what is your name?\n'),input(' what is the name of your pet?\n'),input('what is the species of your pet?\n'))
        account.pets[0].skill_up()
        if new_acc(account) == False:
            print('that account already exists!')
            login()
        loaded=load(account.name)
        acc=player(loaded[0],loaded[1],loaded[2])
        print(f"Hello {acc.name}!")
        print(f"The people at the animal shelter have been watching you")
        print(f"and we have decided that you should have a pet!")
        print('well, have fun!')
        return acc
    else:
        print(f'invalid choice')
        login()
    


def choose_pet(user):
    print("what pet do you want to check on?")
    for x in range(len(user.pets)):
        print(f"{x}. {user.pets[x].name}")
    print(f'{x+1}. New pet?')
    print(f'{x+2}. Exit')
    choice=int_input('')
    
    if choice == len(user.pets):
        species=input('what kind of pet do you want?')
        pet_name=input('what is the name of your pet?')
        new=pet(pet_name,species,0,0,0,0,0,0)
        new.default()
        user.new_pet(new)
        choose_pet(user)
    elif choice == len(user.pets)+1:
        return False
    elif choice >=0 and choice < len(user.pets):
        pet_chosen=user.pets[choice]
        pet_play(pet_chosen,user)

    else:
        print('invalid pet')
        choose_pet(user)

def pet_play(pet,user):
    print(pet)
    print_list([f'Play with {pet.name}',f"feed {pet.name}",f'put {pet.name} to bed','exit'])
    choice=int_input('what do you want to do?   ')
    thing=[]
    items=[]
    if choice==0: #play
            for x in user.items:
                if x.use=='toy':
                    item=x
            pet.play(x)
    elif choice==1: #feed
        for x in user.items:
            if x.use=='food':
                thing.append(x.name)
                items.append(x)
        print(f'what food do you want to use?')
        print_list(thing)
        choice=int_input(f'Choose a food:  ')
        pet.feed(items[choice])
    elif choice==2: #put to bed
        for x in user.items:
            if x.use=='bed':
                item=x
        pet.sleep(item)
    elif choice == 3:
        game(user)
    else: #error handling
        print('invalid option')
        pet_play(pet,user)
    print(pet)

def event(user):
    pet=random.choice(user.pets)
    number=random.randint(0,100)
    if   number % 7 == 0:
        print(f'{pet.name} Got sick!')
        pet.energy=int(pet.energy)-random.randint(1,5)
    elif number % 5 == 0:
            print(f'{pet.name} Found a toy!')
            pet.happiness=int(pet.happiness)+(random.randint(1,5))
    elif number % 3== 0:
                pet.skill_up()
    elif number % 2== 0:
                    print(f'{pet.name} used their skill {random.choice(pet.skills)}')
    else:
                    print('Nothing happened this time')


def game(acc):
    print(acc)
    event(acc)
    exit=choose_pet(acc)
    if exit==False:
        print('bye bye!')
        return False
    else: game(acc)

def main():
    acc=login()
    #acc=load('cecily')
    #acc=player(acc[0],acc[1],acc[2])
    game(acc)
    print(acc)
    save(acc)
main()