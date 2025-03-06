#Cecily Strong Battle simulator charracter handling
#Functions: 1 Edit, 2 Delete
import csv
def write(chars):
    with open("battle simulator\char_data.csv","w",newline='') as file:
        writer=csv.DictWriter(file,fieldnames=['character name','fakemon','level'])
        writer.writeheader()
        writer.writerows(chars)
field_names = ['No', 'Company', 'Car Model'] 

#defaults
#write([{"character name":'tester1',"fakemon":'satan',"level":0},
#        {"character name":'tester2',"fakemon":'george w. bush',"level":1}])

def new_char(char,fakemon,level):
    with open("battle simulator\char_data.csv","a",newline='') as file:
        writer=csv.writer(file)
        writer.writerow([char,fakemon,level])
#new_char("tester3","fish",2)

def edit_char(char,level,func):
    #print(func)
    correctlist=[]
    charin=False
    with open("battle simulator\char_data.csv","r",newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            #print(row)
            if char == row[0]: 
                charin=True
                if func==1: #edit level
                    correctlist.append({"character name":row[0],"fakemon":row[1],"level":level})
                elif func==2:
                    pass
                else:
                    print("not a valid func")
            else:
                correctlist.append({"character name":row[0],"fakemon":row[1],"level":row[2]})
        if charin==False:
            print("your character is not in the list, create a new one?")
        else:
            #print(correctlist)
            write(correctlist)
        return
