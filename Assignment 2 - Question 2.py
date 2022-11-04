# Assignment 2
# For this assignment you'll be looking at 2017 data on immunizations from the CDC. Your datafile for this assignment
# is in assets/NISPUF17.csv. A data users guide for this, which you'll need to map the variables in the data to the questions
# being asked, is available at assets/NIS-PUF17-DUG.pdf. Note: you may have to go to your Jupyter tree
# (click on the Coursera image) and navigate to the assignment 2 assets folder to see this PDF file).

# Question 2
# Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine
# from a healthcare provider. Return a tuple of the average number of influenza vaccines for those children we know
# received breastmilk as a child and those who know did not.
# This function should return a tuple in the form (use the correct numbers:
# (2.5, 0.1)

def average_influenza_doses():
    import numpy as np
    import pandas as pd
    CDC_data = pd.read_csv('assets/NISPUF17.csv')
    working_data = CDC_data
    food_flu = working_data[['CBF_01', 'P_NUMFLU']]
    
    #Number of children who received breastmilk
    bf = food_flu[food_flu['CBF_01'].eq(1)].dropna()
    #Number of children who did not receive breastmilk
    no_bf = food_flu[food_flu['CBF_01'].eq(2)].dropna()
    
    av1 = np.sum(bf['P_NUMFLU'])/len(bf)
    av2 = np.sum(no_bf['P_NUMFLU'])/len(no_bf)
    return (av1, av2)

print(average_influenza_doses())