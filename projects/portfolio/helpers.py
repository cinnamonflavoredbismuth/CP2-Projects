#Cecily Strong Portfolio Helpers
def int_input(msg): #has you choose until you use an integer
    while True:
        try:
            output=int(input(msg))
            break
        except ValueError:
            input("Invalid Input, please use integers")
    return output

def invoke(func): #basically lets you just call function because it doesn't only work from calling the list
    func()
