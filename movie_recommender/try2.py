#cecily strong movie reccomender
"""
requierments:
Uses the provided Movies list 
User is able to choose at least 2 filters for the program to search through 
User can get recommendations based on genre, directors, length and/or actors 
User is able to print the whole list"""
import csv
movie=[]
with open("movie_recommender\Movies list.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        movie.append({"title":row[0],
                        "director":row[1],
                        "genre": row[2],
                        "rating": row[3],
                        "length in minutes": row[4],
                        "notable actor(s)":[row[5]]
                        })
def display(movie):
    for items in movie: #for filtering to work, instead of using the whole dictionary use just the filtered list
        #print(items)
        print('--------------------------------')
        for categories in items:
            
            if categories=='notable actor(s)':
                print(f'{categories}: {" ".join(movie[movie.index(items)][categories])}')
            else:
                print(f'{categories}: {(movie[movie.index(items)][categories])}')
def filter():
    exit = False
    identifiers = ['title','director','genre','rating','length in minutes','notable actor(s)']
    vars = {'title':'',
            'director':'',
            'genre':'',
            'rating':'',
            'length in minutes':[],
            'notable actor(s)':[]}
    for x in identifiers:
        item=[]
        if x == 'notable actor(s)':
            while exit == False:   #this lets you type in as many actors as you want
                individual = input("What actor would you like? type none to be done\n")
                if individual.lower() == 'none': #adds to the filters list and finishes the program
                    break
                else: 
                   item.append(individual)   #lets you add filters
        else:
            choose = input(f"What is the {x}? type none to skip\n")
            if choose.lower() == "none": #keeps it as empty so the filter is not applied
                item=[]
            elif x == 'length': #lets you use a range of ten minutes in either direction
                item.append(choose)
                for y in range(10):
                    item.append(int(choose)+y)
                for y in range(10):
                    item.append(int(choose)-y) 
            else:
                item.append(choose)
        vars[x]=item
    return(vars)

def search(filter,movie):
    search=[]#all movie titles
    check=True#true/false
    #print(filter)
    identifiers = ['title','director','genre','rating','length in minutes','notable actor(s)']
    for items in movie:
        #print(items)
        check=True
        #print(items)
        for x in identifiers:
            if len(filter[x])>0:
                for z in filter[x]:
                    if z in items[x]:
                        pass
                    else:
                        check=False
        #print(check)
        #print(check[0:-1])
        if check==True:
            search.append(items)

    return search

def main(movie,test_mode):
    stay=True
    while stay==True:
        try:
            choose=int(input("""Type the number of what you want:
                             1. Display all movies
                             2. filter movies
                             3. Exit\n"""))
            if choose==1:
                display(movie)
            elif choose==2:
                if test_mode==False:
                    display(search(filter(),movie))
                else:
                    display(search(movie[1],movie))
            elif choose==3:
                break
            else:
                print('invalid choice')
        except:
            print('invalid choice')


#main(movie,True)#testing mode
main(movie,False)
