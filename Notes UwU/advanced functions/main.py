#Cecily Strong Advanced Functions Notes

# 1. What is a helper function?
#    a function that you write to call in another function"""
def is_int(user_input):
    try:
        int(user_input)
    except:
        # 8. What is recursion?
            #when you have a function inside of itself

        # 9. How does recursion work?
            #you call a function inside of itself and giving it new information
        print('not an int')
        user_input = is_int(input('how old are you?\n'))
    return user_input
def age():
    old=is_int(input('how old are you?\n'))
    print(f'cool. you are {old}')
#age()

# 2. What is the purpose of a helper function?
    #to be used in another function, so if a task is multiple tasks, you can make them easier to read 

# 3. What is an inner function?
    #a function that exists within another function  
def add(a):
    b = int(input("Give me a number"))

    def addition():
        print(a+b)

    addition()
#add(3)

# 4. What is the scope of a variable in a function WITH an inner function?
    #any variable in an outer function is accessible to the inner function. stuff in the inner function can't be accessed by the outer function
    
# 5. Why do we use inner functions?
    #so you dont have to return values.  only use them as needed

# 6. What is a closure function?
    #Allows your function to remember information across multiple functions. 
def add(a):

    def addition(b):
        print(a+b)

    return addition
base = add(10)

#print(base(5))
#EXAMPLE
def math(income):
    def perc(amount,type):
        percent = amount/income
        print(f"your {type} is ${amount}, and that is {percent} of yout income")
    return perc

def user_inputs(type):
    return int(input(f"what is your monthly {type}\n$"))

income = user_inputs("income")
rent = user_inputs("income")
utilities = user_inputs("income")
groceries = user_inputs("income")
transportation = user_inputs("income")

start = math()
# 7. Why do we write closure functions?
    #remembers values across multiple calls
