# Assignment 3
# All questions are weighted the same in this assignment. This assignment requires more individual learning then
# the last one did - you are encouraged to check out the pandas documentation to find functions or methods you might not
# have used yet, or ask questions on Stack Overflow and tag them as pandas and python related. All questions are worth the
# same number of points except question 1 which is worth 17% of the assignment grade.
# Note: Questions 3-13 rely on your question 1 answer.

# Question 6
# What country has the maximum % Renewable and what is the percentage?
# This function should return a tuple with the name of the country and the percentage.

def answer_six():
    six = answer_one()
    #Returning one country and its percentage in a tuple
    six_ans = (six.loc[six['% Renewable'].eq(six['% Renewable'].max())].index[0], six['% Renewable'].max())
    return six_ans

print(answer_six())