def options(list):
    print("press the number of what you want")
    for x in list:
        print(f"{list.index(x)+1}. {x}")
        
def print_lots(list):
    for x in list:
        print(x)