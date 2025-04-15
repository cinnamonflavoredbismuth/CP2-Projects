#Cecily Strong Word Counter
def file(doc):
    word_count=0
    with open(doc,"r") as file:
        content = file.read()
        for char in content:
            if char==' ' or char=='\n': #this makes the word count based off of spaces or enters
                word_count+=1
    return word_count