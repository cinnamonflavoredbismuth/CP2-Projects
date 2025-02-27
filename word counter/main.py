#Cecily Strong Word Counter
#doc=input("type your file here")
from datetime import date
""""Write a program that look at a document that a user has written on and update it with the word count and a timestamp for when that wordcount was last updated

REQUIREMENTS:
Uses at least 3 pages (main, file handling, and time handling) NOTE: main is the only file name I've given you
Reads and Writes to the file
Uses functional decomposition
Lets the user tell what file to use it on
Uses good naming practices
Has good white space"""

doc=input('what is the document called?')
#doc='word counter/document.txt' #for testing
def word_count(doc):
    word_count=0
    with open(doc,"r") as file:
        content = file.read()
        #next(content)
        for char in content:
            if char==' ' or char=='\n':
                word_count+=1
    return word_count
def main(doc):
    with open(doc,"a") as file:
        content = f"\nThe word count is: {word_count(doc)}. Word count was last updated {date.today()}"
        file.write(content)
    print(content)
main(doc)