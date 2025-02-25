#Cecily Strong Movie Recommender
"""
requierments:
Uses the provided Movies list 
User is able to choose at least 2 filters for the program to search through 
User can get recommendations based on genre, directors, length and/or actors 
User is able to print the whole list"""
import csv
movie = {}

#main setup. muchos importante
with open("movie_recommender\Movies list.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        movie[row[0]] = {
                        "director":[row[1]],
                        "genre": row[2],
                        "rating": [row[3]],
                        "length": [row[4]],
                        "notable actors":[row[5]]
                         }    

#displays the movies
def display(search,movie):
    for titles in search: #for filtering to work, instead of using the whole dictionary use just the filtered list
        print(titles) #prints the title
        for categories in movie[titles]:
            print(f"    {categories}: {' '.join(movie[titles][categories])}") #prints each category and whats in it

#making the original filters
def filters():
    exit = False
    identifiers = ['title','director','genre','rating','length in minutes','notable actor(s)']
    vars = {'title':[],
            'director':[],
            'genre':'',
            'rating':[],
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

#checking all the movies using the filters
def search(movie,vars):
    filter = []
    search = []
    
    #                 0        1        2       3        4            5
    identifiers = ['title','director','genre','rating','length in minutes','notable actor(s)']
    for titles in movie: #check the title
        if len(vars['title'])>0: 
            if (z.lower() for z in vars['title']) in (z.lower() for z in titles):
                filter.append(True) 
            else: filter.append(False) #if the filter does not conform to the specification
        else:
            filter.append(True)

        for x in identifiers[1:5]: #check the director, genre, rating, and length
            if len(vars[x])>0:
                for y in vars[x]:
                    if y.lower() in (z.lower() for z in (movie[titles][x])):
                        (filter.append(True))
                    else: (filter.append(False)) #if the filter does not conform to the specification
            else:
                filter.append(True)
        
        if 0 not in filter: #the falses are for if the movie does not contain all specifications
            search.append(titles) #adds the movie to the list of the correct results

    #This is the final list of all the movies that are within the parameters
    return(search)

#main interface. lets you choose what to do
def main(movie):
    
    #For testing!!!
    #"""
    vars_for_testing = {
            'title':['Forrest Gump'],
            'director':['Robert Zemeckis'],
            'genre':['Drama'],
            'rating':['pg-a3'],
            'length in minutes':['140'],
            'notable actor(s)':['Tim Robbins']}
    #"""

    stay = True
    while stay == True: #lets it run for however long you want
        try:
            choice = int(input("""
Choose the number of what to do
            1. filter movies
            2. display all movies
            3. exit\n"""))
                
            if choice == 1: #filter the movies and then display
                #vars = filters()
                vars=vars_for_testing
                filtered = search(movie,vars)
                print('---------------------------------------')
                print("The movies that fit this category are...")
                display(filtered,movie)
            elif choice == 2: #display all the movies
                
                display(movie.keys(),movie)
            elif choice == 3: #leave
                return
            
        #stupid proofing
            else:
                print("invalid choice")
        except:
            print("invalid choice")

vars_for_testing = {
            'title':['Forrest Gump'],
            'director':['Robert Zemeckis'],
            'genre':['Drama'],
            'rating':['pg-a3'],
            'length in minutes':['140'],
            'notable actor(s)':['Tim Robbins']}
search(movie,vars_for_testing)
#main(movie)