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

#search all items (by name or author) 2
def search(library):

        innit=False
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
                print("It is in the library")
            else:
                print("nope")


    
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
