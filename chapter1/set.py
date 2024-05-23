# Define a function named "set" that takes an element and an array as input
def set(element, array):
    # Check if the element is present in the array
    if element in array:
        # If the element is present, print a message indicating it is in the given set
        print(element, " is in the given set!")
    else:
        # If the element is not present, print a message indicating it is not in the given set
        print(element, " is not in the given set")

# Define a variable 'e' and set it to the string 'Todd'
e = 'Todd'
# Define a variable 'a' and set it to a list containing several names
a = ['Michael', 'Dwight', 'Jim', 'Andy', 'Tod']

# Call the 'set' function with the variables 'e' and 'a' as arguments
set(e, a)