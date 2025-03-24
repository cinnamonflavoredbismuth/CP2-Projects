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
#import pandas

data=[
    {"username":'hi','color':'blue'}
    ]
with open("Notes UwU/reading_files/user_info.csv","a",newline="") as file:
    fieldnames=['']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

with open("Notes UwU/reading_files/user_info.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{reader.id(row)}: {row[0]}\n{row[1]} \n ----------------------------")
