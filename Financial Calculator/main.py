#Cecily Strong Financial Calculator
#this is the financial calculator program
'''
-How long it will take to save for a goal based on a weekly or monthly deposit
-Compound Interest Calculator 
-Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
-Sale Price Calculator (apply discounts to prices)
-Tip Calculator
'''
def goal(): #How long it will take to save for a goal based on a weekly or monthly deposit
    pass
def interest():#Compound Interest Calculator
    pass
def budget():#Budget Allocator
    pass
def sale(): #Sale Price Calculator
    pass
def tip(): #Tip Calculator
    pass
def main():
    exit=False
    print('Welcome to your financial calculator')
    try:
        select=int(input('''What would you like to do?
              1. Calculate how long it will take to save based on a weekly or monthly deposit
              2. Compound Interest Calculator 
              3. Budget Allocator
              4. Sale Price Calculator
              5. Tip Calculator'''))
        if select==1:
                goal()
        elif select==2:
                interest()
        elif select==3:
                budget()
        elif select==4:
                sale()
        elif select==5:
                tip()
    except:
        print('invalid number')
    try:
        select=int(input("""Would you like to exit?
                     1. Yes
                     2. No"""))
        if select==2:
            exit=False
        else:
            exit=True
    
    except:
        print('invalid number')
    print(exit)
    if exit==False:
        main()
    else:
         print('exit')
main()