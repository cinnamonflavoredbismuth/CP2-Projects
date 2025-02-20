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
            print(f" {row[0]}: {row[1]} {row[2]} \n ----------------------------")
def setup():
    basics={
        "number": [1,2],
        "items": ["wash dishes",'mow lawn'],
        'completion status': ['','X']
        }
    with open("to do list/list.csv","w+") as file:
        
        writer = csv.DictWriter(file, fieldnames = basics.keys())
        writer.writeheader()
        for i in range(len(basics)):
            writer.writerow([basics[x][i]])
        print(writer)

def complete():
    pass

def all_data(number):
    data = {}
    with open("to do list/list.csv","r") as file:
        reader = csv.reader(file)
        #next(reader)
        for row in reader:
                if row != number:
                    data[row[0]]=[row[1],row[2]]
        print(data)
        return(data)
            
def delete(data): 
    with open("to do list/list.csv","w+") as file:
        writer = csv.DictWriter(file, fieldnames = data)
        writer.writerows(data)
        print(writer)
def main():
    setup()
  #  delete(all_data(1))

main()
