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

def length():
    return(int(input("How many characters do you want your password to be?\n")))

def uppercase():
    return(random.choice(string.ascii_uppercase))
 
def lowercase():
    return(random.choice(string.ascii_lowercase))

def numbers():
    return(random.choice(string.digits))

def special_chars():
    return(random.choice(string.punctuation))

def main():
    
    password=[]
    amount=length()
    functions=[]
    questions=["Do you want uppercase letters? y/n\n","Do you want lowercase letters? y/n\n","Do you want numbers? y/n\n","Do you want special characters? y/n\n"]
    all_functions=[uppercase,lowercase,numbers,special_chars]
    for x in range(4):
        yn=0
        while yn!="y" and yn!="n":
            yn=str(input(questions[x]))
            if yn=="y":
                functions.append(x)
                break
            elif yn=="n":
                break
            else:
                print("invalid option")
    print(functions)
    for x in range(amount):
        password.append(all_functions[random.randint(0,len(functions))]())
    print("".join(password))
    '''
functions=[uppercase,lowercase,numbers,special_chars]
print(len(functions))
print(random.randint(0,3))
print(random.randint(0,len(functions)))
print(functions[1])
print(functions[random.randint(0,len(functions))])
functions[1]
functions[random.randint(0,len(functions))]
'''
main()