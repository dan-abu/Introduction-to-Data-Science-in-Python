# Assignment 2
# For this assignment you'll be looking at 2017 data on immunizations from the CDC. Your datafile for this assignment
# is in assets/NISPUF17.csv. A data users guide for this, which you'll need to map the variables in the data to the questions
# being asked, is available at assets/NIS-PUF17-DUG.pdf. Note: you may have to go to your Jupyter tree
# (click on the Coursera image) and navigate to the assignment 2 assets folder to see this PDF file).

# Question 1
# Write a function called proportion_of_education which returns the proportion of children in the dataset who had a mother with the education levels equal to less than high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree.
# This function should return a dictionary in the form of (use the correct numbers, do not round numbers):
#     {"less than high school":0.2,
#     "high school":0.4,
#     "more than high school but not college":0.2,
#     "college":0.2}

def proportion_of_education():
    import numpy as np
    import pandas as pd
    CDC_data = pd.read_csv('assets/NISPUF17.csv')
    working_data = CDC_data
    edu_lv = pd.DataFrame(working_data.loc[:, 'EDUC1'])
    
    levels = {"less than high school": len(edu_lv[edu_lv['EDUC1']==1])/28465,
    "high school":len(edu_lv[edu_lv['EDUC1']==2])/28465,
    "more than high school but not college":len(edu_lv[edu_lv['EDUC1']==3])/28465,
    "college":len(edu_lv[edu_lv['EDUC1']==4])/28465}
    return levels

print(proportion_of_education())