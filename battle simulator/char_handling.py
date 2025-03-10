#Cecily Strong Battle simulator charracter handling
#Functions: 1 Edit, 2 Delete
import csv
from helper_functions import options
def write(chars):
    with open("battle simulator\char_data.csv","w",newline='') as file:
        writer=csv.DictWriter(file,fieldnames=['name','lvl','xp','fakemon','hp','str','def','spd'])
        writer.writeheader()
        writer.writerows(chars)


#defaults
defaults=[{'name':'tester1','xp':4,'lvl':1,'fakemon':'satan','hp':5,'str':0,'def':1,'spd':2},
       {'name':'tester2','xp':4,'lvl':1,'fakemon':'george w bush','hp':7,'str':1,'def':2,'spd':1}]
#write(defaults)

def new_char(char,xp,lvl,fakemon,hp,str,defe,spd):
    with open("battle simulator\char_data.csv","a",newline='') as file:
        writer=csv.writer(file)
        writer.writerow([char,xp,lvl,fakemon,hp,str,defe,spd])

def edit_char(char,xp,lvl,fakemon,hp,str,defe,spd,func):
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
                    correctlist.append({"name":char,'lvl':lvl,'xp':xp,"fakemon":fakemon,"hp":hp,"str":str,'def':defe,'spd':spd})
                elif func==2:
                    pass
                else:
                    print("not a valid func")
                    correctlist.append({"name":row[0],'lvl':row[1],'xp':row[2],"fakemon":row[3],"hp":row[4],"str":row[5],'def':row[6],'spd':row[7]})
            else:
                correctlist.append({"name":row[0],'lvl':row[1],'xp':row[2],"fakemon":row[3],"hp":row[4],"str":row[5],'def':row[6],'spd':row[7]})
        if charin==False:
            print("your character is not in the list, create a new one?")
        else:
            #print(correctlist)
            write(correctlist)
        return

def export_char(name):
    char={}
    with open("battle simulator\char_data.csv","r",newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == name:
                char[row[0]]=({'lvl':row[1],'xp':row[2],"fakemon":row[3],"hp":row[4],"str":row[5],'def':row[6],'spd':row[7]})
                return char
        else:
            return False

def display_chars():
    with open("battle simulator\char_data.csv","r",newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(f"name:{row[0]} lvl:{row[1]},xp:{row[2]} fakemon:{row[3]} hp:{row[4]} str:{row[5]},def:{row[6]} spd:{row[7]}")