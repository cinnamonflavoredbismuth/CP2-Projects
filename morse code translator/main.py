#Cecily Strong Simple Morse Code Translator
"""Create two lists (one of the alphabet letters in English, and other for the corresponding Morse Code Symbols) 
Create a function to translate English into Morse Code
Create a function to translate Morse Code into English
Create a main loop where users can choose to translate English to Morse Code, Morse Code to English, or Exit
Project needs to:
Use string manipulation to control the appearance of the output 
Use basic error handling (for characters not in Morse Code)
Use good naming for functions and variables
Use pseudocode comments to explain what the program is doing
Use white space to make sure code is easy to read"""
def english_to_morse(translate):
    split(translate)
def morse_to_english(translate):
    pass
def main():
    exit=False
    while exit==False:
        try:
            choice=int(input("""1. English to morse code
                     2.Morse code to english
                     3. Exit"""))
            if choice==1:
                english_to_morse(input("What do you want to translate?"))
            if choice==2:
                english_to_morse(input("What do you want to translate?"))
            elif choice==3:
                break
            else:
                print("invalid option")
        except:
            print("Invalid option")