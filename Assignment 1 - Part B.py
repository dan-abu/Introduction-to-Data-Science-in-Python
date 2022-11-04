# Assignment 1
# For this assignment you are welcomed to use other regex resources such a regex "cheat sheets" you find on the web.
# Before start working on the problems, here is a small example to help you understand how to write your own answers.
# In short, the solution should be written within the function body given, and the final result should be returned.
# Then the autograder will try to call the function and validate your returned result accordingly.

# Part B
# The dataset file in assets/grades.txt contains a line separated list of people with their grade in a class.
# Create a regex to generate a list of just those students who received a B in the course.

import re
def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()

    grade_list = re.findall('(?:[A-Z][a-z]*[-]*(?:[A-Z][a-z]*)*\s)(?:[A-Z][a-z]*[:]\s)(?:B)', grades)
    name_list = []
    for x in grade_list:
        x = x[:-3]
        name_list.append(x)
    
    return name_list

print(grades())