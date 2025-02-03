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
    for x in library:
        print(f"{x[0]} by {x[1]}")

#search all items (by name or author) 2
def search(library):
    pass

#add item (add name and author) 3
def add(library):
    name=input("What is the name of the book?\n")
    author=input("What is the author?\n")
    library.add((name,author))

#remove item 4
def remove(library):
    pass

def main():
    #how the library will work: [name,author] for each item in the library list
    library={("The Boy Wonder #1","Juni Ba"),("The Boy Wonder #2","Juni Ba")}
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
