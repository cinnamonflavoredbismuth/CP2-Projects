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

def check(number):
    the_dict=[]
    with open("to do list/list.csv","r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                the_dict.append(row[0])

            if number in the_dict:
               
                return True
            else:
             
                return False

def display():
    with open("to do list/list.csv","r") as file:
            reader = csv.reader(file)
            print(reader)
            next(reader)
            for row in reader:
                print(f"{row[0]} {row[1]} \n ----------------------------")

def write(data):
    with open("to do list/list.csv","w",newline='') as file:
        keys = ["items","completion status"]
        writer = csv.DictWriter(file,fieldnames = keys)
        writer.writeheader()
        writer.writerows(data)
    return

def length():
     correctlist=[]
     
     with open("to do list/list.csv","r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(row[0])
                correctlist.append({'items':row[0],'completion status':row[1]})
            return correctlist
     
def remove(item):
    correctlist = []
    with open("to do list/list.csv","r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(row)
                if row[0] != item:
                   correctlist.append({'items':row[0],'completion status':row[1]})
            write(correctlist)
            return

def add(item):
    with open("to do list/list.csv","a") as file:
         writer = csv.writer(file)
         writer.writerow([item,''])
    return

def complete(item):
    correctlist=[]
    with open("to do list/list.csv","r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(row)
                if row[0] != item:
                   correctlist.append({'items':row[0],'completion status':row[1]})
                else:
                   correctlist.append({'items':row[0],'completion status':'X'})  
            write(correctlist)
            return

def main():
    try:
        choose2 = int(input('''Press the number of what you want:
                        1. Display List
                        2. Add an item
                        3. Remove an item
                        4. Mark an item as done
                        5. Exit
                        '''))
        if choose2 == 1: #display
            display()
        elif choose2 == 2: #add
            item = input('what would you like to add?')
            add(item)
        elif choose2 == 3: #remove
            number = input('what do you want to remove?')
            valid = check(number)
            if valid == True:
                write(remove(number))
            else:
                print('invalid option')
                

        elif choose2 == 4: #mark as complete
            valid = False
            number = input('what do you want to complete?')
            complete(number)
            
            
        elif choose2 == 5: #exit
            return
        else:
            print('invalid choice1')
            main()
    except: 
        print('invalid choice2')
        main()


display()
remove('mow lawn')
display()
main()