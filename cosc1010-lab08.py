# Ryan Dennis
# UWYO COSC 1010
# Submission Date 11/10/2024
# Lab 08
# Lab Section:14
# Sources, people worked with, help given to: Stack Overflow, Geeks For Geeks
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def check(string):
    new_string = ""
    if isinstance(string, int):
        new_string = int(string)
        return(new_string)
    elif isinstance(string, float):
        new_string = float(string)
        return("%.1f" % new_string)
    else:
        return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
while True:
    slope = input("What is the slope? Or type Exit to quit.")
    if slope.lower() != "exit":
        intercept = input("What is the y intercept?")
        lower = input("What is the lower bound?")
        upper = input("What is the upper bound?")
        if lower.isdigit() != True or upper.isdigit() != True:
            print("False")
        elif int(lower) >= int(upper):
            print("False")
        else:
            m = float(slope)
            b = float(intercept)
            lower_bound = int(lower)
            upper_bound = int(upper)
            for i in range (lower_bound, upper_bound+1):
                number = ((m*i)+b)
                print(number)
            break
    else:
        break
print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def root(a,b,c):
    number = (((b**2)-4*a*c))
    if number < 0:
        return 0
    else:
        return number**.5

def quadratic_formula():
    while True:
        a = input("What is the value of a? Or type exit to quit.")
        if a.lower() == "exit":
            break
        else:
            a = int(a)
            b = int(input("What is the value of b?"))
            c = int(input("What is the value of c?"))
            square_root = root(a,b,c)
            if square_root == 0:
                print("null")
                continue
            else:
                root_1 = (-b+square_root)/(2*a)
                print(root_1)
                root_2 = (-b-square_root)/(2*a)
                print(root_2)
                break
quadratic_formula()



