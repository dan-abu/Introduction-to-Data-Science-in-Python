# Assignment 2
# For this assignment you'll be looking at 2017 data on immunizations from the CDC. Your datafile for this assignment
# is in assets/NISPUF17.csv. A data users guide for this, which you'll need to map the variables in the data to the questions
# being asked, is available at assets/NIS-PUF17-DUG.pdf. Note: you may have to go to your Jupyter tree
# (click on the Coursera image) and navigate to the assignment 2 assets folder to see this PDF file).

# Question 4
# A correlation is a statistical relationship between two variables. If we wanted to know if vaccines work, we might look at the
# correlation between the use of the vaccine and whether it results in prevention of the infection or disease [1]. In this
# question, you are to see if there is a correlation between having had the chicken pox and the number of chickenpox vaccine
# doses given (varicella).
# Some notes on interpreting the answer. The had_chickenpox_column is either 1 (for yes) or 2 (for no), and the
# num_chickenpox_vaccine_column is the number of doses a child has been given of the varicella vaccine.
# A positive correlation (e.g., corr > 0) means that an increase in had_chickenpox_column (which means more no’s) would also
# increase the values of num_chickenpox_vaccine_column (which means more doses of vaccine). If there is
# a negative correlation (e.g., corr < 0), it indicates that having had chickenpox is related to an increase in the
# number of vaccine doses.
# Also, pval is the probability that we observe a correlation between had_chickenpox_column and num_chickenpox_vaccine_column
# which is greater than or equal to a particular value occurred by chance. A small pval means that the observed correlation is
# highly unlikely to occur by chance. In this case, pval should be very small (will end in e-18 indicating a very small number).
# [1] This isn’t really the full picture, since we are not looking at when the dose was given. It’s possible that children had
# chickenpox and then their parents went to get them the vaccine. Does this dataset have the data we would need to investigate
# the timing of the dose?

def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    
    # this is just an example dataframe
    #df=pd.DataFrame({"had_chickenpox_column":np.random.randint(1,3,size=(100)),
                   #"num_chickenpox_vaccine_column":np.random.randint(0,6,size=(100))})

    # here is some stub code to actually run the correlation
    #corr, pval=stats.pearsonr(df["had_chickenpox_column"],df["num_chickenpox_vaccine_column"])
    
    # just return the correlation
    #return corr
    CDC_data = pd.read_csv('assets/NISPUF17.csv')
    working_data = CDC_data
    q4 = working_data[['HAD_CPOX', 'P_NUMVRC']]
    q4['HAD_CPOX'] = q4[q4['HAD_CPOX']<3]
    q4 = q4.dropna()
    corr, pval=stats.pearsonr(q4['HAD_CPOX'],q4['P_NUMVRC'])
    return corr

print(corr_chickenpox())