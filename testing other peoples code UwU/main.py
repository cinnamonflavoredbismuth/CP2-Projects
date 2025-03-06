import csv
with open("to do list/list.csv","r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(row)