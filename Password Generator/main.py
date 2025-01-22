#Cecily Strong Random Password Generator
"""A main function that runs the code
Functions for the different password requirements
A function that assembles that password once it is the correct length
Users should be able to specify length and if they want to include
uppercase letters
lowercase letters
numbers
special characters
HINT: You can make this by randomly selecting from different lists OR by randomly generating the ASCII letters! """

import random
import string

def choose():
    main_list=[int(input("How many characters do you want your password to be?"))
               ,input("Do you want uppercase letters? y/n"),input("Do you want lowercase letters? y/n")
               ,input("Do you want numbers? y/n"),input("Do you want special characters? y/n")]
    return(main_list)
def length():
    return(int(input("How many characters do you want your password to be?")))

def uppercase():
    return(random.choice(string.ascii_uppercase))
 
def lowercase():
    return(random.choice(string.ascii_lowercase))

def numbers():
    return(random.choice(string.digits))

def special_chars():
    return(random.choice(string.punctuation))

def assemble():
    pass

def main():
    main_list=print()
    print(main_list)
    functions=[]
    password=[]
    if main_list[1]=="y":
        functions.append(uppercase())
    if main_list[2]=="y":
        functions.append(lowercase())
    if main_list[3]=="y":
        functions.append(numbers())
    if main_list[4]=="y":
        functions.append(special_chars())
    print(functions)
    for x in range(main_list[0]+1):
        password.append(random.choice(functions))
        print(password)
main()