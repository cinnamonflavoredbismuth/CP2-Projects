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
def goal(total_goal,time,deposit): #How long it will take to save for a goal based on a weekly or monthly deposit
    if time==1:
           time_mes='week'
    elif time==2:
           time_mes='month'
    print(f'it will take you {int(total_goal/deposit)} {time_mes}s to reach your goal')
    return 
def interest(first_investment,monthly,years,rate,compounded):#Compound Interest Calculator
    
def budget():#Budget Allocator
    pass
def sale(): #Sale Price Calculator
    pass
def tip(): #Tip Calculator
    pass
def main():
    exit=False
    print('Welcome to your financial calculator')
    
    select=int(input('''What would you like to do?
              1. Calculate how long it will take to save based on a weekly or monthly deposit
              2. Compound Interest Calculator 
              3. Budget Allocator
              4. Sale Price Calculator
              5. Tip Calculator
              6. Exit\n'''))
    if select == 1:
                return goal(float(input('How much do you want to save up for?')),int(input("""What time frame do you want to count by?
                   1. Weeks
                   2. Months""")),float(input(f'How much money do you want to deposit per amount of time?')))
    elif select==2:
                return interest(float(input("How much money are you going to invest initialy?")),
                                float(input("How much do you want to add per month?")))
    elif select==3:
                return budget()
    elif select==4:
                return sale()
    elif select==5:
                return tip()
    else:
        return
main()