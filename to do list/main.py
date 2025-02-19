#Cecily Strong To Do List
'''Create a to do list (Kept on a txt file)
Add items to the to do list
Mark item as complete
Delete item from to do list'''
import csv

import pandas as pd

def display():
    with open("to do list/list.csv","r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(f" {row[0]} {row[1]} \n ----------------------------")
def add():
    pass

def complete():
    pass

def delete(number):
    data = {}
    with open("to do list/list.csv","r+") as file:
        reader = csv.reader(file)
        print(reader)
        for row in reader:
            if row != number:
                data[]
        print(reader)

def main():
    delete()

main()