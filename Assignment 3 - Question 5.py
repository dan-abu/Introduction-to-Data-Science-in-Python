# Assignment 3
# All questions are weighted the same in this assignment. This assignment requires more individual learning then
# the last one did - you are encouraged to check out the pandas documentation to find functions or methods you might not
# have used yet, or ask questions on Stack Overflow and tag them as pandas and python related. All questions are worth the
# same number of points except question 1 which is worth 17% of the assignment grade.
# Note: Questions 3-13 rely on your question 1 answer.

# Question 5
# What is the mean energy supply per capita?
# This function should return a single number.

def answer_five():
    five = answer_one()
    return five['Energy Supply per Capita'].mean()

print(answer_five())