# Assignment 2
# For this assignment you'll be looking at 2017 data on immunizations from the CDC. Your datafile for this assignment
# is in assets/NISPUF17.csv. A data users guide for this, which you'll need to map the variables in the data to the questions
# being asked, is available at assets/NIS-PUF17-DUG.pdf. Note: you may have to go to your Jupyter tree
# (click on the Coursera image) and navigate to the assignment 2 assets folder to see this PDF file).

# Question 3
# It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child.
# Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it
# (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox. Return results by sex.
# This function should return a dictionary in the form of (use the correct numbers):
#     {"male":0.2,
#     "female":0.4}
# Note: To aid in verification, the chickenpox_by_sex()['female'] value the autograder is looking for starts with
# the digits 0.0077.

def chickenpox_by_sex():
    import numpy as np
    import pandas as pd
    CDC_data = pd.read_csv('assets/NISPUF17.csv')
    working_data = CDC_data
    q3 = working_data[['SEX', 'HAD_CPOX', 'P_NUMVRC']]
    q3['P_NUMVRC'] = q3['P_NUMVRC'].fillna(0)
    
    #Boys who have had chickenpox and were vaccinated
    b_mask = (q3['SEX'].eq(1)) & (q3['HAD_CPOX'].eq(1)) & (q3['P_NUMVRC'].gt(0))
    #Boys who haven't had chickenpox and were vaccinated
    nochix_b_mask = (q3['SEX'].eq(1)) & (q3['HAD_CPOX'].eq(2)) & (q3['P_NUMVRC'].gt(0))
    #Ratio of boys who have had chickenpox and were vaccinated VS boys who haven't had chickenpox and were vaccinated
    bchixv = q3.where(b_mask).dropna()
    nobchixv = q3.where(nochix_b_mask).dropna()
    
    #Girls who have had chickenpox and were vaccinated
    g_mask = (q3['SEX'].eq(2)) & (q3['HAD_CPOX'].eq(1)) & (q3['P_NUMVRC'].gt(0))
    #Girls who haven't had chickenpox and were vaccinated
    nochix_g_mask = (q3['SEX'].eq(2)) & (q3['HAD_CPOX'].eq(2)) & (q3['P_NUMVRC'].gt(0))
    #Ratio of girls who have had chickenpox and were vaccinated VS girls who haven't had chickenpox and were vaccinated
    gchixv = q3.where(g_mask).dropna()
    nogchixv = q3.where(nochix_g_mask).dropna()
    
    #Dictionary of boy and girl ratios
    gender_ratio = {'male': len(bchixv)/len(nobchixv), 'female': len(gchixv)/len(nogchixv)}
    return gender_ratio

print(chickenpox_by_sex())