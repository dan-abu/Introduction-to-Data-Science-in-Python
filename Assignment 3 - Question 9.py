# Assignment 3
# All questions are weighted the same in this assignment. This assignment requires more individual learning then
# the last one did - you are encouraged to check out the pandas documentation to find functions or methods you might not
# have used yet, or ask questions on Stack Overflow and tag them as pandas and python related. All questions are worth the
# same number of points except question 1 which is worth 17% of the assignment grade.
# Note: Questions 3-13 rely on your question 1 answer.

# Question 9
# Create a column that estimates the number of citable documents per person. What is the correlation between the number
# of citable documents per capita and the energy supply per capita? Use the .corr() method, (Pearson's correlation).
# This function should return a single number.
# (Optional: Use the built-in function plot9() to visualize the relationship between Energy Supply per
# Capita vs. Citable docs per Capita)

def answer_nine():
    q1 = answer_one()
    
    #Creating estimated population column
    q1['Estim. pop.'] = q1['Energy Supply'] / q1['Energy Supply per Capita']
    
    #Creating citable docs per capita column and calculating the correlation
    q1['Citable docs per Capita'] = q1['Citable documents'] / q1['Estim. pop.']
    corr_ans = q1['Citable docs per Capita'].corr(q1['Energy Supply per Capita'])
    
    return corr_ans

print(answer_nine())