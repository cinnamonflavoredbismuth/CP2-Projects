#Cecily Strong Personal Library Program
"""Stores all items in a list
Function to add a new item
Function to search the items
Function to remove an item
Function that runs the code (displays the menu options inside and calls the functions inside of a while True loop)
Project must include
easy to understand variable and function names
Pseudocode comments explaining what the code is doing
Good use of white space to keep items separate and easy to read/find
Have at least 2 people test your code before submission!
"""

#display all items (name, author or both?) 1
def display(library):
    for dicts in library:
        for names in dicts:
            print(f"{names}:") #Title
            for keys in library[library.index(dicts)][names]:
                print(f"    {keys}: {library[library.index(dicts)][names][keys]}") #information

def find(identifier,library,books):
    key=input(f"Who is the {identifier}?\n")
    for dicts in library:
        for names in dicts:
                for keys in library[library.index(dicts)][names]:
                    if keys==identifier:
                        if library[library.index(dicts)][names][keys]==key:
                                innit=True
                                books.add(names)
    if innit==True:
                print(f"The comics that have this {identifier} are:")
                print(*books, sep=', ')
    else:
        print(f"This is not an avaliable {identifier}")
#search all items (by name or author) 2
def search(library):

        innit=False
        books=set()
        choose=int(input('''Press the number of what you want
        1. Title
        2. Author
        3. Artist
        4. issue number
        5. Series\n'''))
        if choose==1:
            name=input("What is the name of the comic?\n")
            for dicts in library:
                for names in dicts:
                    print(names)
                    if name == names:
                        innit=True
            if innit==True:
                print(f"{name} is in the library")
            else:
                print(f"{name} is not in the library")
        elif choose==2:
            find("author",library,books)
            if innit==True:
                print("The comics that have this author are:")
                print(*books, sep=', ')
            else:
                print("This is not an avaliable author")
        elif choose==3:
            find("artist",library,books)
            
        


    
#add item (add name and author) 3
def add(library):
    name=input("What is the name of the book?\n")
    author=input("What is the author?\n")
    artist=input("What is the artist?")
    issue=input("What issue is it?")
    series=input("What series is it part of?")
    library.append({
        name:{"author":author,
        "artist":artist,
        "issue":issue,
        "series":series}
                     })
    print(library)

#remove item 4
def remove(library):
    name=input("What is the Title?")
    if name in library:
        library.remove(name)
    else:
        print(f"{name} is not in the library")
    
def main():
    #how the library will work: [name,author] for each item in the library list
    library=[
        {"The Boy Wonder #1":{
            "author":"Juni Ba",
            "artist":"Juni Ba",
            "issue":"1",
            "series":"The Boy Wonder"
        }},
        {"The Boy Wonder #2":{
            "author":"Juni Ba",
            "artist":"Juni Ba",
            "issue":"2",
            "series":"The Boy Wonder"
        }}
    ]
        
    run=True
    while run==True:
            select=int(input("""What would you like to do?
                     1. Display all items
                     2. Search items
                     3. Add a new item
                     4. Remove an item
                     5. Exit\n"""))
            if select==1:
                display(library)
            elif select==2:
                search(library)
            elif select==3:
                add(library)
            elif select==4:
                remove(library)
            elif select==5:
                print("Thank you")
                run=False
                break


main()
