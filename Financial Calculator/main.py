#Cecily Strong Financial Calculator
#this is the financial calculator program
#A = P(1 + r/n)^nt
'''
-How long it will take to save for a goal based on a weekly or monthly deposit
-Compound Interest Calculator 
-Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
-Sale Price Calculator (apply discounts to prices)
-Tip Calculator
'''
def goal(): #How long it will take to save for a goal based on a weekly or monthly deposit
    try:
        total_goal=float(input('How much do you want to save up for?\n'))
    except:
        print("Invalid option\n")
        goal()
    try:
        time=input("what are we counting by?\n") 
    except:
        print("Invalid option\n")
        goal()
    try:         
        deposit=float(input(f'How much money do you want to deposit per {time.replace("s","")}?\n'))
    except:
        print("Invalid option\n")
        goal()
    print
    print(f'it will take you {total_goal/deposit} {time} to reach your goal\n')
    return 
def interest():#Compound Interest Calculator
    try:
        p=float(input("How much money are you going to invest initialy?\n"))
    except:
        print("Invalid option\n")
        interest()
    try:    
        t=int(input("How many years do you want this to go?\n"))
    except:
        print("Invalid option\n")
        interest()
    try:    
        r=float(input("What is the interest rate?\n"))
    except:
        print("Invalid option\n")
        interest() 
    try:   
        n=int(input("How many times per year will this be compounded?\n"))
    except:
        print("Invalid option\n")
        interest()
    print(f"${(p*(1 + r/n)**(n*t)):.2f}")
    return
def budget():#Budget Allocator
    try:
        money=float(input("How much money do you want to budget?"))
    except:
        print("Invalid option\n")
        budget()
    print(f"you should put ${20%money:.2f} into savings, ${30%money:.2f} in to entertainment, and ${15%money:.2f} in to food\n") #using reccomended budgeting methods
    return
def sale(): #Sale Price Calculator
    try:
        price=float(input("What was the original price?\n"))
    except:
        print("Invalid option\n")
        sale()
    try:
        sale=float(input("What was the sale percentage?\n"))
    except:
        print("Invalid option\n")
        sale()
    print(f"After sale, the price would be ${price-(sale%price):.2f}\n")
    return
def tip(): #Tip Calculator
    try:
        price=float(input("How much did you spend on your meal?\n"))
    except:
        print("Invalid option\n")
        tip()
    print(f"You should tip ${15%price:.2f} to your server\n")#using the normal 15% of your meal price is the tip rule
    return
def main():
    print('Welcome to your financial calculator') 
    try:
        select=int(input('''What would you like to do?
              1. Calculate how long it will take to save based on a weekly or monthly deposit
              2. Compound Interest Calculator 
              3. Budget Allocator
              4. Sale Price Calculator
              5. Tip Calculator
              6. Exit\n'''))
        if select == 1:
            goal()
            main()#using this so the function doesn't just end when you are finished with the finances
        elif select==2:
                interest()
                main()
        elif select==3:
                budget()
                main()
        elif select==4:
                sale()
                main()
        elif select==5:
                tip()
                main()
        elif select==6:
            return
    except:
        print("Invalid option\n")
        main()
main()