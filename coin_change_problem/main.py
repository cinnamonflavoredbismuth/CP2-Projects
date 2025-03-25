#Cecily Strong Coin Change Problem
import csv
def debug():
    import trace
    import sys
    def trace_calls(frame,event,argument):
        func=frame.f_code.co_name
        ignore=['__init__','_shutdown','ident','_stop','daemon','_maintain_shutdown_locks']
        if func in ignore:
            pass
        else:
            if event == 'call': #when function is called
                #f_code: the file
                #co_name: the function
                #f_code.co_name: function name
                print(f'Calling function: {frame.f_code.co_name}')

            elif event == 'line': #when a new line of code happens
                #lineno: line number
                print(f'    Executing line {frame.f_lineno} in {frame.f_code.co_name}')

            elif event == 'return': #When we return stuff
                print(f'    {frame.f_code.co_name} returned {argument}')

            elif event == 'exception': #Triggered when there is an exception
                print(f'    Exeption in {frame.f_code.co_name}: {argument}')

        return trace_calls
    sys.settrace(trace_calls)
    tracer=trace.Trace(count=False,trace=True)
def coins_dict():
    with open("coin_change_problem\coin_denomination.csv","r",newline='') as file:
        coins={}
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            coins[row[0]]=row[1:]
            return coins

def country_coins(country):
    with open("coin_change_problem\coin_denomination.csv","r",newline='') as file:
        coins={}
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0].lower()==country.lower():
                coins[row[0]]=row[1:]
                return coins
        else:
            return False
        
def split_coins(coins):
    for x in list(coins.keys()):
        dic={}
        for y in coins[x]:
            z=y.split('-')
            dic[z[1]]=z[0]
        coins[x]=dic
    return coins



def coin_change(country,amount):
    amount=float(amount)
    coins=split_coins(country_coins(country))
    print(coins)
    keys=[]
    for x in list(coins['usa'].keys()):
        keys.append(float(x))
    keys.sort(reverse=True)
    coins_list=[]
    for x in keys:
        div=amount//x
        amount=amount-div
        coins_list.append(f'{div} {coins[str(x)]}(s)')
    return coins_list
print(coin_change('usa',5.30))