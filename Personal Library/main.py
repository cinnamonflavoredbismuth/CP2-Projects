#Cecily Strong Personal Library Program

def main():
    run=True
    while run==True:
        try:
            select=int(input("""What would you like to do?
                     1. Display all items
                     2. Search items
                     3. Add a new item
                     4. Remove an item
                     5. Exit"""))
            if select==1:
                pass
            elif select==2:
                pass
            elif select==3:
                pass
            elif select==4:
                pass
            elif select==5:
                print("Thank you")
                run=False
                return
        except:
            print("invalid option")