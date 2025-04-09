#Cecily Strong Word Counter
from datetime import date
from file import file as word_count


#doc='word counter/document.txt' #for testing

def main():
    doc=input('what is the document called?')
    with open(doc,"a") as file:
        content = f"\nThe word count is: {word_count(doc)}. Word count was last updated {date.today()}" #this is what is added to the document
        file.write(content) #this is how it is added to the document
    print(content) #lets the user know what the date and word count is
main()