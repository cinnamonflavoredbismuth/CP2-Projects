#Cecily Strong
#Reading Files notes
#1. How do you open a file in your program?
#
#2. How do you alter text to work as data in a program?
#
#3. What is a CSV file Download CSV file?
#
#4. How are they used in programming?
#
import csv

with open("Notes UwU/reading files.txt","r") as file:
    content = file.read()
    print(content.upper())
print(content)
#file = open("Notes UwU\user_info.csv,","r").read()

users = {}

with open("Notes UwU/user_info.csv") as file:
    reader = csv.reader(file)
    #this is the headers of the csv, dodnt print
    next(reader)
    for row in reader:
        print(row)
        #              key    item
        users.update({row[0]:row[1]})
print(users)
        