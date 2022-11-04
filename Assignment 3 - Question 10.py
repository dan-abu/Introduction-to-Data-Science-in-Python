# Assignment 3
# All questions are weighted the same in this assignment. This assignment requires more individual learning then
# the last one did - you are encouraged to check out the pandas documentation to find functions or methods you might not
# have used yet, or ask questions on Stack Overflow and tag them as pandas and python related. All questions are worth the
# same number of points except question 1 which is worth 17% of the assignment grade.
# Note: Questions 3-13 rely on your question 1 answer.

# Question 10
# Create a new column with a 1 if the country's % Renewable value is at or above the median for all
# countries in the top 15, and a 0 if the country's % Renewable value is below the median.
# This function should return a series named HighRenew whose index is the country name sorted in ascending order of rank.

def answer_ten():
    q1 = answer_one()
    
    #Sorting df by % renewable
    q1.sort_values(by='Rank', ascending=True)
    
    #Creating new HighRenew column
    q1['HighRenew'] =  q1['% Renewable'].apply(lambda x: 1 if x >= q1['% Renewable'][0:15].median() else 0)
    
    return q1['HighRenew']

print(answer_ten())