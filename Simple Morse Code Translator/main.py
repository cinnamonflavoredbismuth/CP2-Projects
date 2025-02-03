#Cecily Strong Morse code translator
'''Create two lists (one of the alphabet letters in English, and other for the corresponding Morse Code Symbols) 
Create a function to translate English into Morse Code
Create a function to translate Morse Code into English
Create a main loop where users can choose to translate English to Morse Code, Morse Code to English, or Exit
Project needs to:
Use string manipulation to control the appearance of the output 
Use basic error handling (for characters not in Morse Code)
Use good naming for functions and variables
Use pseudocode comments to explain what the program is doing
Use white space to make sure code is easy to read
'''



def morse_to_english(): #morse to english, option 1
    morse=[".-",'-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-',
       '.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.','.-.-.-','--..--','..--..','/']
    english=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
         ,'0','1','2','3','4','5','6','7','8','9','.',',','?',' ']
    code=input("What do you want to translate?\n")
    code3=code.split(' ')
    for x in code3:
        if x not in morse:
            return("Invalid")
    for x in code3:
        code3[code3.index(x)]=english[morse.index(x)]
    return(' '.join(code3))

def english_to_morse(): #english to morse code, option 2
    
    morse=[".-",'-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-',
       '.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.','.-.-.-','--..--','..--..','/']
    english=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
         ,'0','1','2','3','4','5','6','7','8','9','.',',','?',' ']
    code=input("What do you want to translate?\n")
    code2=code.lower()
    code3=list(code2)
    for x in code3:
        if x not in english:
            return("Invalid")
    for x in code3:
        code3[code3.index(x)]=morse[english.index(x)]
    return(' '.join(code3))

def main():
    exit=False
    while exit==False:
        try:
            choice=int(input("""Press the number of what you want:
                            1. Morse to english
                            2. English to morse
                            3. Exit\n"""))
            if choice==1:
                code=input("What do you want to translate?\n")
                print(morse_to_english())
            elif choice==2:
                
                print(english_to_morse())
            elif choice==3:
                break
            else:
                print("Invalid choice")
        except:
            print("Not a number")

main()