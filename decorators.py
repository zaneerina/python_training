# functional programming - a function can  be passed to another function
# decorator - takes a function and adds a capability to it

def announce(f): # decorator function - takes a function, modifies it & returns the modified version;
    def wrapper():
        print("About to run the function...")
        f() # hello() function
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello!")

hello() # run the function