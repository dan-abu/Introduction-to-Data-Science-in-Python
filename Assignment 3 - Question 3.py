# Assignment 3
# All questions are weighted the same in this assignment. This assignment requires more individual learning then
# the last one did - you are encouraged to check out the pandas documentation to find functions or methods you might not
# have used yet, or ask questions on Stack Overflow and tag them as pandas and python related. All questions are worth the
# same number of points except question 1 which is worth 17% of the assignment grade.
# Note: Questions 3-13 rely on your question 1 answer.

# Question 3
# What are the top 15 countries for average GDP over the last 10 years?
# This function should return a Series named avgGDP with 15 countries and their average GDP sorted in descending order.
def answer_three():
    #Adding avgGDP column
    hi = answer_one()
    stuff = hi.columns[10:20]
    avgGDP = hi[stuff].mean(axis=1).sort_values(ascending=False)
    
    return avgGDP

print(answer_three())