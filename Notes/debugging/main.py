# Cecily Strong Debugging Notes
import trace
import sys
#frame: current run. the now
#event: type of thing that is happening
#argument: the information being used
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
# 1. What is tracing?
def sub(a,b):
    return a-b
def add(a,b):
    print(sub(a,b))
    return a+b
print(add(1,2))

#tracer.run('add(1,2)')
#Basic tracing command
    #python -m trace --trace [file path]
'''
    --trace (display lines as executed)
    --count (displays number of times executed)
    --listfucns (displays the functions executed by running the program)
    --trackcalls (displays relationships between functions)
    '''

    #Tracing is basically just running the program and walking through each step that it normally does in the background
#IGNORE THESE
"""
__init__
_shutdown
ident
_stop
daemon
_maintain_shutdown_locks
"""
# 2. What are some ways we can debug by tracing?
    # track path and see where bugs occur

# 3. How do you access the debugger in VS Code?
    #f5 
    #debugger screen on left
    #right click and click debug

# 4. What is testing?
    #when you run your code to make sure it runs as required

# 5. What are boundary conditions?
    #check the entries most likely to be wrong

# 6. How do you handle when users give strange inputs?
    #return an error message and send them to menu