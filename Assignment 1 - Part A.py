# Assignment 1
# For this assignment you are welcomed to use other regex resources such a regex "cheat sheets" you find on the web.
# Before start working on the problems, here is a small example to help you understand how to write your own answers.
# In short, the solution should be written within the function body given, and the final result should be returned.
# Then the autograder will try to call the function and validate your returned result accordingly.

# Part A
# Find a list of all of the names in the following string using regex.

import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    names = re.findall("[A-Z][a-z]*", simple_string)
    return names

print(names())
