#Cecily Strong Pet Simulator
import random
class pet:
    def __init__(self,name,species):#,age,hunger,happiness,energy):
        self.name=name
        self.species=species
        self.age=0
        self.hunger=20
        self.happiness=20
        self.energy=20
        #'''
    def __str__(self):
        return f"""{self.name}
    Species: {self.species}
    Age: {self.age} week(s)
    Hunger: {self.hunger}
    Happiness: {self.happiness}
    Energy: {self.energy}"""
    def max(self):
        self.hunger=20
        self.happiness=20
        self.energy=20
    def ageup(self):
        self.age=self.age+1

class item:
    def __init__(self,name,use,stats,quantity,price):
        self.name=name
        self.use=use 
        self.stats=stats
        self.quantity=quantity
        self.price=price
    def __str__(self):
        print(f"""{self.name}
    It costs {self.price} coins
    class: {self.use}
    quantity: {self.quantity}""")
    def purchase(self):
        if self.quantity>0:
            self.quantity=self.quantity-1
            return True
        else: 
            print('The item is not in stock!')
            return False
    def sell(self):
        self.quantity=self.quantity+1

class player:
    def __init__(self,name,pets):
        self.name=name
        self.pets=pets
        self.coins=20
    def income(self,income):
        self.coins=self.coins+income
    def expense(self,expense):
        self.coins=self.coins-expense
    def new_pet(self,pet):
        print(self.pets)
        print(self.pets.append(1))
        self.pets=list(self.pets).append(pet)
        print(self.pets)
    def __str__(self):
        return f"""{self.name}
    {self.coins} 
    Pets:
        {self.pets[0]}
        {self.pets[1]}"""
            

coco=pet('Coco','Cat')
henri = pet('Henri','dog')
cecily=player('cecily',[coco,0])
print(cecily)
cecily.new_pet(henri)
#print(cecily)

#print(henri)
henri.max()
henri.ageup()
#print(henri)