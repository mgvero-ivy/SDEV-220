#file name: __init__.py
#Author: Marko Gvero
#created: 2024-06-10
#Module 5 Programming Assignment - Testing

def sum(arg): #this function takes a list, tuple, or set of numbers and adds the values togther and returns the total
    total = 0
    for val in arg:
        total += val
    return total

'''Complete the following sections (and their sub-sections) to perform a unit test:

    Testing Your Code
    Writing Your First Test
    Executing Your First Test

At the end of the code file, use a multi-line comment to describe the test results in your own words.  What do the test results mean?'''