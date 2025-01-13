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
def (): #How long it will take to save for a goal based on a weekly or monthly deposit
    total_goal=float(input('How much do you want to save up for?')),
    time=int(input("""What time frame do you want to count by?
                   1. Weeks
                   2. Months""")),
    deposit=float(input(f'How much money do you want to deposit per amount of time?'))
    if time==1:
           time_mes='week'
    elif time==2:
           time_mes='month'
    else:
           print("invalid option")
    print(f'it will take you {int(total_goal/deposit)} {time_mes}s to reach your goal')
    return 
def interest():#Compound Interest Calculator
    p=float(input("How much money are you going to invest initialy?"))
    t=int(input("How many years do you want this to go?"))
    r=float(input("What is the interest rate?"))
    n=int(input("How many times per year will this be compounded?"))
    print(f"${(p*(1 + r/n)**(n*t)):.2f}")
    return
def budget():#Budget Allocator
    money=float(input("How much money do you want to budget?"))
    print(f"you should put ${20%money:.2f} into savings, ${30%money:.2f} in to entertainment, and ${15%money:.2f} in to food")
    return
def sale(): #Sale Price Calculator
    price=float(input("What was the original price?"))
    sale=float(input("What was the sale percentage?"))
    print(f"After sale, the price would be ${price-(sale%price):.2f}")
    return
def tip(): #Tip Calculator
    price=float(input("How much did you spend on your meal?"))
    print(f"You should tip ${15%price:.2f} to your server")
    return
def main():
    print('Welcome to your financial calculator')
    
    select=int(input('''What would you like to do?
              1. Calculate how long it will take to save based on a weekly or monthly deposit
              2. Compound Interest Calculator 
              3. Budget Allocator
              4. Sale Price Calculator
              5. Tip Calculator
              6. Exit\n'''))
    if select == 1:
                return goal()
    elif select==2:
                return interest()
    elif select==3:
                return budget()
    elif select==4:
                return sale()
    elif select==5:
                return tip()
    elif select==6:
        return
    else:
        print("Invalid option")
        main()
main()