# Assignment 1
# For this assignment you are welcomed to use other regex resources such a regex "cheat sheets" you find on the web.
# Before start working on the problems, here is a small example to help you understand how to write your own answers.
# In short, the solution should be written within the function body given, and the final result should be returned.
# Then the autograder will try to call the function and validate your returned result accordingly.

# Part C
# Consider the standard web log file in assets/logdata.txt. This file records the access a user makes when visiting a web page (like this one!). Each line of the log has the following items:
# a host (e.g., '146.204.224.152')
# a user_name (e.g., 'feest6811' note: sometimes the user name is missing! In this case, use '-' as the value for the username.)
# the time a request was made (e.g., '21/Jun/2019:15:45:24 -0700')
# the post request type (e.g., 'POST /incentivize HTTP/1.1' note: not everything is a POST!)
# Your task is to convert this into a list of dictionaries, where each dictionary looks like the following:
# example_dict = {"host":"146.204.224.152", 
#                 "user_name":"feest6811", 
#                 "time":"21/Jun/2019:15:45:24 -0700",
#                 "request":"POST /incentivize HTTP/1.1"}

import re
def logs():
    with open("assets/logdata.txt", "r") as file:
        logdata = file.read()
    
    pattern = '(\d+[.]\d+[.]\d+[.]\d+) - ([a-z-]\S*) .+(21\/Jun\/2019[:]\d+[:]\d+[:]\d+\s[-]0700)\] "([A-Z]\S+ \/\S+ HTTP\/\d{1}[.]\d{1})'
    all_data = re.findall(pattern, logdata)
    finaldict = []
    for x in all_data:
        x = {'host': x[0], 'user_name': x[1], 'time': x[2], 'request': x[3]}
        finaldict.append(x)
        
    return finaldict