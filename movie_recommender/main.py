#Cecily Strong Movie Recommender
"""
requierments:
Uses the provided Movies list DONE
User is able to choose at least 2 filters for the program to search through DONE
User can get recommendations based on genre, directors, length and/or actors DONE
User is able to print the whole list DONE"""
import csv
movie={}

def display(movie):
    for titles in movie:
        print(titles)
        for categories in movie[titles]:
            print(f"    {categories}: {movie[titles][categories]}")

with open("movie_recommender\Movies list.csv") as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        movie[row[0]]={
                        "Director":row[1],
                        "Genre": row[2],
                        "Rating": row[3],
                        "Length": row[4],
                        "Notable Actors":[row[5]]
                         }    

def search(movie):
    filter=[]
    search=[]
    exit=False
    identifiers=["title","director",'genre','rating','length','notable actor(s)']
    vars=["title",'director','genre','rating','length','notable_actors']
    while exit==False:
        try:
            first_choice=int(input("""Press the number of what you want to do:
            1. Print all the movies
            2. use filters"""))
            if first_choice==1:
                #filter setup
                for x in identifiers:
                    choose=input(f"What is the {x}? type none to skip\n")
                    if choose.lower() == "none":
                        vars[identifiers.index(x)]=""
                    else:
                        vars[identifiers.index(x)]=choose

                #checking all the movies using the filters
                for titles in movie:
                    #title
                    if len(vars[0])>0:
                        if vars[0].lower() == titles.lower():
                            filter.append[True]
                        else: filter.append[False]
                    else:filter.append[True]
                    #director,genre,rating,length
                    for x in vars[1:4]:
                        if len(vars)>0:
                            if (movie[titles][identifiers[vars.index[x]]]).lower()==vars.lower():
                                return(filter.append[True])
                            else: return(filter.append[False])
                        else:return(filter.append[True])
                    #notable actors
                    if len(vars[5])>0:
                        if vars[5].lower() in (movie[titles]["Notable Actors"]).lower():
                            filter.append[True]
                        else: filter.append[False]
                    else:filter.append[True]
                    #adds the movie to the list of the correct results
                    if False not in filter:
                        search.append(titles)
                return(search)
            elif first_choice==2:
                return(movie)
            else:
                print("invalid choice")
        except:
            print("Invalid choice")

def main(movie):
    stay=True
    while stay==True:
        try:
            choice=int(input("""choose the number of what to do
            1. search movies
            2. exit"""))
                
            if choice==1:
                filtered=search(movie)
                display(filtered)
            elif choice==2:
                return
            else:
                print("invalid choice")
        except:
            print("invalid choice")