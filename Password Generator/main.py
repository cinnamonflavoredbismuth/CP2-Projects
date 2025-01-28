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

#length of the password
def length():
    return(int(input("How many characters do you want your password to be?\n")))

#upercase letters
def uppercase():
    return(random.choice(string.ascii_uppercase))
 
#lowercase letters
def lowercase():
    return(random.choice(string.ascii_lowercase))

#numbers
def numbers():
    return(random.choice(string.digits))

#special characters
def special_chars():
    return(random.choice(string.punctuation))

#main function
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
                print(x)
                functions.append(x)
                break
            elif yn=="n":
                break
            else:
                print("invalid option\n") #stupid proofing
    for x in range(amount):
        password.append(all_functions[random.choice(functions)]()) #basically this it picking a random function from the ones you said yes to 
    print("".join(password))

main()