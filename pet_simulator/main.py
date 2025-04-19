#Cecily Strong Pet Simulator
"""Class Implementation:
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
        Age: {self.age} week(s)
        Hunger: {self.hunger}
        Happiness: {self.happiness}
        Energy: {self.energy}"""
    def default(self):
        self.age=0
        self.hunger=20
        self.happiness=20
        self.energy=20
    def ageup(self):
        self.age=self.age+1
    def feed(self,food):
        self.hunger=self.hunger+food.level
        #subtract happiness?
    def play(self,toy):
        self.energy=self.energy-toy.level
        #finish this. add happiness, ect
    def sleep(self,bed):
        pass
    #finish this. subtract hunger, add energy

class item:
    def __init__(self,name,use,level,price):
        self.name=name
        self.use=use 
        self.level=level
        self.price=price
    def __str__(self):
        print(f"""{self.name}
    Price: {self.price} coins
    Class: {self.use}
    Level: {self.level}""")
        return''

class player:
    def __init__(self,name,pets,items,coins):
        self.name=name
        self.pets=pets
        self.coins=coins
        self.items=items
    def income(self,income):
        self.coins=self.coins+income
    def expense(self,expense):
        self.coins=self.coins-expense
    def new_pet(self,pet):
        self.pets[len(list(pets.keys))+1]=pet
    def __str__(self):
        print(f"""{self.name}
    {self.coins} coins 
Pets:""")
        for x in list(self.pets.keys()):
            print(f'    {self.pets[x].name}')
        print('Items:')
        for x in list(self.items.keys()):
            print(f'    {self.items[x].name} (lvl {self.items[x].level})')
        return ''
    def default(self):
        self.coins=20
        user.items={0:item('basic bed','bed',1,0),
       1:item('basic food','food',1,0),
       2:item('basic toy','toy',1,0)}
            
pets={0:pet('Coco','Cat',0,0,0,0),
      1:pet('Henri','dog',0,0,0,0)}
items={0}
user=player('cecily',pets,items,0)
user.default()
user.pets[0].default()
user.pets[1].default()

print(user)
print(user.pets[1])

