#Cecily Strong Writing to files notes

"""
r = to read on file
w = write on the file (replaces old file)
w+ = read and write
a = append (add so the file, doesn't delete them) (create a file if it doesn't exist)
x = create a file
a+ = append and read
"""
import csv

with open("Notes UwU/reading_files/user_info.csv", "w") as file:
    file.write("computer science!")
    print(file.read())