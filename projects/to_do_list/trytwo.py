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


def display():
    with open("to do list/list.txt","r") as file:
            reader = file.read()
            words=''
            for item in reader:
                if item == '\n':
                    print(f"{words}")
                    words=''
                else:
                    words=words+item
                

def write(data):
    with open("to do list/list.txt","w",newline='') as file:
        for x in data:
            file.write(f"{data[data.index(x)]}\n")
    return

def remove(item):
    correctlist = []
    with open("to do list/list.txt","r") as file:
            reader = file.read()
            words=""
            for letter in reader:
                if letter=='\n':
                    if item not in words: 
                        correctlist.append(words)
                    else: pass
                    words=""
                else:
                    words=words+letter
            write(correctlist)
            return

def add(item):
    correctlist=[]
    with open("to do list/list.txt","r") as file:
            reader = file.read()
            words=""
            for letter in reader:
                if letter=='\n':
                    correctlist.append(words)
                    words=""
                else:
                    words=words+letter
            correctlist.append(item)
            write(correctlist)
            return

def complete(item):
    correctlist = []
    with open("to do list/list.txt","r") as file:
            reader = file.read()
            words=""
            for letter in reader:
                if letter=='\n':
                    if item in words:
                        correctlist.append(f"{words} X")
                    else: 
                        correctlist.append(words)
                    words=""
                else:
                    words=words+letter
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
            main()
        elif choose2 == 2: #add
            item = input('what would you like to add?\n')
            add(item)
            main()
        elif choose2 == 3: #remove
            number = input('what do you want to remove?\n')
            remove(number)
            main()
        elif choose2 == 4: #mark as complete
            number = input('what do you want to complete?\n')
            complete(number)
            main()
            
        elif choose2 == 5: #exit
            return
        else:
            print('not an option')
            main()
    except: 
        print('not a number')
        main()
    

#write(['wash dishes','clean room','fold laundry X'])

#main()