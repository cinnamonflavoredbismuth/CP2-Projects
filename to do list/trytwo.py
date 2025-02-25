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

            if str(number) in (the_dict):
                return True
            else:
                return False
        


def display():
    with open("to do list/list.csv","r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(f" {row[0]}: {row[1]} {row[2]} \n ----------------------------")

def write(data):
    with open("to do list/list.csv","w",newline='') as file:
        keys = ["number","items","completion status"]
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
                correctlist.append({'number':row[0],'items':row[1],'completion status':row[2]})
            return correctlist
     
def remove(number):
    correctlist = []
    with open("to do list/list.csv","r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] != str(number):
                   correctlist.append({'number':row[0],'items':row[1],'completion status':row[2]})
            return correctlist

def add(item):
    amount = len(length())
    with open("to do list/list.csv","a") as file:
         writer = csv.writer(file)
         writer.writerow([amount+1,item,''])
    return

def complete(number):
    data = length()
    print(data)
    for x in data:
        if data[data.index(x)]['number'] == str(number):
            data[data.index(x)]['completion status']='X'
    return data

def main():
    exit=False
    while exit == False:
        try:
            choose = int(input('''Press the number of what you want:
                            1. Display List
                            2. Add an item
                            3. Remove an item
                            4. Mark an item as done
                            5. Exit
                            '''))
            if choose == 1: #display
                display()
            elif choose == 2: #add
                item = input('what would you like to add?')
                add(item)
            elif choose == 3: #remove
                    try:
                        number = int(input('what number do you want to remove?'))
                        valid = check(number)
                        if valid == True:
                            remove(number)
                        else:
                            print('invalid option')
                    except:
                        print('invalid option')

            elif choose == 4: #mark as complete
                valid = False
                try:
                    number = int(input('what number do you want to complete?'))
                    valid = check(number)
                    if valid == True:
                        complete(number)
                    else:
                        print('invalid option')
                except:
                    print('invalid option')
            elif choose == 5: #exit
                break
            else:
                print('invalid choice')
        except: print('invalid choice')

remove(2)
main()