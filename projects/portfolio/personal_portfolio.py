#Cecily Strong Personal Portfolio
from movie_recommender.main import main2 as movie #
from to_do_list.trytwo import main as to_do_list #
from personal_library.main import main as library #
from battle_simulator.main import main2 as battle #
from coin_change_problem.main import main as coin #
from word_counter.main import main as word #
from helpers import *



def main():
    projects={
        1:[library,'Peronal Library',"The personal library is supposed to store comics and their authors, dates of publication, ect. in a dictionary as a way to learn different list types. What I didn't expect was the list types our teacher wanted us to use were not exactly optimal for a library program. Time and time again I wished I could just use dictionaries, alas, the project requirments were already written, and there was no going back. I foolishly thought I stupid proofed my code enough, but as is the trend, my code was deemed unfinished, and I had to find more errors and squash them. I was pulling my hair out in frustration, and mostly stress. I had only a few days to finish this project, and there were so many things to fix! I worked for hours on end to finish the program and to have it deemed worthy by my almighty teacher. After several hours, a few tears shed, and many snacks consumed, I got the code debugged enough to be deemed a passing grade. I learned that using tuples and sets are quite inconvinent, especially when storing information like that in a library. Perhaps if it were a different project I would have actually remembered how they work, but alas, I do not. The second part of the personal library was supposed to use dictionaries, and that was a godsend. Dictionaries are now my favorite, I will not be taking any notes."],
        2:[movie,'movie reccomender',"""This is the Movie Reccomender, aka, the beginning of my struggles with CSVs. The premise of the code was to get movies from a csv and then use filters to then narrow down your results to fit those parameters, like actor, genre, length, ect. I went in with high hopes, and false confidence. I had just learned about how CSVs worked, and I did not remotely understood them as well as I thought I did. I casually programmed the code and submitted it confidently, when I got a glaring low score! It turns out that I had not done enough testing, and it did not help that the instructions were very vague. I was fed up with the code! I then redid the code, so much to the point that I made a whole other file that was my second try. I, after fighting tooth and nail to get the code to work, got a passing score from my teacher. I had finally learned how to use python to read CSVs... kind of"""],
        3:[to_do_list,"To Do List","This is the next step in the CSV Saga, the to do list. It was meant to have the user be able to add, remove, and mark tasks as done on a text file. I had sort of figured out how to read CSVs, but I had no clue how to write to them. I had not an idea how to make them work, and that was a massive source of frustration. I scoured reddit, W3Schools, Google, and even Quora for answers, but none were yeilded to me. By this point, I had enough. I decided that CSVs were the bane of my existence, and that I hated them. After some explaination from friends, however, things gradually started to make sense. Granted, I still had to have 2 tries to get it right, but I was then left with an actually functioning peice of code! I would come to use these newfound CSV skills with my later projects, and it was quintessential."],
        4:[battle,"Battle Simulator","Here it was: my biggest project as of yet. The Battle Simulator, meant to have a battling game with individual stats that you can level up, and have characters that can you save between runs of the game so you don't have to restart every time. Of course, to make these characters save between loads, I had to use my age-old enemy: CSVs. Things were different this time, however. I had gained the upper hand. I initially just stole the code from my to do list and updated it to save the characters. The CSV evolved, the code evolved, and most importantly, I evolved. I finally knew how CSVs worked! All I needed to do now was to make a battle system. Easy, right? Apparently not. I ended up back at my desk at 10pm debugging and fixing my code, only for my code to, you guessed it, not to get a passing score. The next project was just upgrading the battle simulator, so I fixed it while adding new features, so the updated battle simulator and my original battle simulator would get the points for actually working. At least, thats what I assumed. It seemed I only got graded on the updated battle simulator! Which, in hindsight, makes sense, but it was rather a bother to fix."],
        5:[coin,"Coin Change Problem","The coin change problem, a classic in beginner programming classes, this one with a minor twist: We had to use CSVs in it. The premise of the coin change problem, if you're unfamilliar, is converting a total dollar amount to change. My teacher said it would be easy, and she did not dissapoint. I used my newfound CSV skills to add the coins and their values to the document and easlily fetch them to use for the conversions. From this I learned that you don't only have to seperate things with commas, but I used dashes to connect coins and values and then separated them into their own lists."],
        6:[word,"Word Counter","The Word counter was basically just letting someone upload a document and make a word count from it. In the beginning of my programming class, this would have been a huge struggle, however, with my text file skills, I could now read documents like it was second nature. I used spaces and new line indicators to find how many words there were, and it worked perfectly! This was my easiest project yet, I could not have completed it without my fight to get my proficiency with these file types."],
        7:[0,"Exit",'Thank you']}
    def choose():
        for x in list(projects.keys()): 
            print(f"{x}. {projects[x][1]}") #this is the number you choose
        choice=int_input("What function do you want?\n") 
        if choice not in list(projects.keys()):
            print("Option not in the given choices")
            choose() #stupid proofing
        else: return choice

    input('This portfolio is essentially a culmination of the six projects I have been most proud of, or worked the hardest on while in CS1400 2. Each of these projects served an important role in my programming journey, and I have gathered them all for you to tell you how they affected me, my knowledge, and of course, my mental state.\nPress Enter to continue\n')
    input('How to use:\nChoose the number of which project you want to see, press enter to see a brief description, and then press enter again to move on to run the project\nPress enter to continue')
    choice=choose()
    input(f'{projects[choice][2]}\nPress Enter to contunue')
    if projects[choice][0]==0:
        return #exit
    else:
        invoke(projects[choice][0])
    main()
main()