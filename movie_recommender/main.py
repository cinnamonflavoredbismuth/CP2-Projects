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
                        "Director":row[1],
                        "Genre": row[2],
                        "Rating": row[3],
                        "Length": row[4],
                        "Notable Actors":[row[5].join(' ,')]
                         }    


#displays the movies
def display(search,movie):
    for titles in search: #for filtering to work, instead of using the whole dictionary use just the filtered list
        print(titles) #prints the title
        for categories in movie[titles]:
            print(f"    {categories}: {movie[titles][categories]}") #prints each category and whats in it

#making the original filters
def filters():
    actors = []
    exit = False
    identifiers = ["title","director",'genre','rating','length','notable actor(s)']
    vars = ["title",'director','genre','rating','length','notable_actors']
    for x in identifiers:
        if x == 'notable actor(s)':
            while exit == False:   #this lets you type in as many actors as you want
                individual = input("What actor would you like? type done to be done\n")
                if individual.lower() == 'done': #adds to the filters list and finishes the program
                    vars[identifiers.index] = actors
                    break
                else: #adds to the actor list that will eventually be added
                    actors.append(individual)
        else:   #lets you add filters
            choose = input(f"What is the {x}? type none to skip\n")        
            if choose.lower() == "none": #keeps it as empty so the filter is not applied
                vars[identifiers.index(x)] = ""
            else:
                vars[identifiers.index(x)] = choose
    return(vars)

#checking all the movies using the filters
def search(movie,vars):
    filter = []
    search = []
#                      0        1        2       3        4            5
    identifiers = ["title","director",'genre','rating','length','notable actor(s)']

    for titles in movie: #check the title
        if len(vars[0])>0: 
            if vars[0].lower() == titles.lower():
                filter.append[True] 
            else: filter.append[False] #if the filter does not conform to the specification
        else:filter.append[True]

        
        for x in vars[1:4]: #check the director, genre, rating, and length
            if len(vars)>0:
                if (movie[titles][identifiers[vars.index[x]]]).lower() == vars.lower():
                    (filter.append[True])
                else: (filter.append[False]) #if the filter does not conform to the specification
            else:(filter.append[True])

        
        if len(vars[5])>0:  #check the notable actors
            if vars[5].lower() in (movie[titles]["Notable Actors"]).lower():
                filter.append[True]
            else: filter.append[False] #if the filter does not have all the actors that were wanted
        else:filter.append[True]

        
        if False not in filter: #adds the movie to the list of the correct results
            #the falses are for if the movie does not contain all specifications
            search.append(titles)

    #This is the final list of all the movies that are within the parameters
    return(search)

#main interface. lets you choose what to do
def main(movie):
    stay = True
    while stay == True: #lets it run for however long you want
        try:
            choice = int(input("""
Choose the number of what to do
            1. filter movies
            2. display all movies
            3. exit\n"""))
                
            if choice == 1: #filter the movies and then display
                vars = filters()
                filtered = search(movie,vars)
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

main(movie)