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
    def __init__(self,name,species,age,hunger,happiness,energy):
        self.name=name
        self.species=species
        self.age=age
        self.hunger=hunger
        self.happiness=happiness
        self.energy=energy
        #'''
    def __str__(self):
        return f"""    {self.name}
        Species: {self.species}
        Age: {self.age} day(s)
        Hunger: {self.hunger}
        Happiness: {self.happiness}
        Energy: {self.energy}"""
    def default(self):
        self.age=0
        self.hunger=20
        self.happiness=20
        self.energy=20
    def feed(self,user,food):
        self.hunger=self.hunger+food.level
        self.happiness=self.happiness+food.happiness
        user.time+=1
    def play(self,user,toy):
        self.energy=self.energy-1
        self.happiness=self.happiness+toy.level
        self.hunger=self.hunger-1
        user.time+=1
    def sleep(self,user,bed):
        self.energy=self.energy+bed.level
        self.age=self.age+1
        user.time+=5
    def export(self):
        return f"{self.name}-{self.species}-{self.age}-{self.hunger}-{self.happiness}-{self.energy}"

class item:
    def __init__(self,name,use,level,happiness,price):
        self.name=name
        self.use=use 
        self.level=level
        self.price=price
        self.happiness=happiness
    def __str__(self):
        print(f"""{self.name}
    Price: {self.price} coins
    Class: {self.use}
    Level: {self.level}
    Happiness: {self.happiness}""")
        return''
    def export(self):
        return f"{self.name}-{self.use}-{self.level}-{self.happiness}-{self.price}"

class player:
    def __init__(self,name,pets,items,coins,time):
        self.name=name
        self.pets=pets
        self.coins=coins
        self.items=items
        self.time=time
    def income(self,income):
        self.coins=self.coins+income
    def expense(self,expense):
        self.coins=self.coins-expense
    def new_pet(self,pet):
        self.pets.append(pet)
    def new_item(self,item):
        self.items.append(item)
    def remove_item(self,item):
        self.items.pop(item)
    def remove_pet(self,pet):
        self.pets.pop(pet)
    def __str__(self):
        print(f"""{self.name}
    {self.coins} coins 
Pets:""")
        for x in range(len(self.pets)):
            print(f'    {self.pets[x].name}')
        print('Items:')
        for x in range(len(self.items)):
            print(f'    {self.items[x].name} (lvl {self.items[x].level})')
        return ''
    def default(self,user):
        self.coins=20
        user.items=[item('basic bed','bed',1,1,0),
       item('basic food','food',1,1,0),
       item('basic toy','toy',1,1,0)]
    def export(self):
        exported_item=[]
        for x in self.items:
            exported_item.append(x.export())
        exported_pet=[]
        for x in self.pets:
            exported_pet.append(x.export())
        items=';'.join(exported_item)
        pets=';'.join(exported_pet)
        return [self.name,pets,items,str(self.time),str(self.coins)]

#Save/load handling
def load(name):
    with open("pet_simulator/accounts.csv","r",newline='') as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            if len(row)<0:
                pass
            else:
                #print(row)
                if row[0] == name:
                    char=row
                    pets1=(char[1].split(';'))
                    pets=[]
                    for x in pets1:
                        traits=x.split('-')
                        pets.append(pet(traits[0],traits[1],traits[2],traits[3],traits[4],traits[5]))
                    items1=(char[2].split(';'))
                    items=[]
                    for x in items1:
                        traits=x.split('-')
                        items.append(item(traits[0],traits[1],traits[2],traits[3],traits[4]))
                   
                    char[1]=pets
                    char[2]=items
                    return char
        else:
            return False

def write(chars):
    with open("pet_simulator/accounts.csv","w",newline='') as file:
        writer=csv.DictWriter(file,fieldnames=['name','pets','items','coins','time'])
        writer.writeheader()
        writer.writerows(chars)

def save(acc):
    accounts=[]
    account=acc.export()
    with open("pet_simulator/accounts.csv","r",newline='') as file:
        reader=csv.reader(file)
        for row in reader:
            if row[0] == acc.name:
                accounts.append({'name':account[0],'pets':account[1],'items':account[2],'coins':account[3],'time':account[4]})
            else:
                accounts.append({'name':row[0],'pets':row[1],'items':row[2],'coins':row[3],'time':row[4]})
    write(accounts)

def new_acc(acc):
    with open("pet_simulator/accounts.csv","a",newline='') as file:
        writer=csv.writer(file)
        if load(acc.name) == False:
            writer.writerow(acc.export())
        else:
            print('Username already taken')

def default_account(name,pet_name,species):
    account=player(name,[pet(pet_name,species,0,0,0,0)],0,20,0)
    acc=account.default()
    return acc

loaded=load('cecily')
acc=player(loaded[0],loaded[1],loaded[2],loaded[3],loaded[4])

#functions
def login():
    print('Welcome to your pet simulator!')
    print('do you have an account?')
    print_list(['yes','no'])
    choice=int_input('')
    if choice==0:
        account=input('what is the name of your account?')
        loaded=load(account)
        acc=player(loaded[0],loaded[1],loaded[2],loaded[3],loaded[4])
    elif choice==1:
        account=default_account(input('what is your name?'),input(' what is the name of your pet?'),input('what is the species of your pet?'))
        new_acc(account.export())
        loaded=load(account.name)
        if loaded==False:
            print('you do not have an account, make a new one?')
            login()
        else:
            acc=player(loaded[0],loaded[1],loaded[2],loaded[3],loaded[4])
    else:
        print('invalid choice')
        login()
    return acc

def main():
    #acc=login()
    acc=load('cecily')

#main()