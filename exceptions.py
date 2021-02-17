
# Handle the exceptions gracefully:

import sys

try: # try to take input values
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError: # except when the input is a non-integer value which causes ValueError
    print("Error: Invalid input")
    sys.exit(1)

try: #try to execute this line
    result = x / y
except ZeroDivisionError: # except when there is a division by 0, then return an error message
    print("Error: Cannot divide by 0")
    sys.exit(1) # exit the program with status code = 1; where status code 1 means that smt went wrong

print(f"{x} / {y} = {result}") #  problem: when y=0, then error is displayed; we should be able to catch it