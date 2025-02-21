#Cecily Strong To Do List
'''Create a to do list (Kept on a txt file)
Add items to the to do list
Mark item as complete
Delete item from to do list'''
"""
r = to read on file
w = write on the file (replaces old file)
w+ = read and write
a = append (add so the file, doesn't delete them) (create a file if it doesn't exist)
x = create a file
a+ = append and read
"""
import csv
import pandas as pd



def display():
    with open("to do list/list.csv","r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(f" {row[0]}: {row[1]} {row[2]} \n ----------------------------")

def write(data):
    with open("to do list/list.csv","w",newline='') as file:
        keys=["number","items","completion status"]
        writer = csv.DictWriter(file,fieldnames = keys)
        writer.writeheader()
        writer.writerows(data)

def length():
     correctlist=[]
     
     with open("to do list/list.csv","r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(row[0])
                correctlist.append({'number':row[0],'items':row[1],'completion status':row[2]})
            return correctlist
     
def remove(number):
    correctlist=[]
    with open("to do list/list.csv","r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0]!=number:
                   correctlist.append({'number':row[0],'items':row[1],'completion status':row[2]})
            return correctlist

def add(item):
    amount=len(length())
    with open("to do list/list.csv","a") as file:
         writer=csv.writer(file)
         writer.writerow([amount+1,item,''])

def complete(number):
    data=length()
    print(data)
    for x in data:
        if data[data.index(x)]['number']==number:
            data[data.index(x)]['completion status']='X'

def main(data):
    write(data)
    display()

data=[
       {"number":1,'items':'wash dishes','completion status':''},
       {'number':2,'items':'mow lawn','completion status':'X'}]

main(data)
complete(2)