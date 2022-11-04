# Assignment 3
# All questions are weighted the same in this assignment. This assignment requires more individual learning then
# the last one did - you are encouraged to check out the pandas documentation to find functions or methods you might not
# have used yet, or ask questions on Stack Overflow and tag them as pandas and python related. All questions are worth the
# same number of points except question 1 which is worth 17% of the assignment grade.
# Note: Questions 3-13 rely on your question 1 answer.

# Question 1
# Load the energy data from the file assets/Energy Indicators.xls, which is a list of indicators of energy supply and
# renewable electricity production from the United Nations for the year 2013, and should be put into a DataFrame with the
# variable name of Energy.
# Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and
# header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should
# change the column labels so that the columns are: ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable]
# Convert Energy Supply to gigajoules (Note: there are 1,000,000 gigajoules in a petajoule). For all countries which have
# missing data (e.g. data with "...") make sure this is reflected as np.NaN values.
# Rename the following list of countries (for use in later questions):
# "Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"
# There are also several countries with numbers and/or parenthesis in their name. Be sure to remove
# these, e.g. 'Bolivia (Plurinational State of)' should be 'Bolivia'.  'Switzerland17' should be 'Switzerland'.
# Next, load the GDP data from the file assets/world_bank.csv, which is a csv containing
# countries' GDP from 1960 to 2015 from World Bank. Call this DataFrame GDP.
# Make sure to skip the header, and rename the following list of countries:
# "Korea, Rep.": "South Korea", 
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"
# Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from
# the file assets/scimagojr-3.xlsx, which ranks countries based on their journal contributions in the aforementioned area.
# Call this DataFrame ScimEn.
# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names).
# Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).
# The index of this DataFrame should be the name of the country, and the columns
# should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'].
# This function should return a DataFrame with 20 columns and 15 entries, and the rows of
# the DataFrame should be sorted by "Rank".

import pandas as pd

def answer_one():
    import pandas as pd
    import numpy as np
    import functools
    import warnings
    warnings.filterwarnings('ignore')
    from pandas import ExcelWriter
    from pandas import ExcelFile
    from functools import reduce
    
    #Adding and cleaning the energy excel
    Energy_excel = pd.read_excel('assets/Energy Indicators.xls')
    Energy = pd.DataFrame(Energy_excel)
    del Energy['Unnamed: 0']
    del Energy['Unnamed: 1']
    one_index = range(17)
    two_index = range(244, 282)
    del_list1 = []
    del_list2 = []
    for x in one_index:
        del_list1.append(x)
    for x in two_index:
        del_list2.append(x)
    Energy.drop(del_list1, inplace=True)
    Energy.drop(del_list2, inplace=True)
    Energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    Energy.replace('...', np.nan, inplace=True)
    Energy['Energy Supply'] = Energy['Energy Supply'].apply(lambda x: x * 1000000)
    new_countries = {"Republic of Korea": "South Korea",
                "United States of America20": "United States",
                "United Kingdom of Great Britain and Northern Ireland19": "United Kingdom",
                "China, Hong Kong Special Administrative Region3": "Hong Kong",
                "Bolivia [(]Plurinational State of[)]": "Bolivia",
                "Switzerland17": "Switzerland",
                "Australia1": "Australia",
                "China2": "China",
                "China, Macao Special Administrative Region4": "Macao",
                "Denmark5": "Denmark",
                "Falkland Islands [(]Malvinas[)]": "Falkland Islands",
                "France6": "France",
                "Greenland7": "Greenland",
                "Indonesia8": "Indonesia",
                "Iran [(]Islamic Republic of[)]": "Iran",
                "Italy9": "Italy",
                "Japan10": "Japan",
                "Kuwait11": "Kuwait",
                "Micronesia [(]Federated States of[)]": "Micronesia",
                "Netherlands12": "Netherlands",
                "Portugal13": "Portugal",
                "Saudi Arabia14": "Saudi Arabia",
                "Serbia15": "Serbia",
                "Sint Maarten [(]Dutch part[)]": "Sint Maarten",
                "Spain16": "Spain",
                "Ukraine18": "Ukraine",
                "Venezuela [(]Bolivarian Republic of[)]": "Venezuela"}
    Energy['Country'].replace(new_countries, inplace=True, regex=True)
    
    #Adding and cleaning the GDP data
    WBdata = pd.read_csv('assets/world_bank.csv')
    GDP = pd.DataFrame(WBdata)
    GDP.drop([0,1,2], inplace=True)
    row_labels = []
    for x in GDP.loc[3]:
        row_labels.append(x)
    GDP.columns = row_labels
    GDP.drop([3], inplace=True)
    WBcountries = {"Korea, Rep[.]": "South Korea", 
            "Iran, Islamic Rep[.]": "Iran",
            "Hong Kong SAR, China": "Hong Kong"}
    GDP['Country Name'].replace(WBcountries, inplace=True, regex=True)
    new_columns = []
    for x in GDP.columns[0:4]:
        new_columns.append(x)
    GDP_column_years = range(1960, 2016)
    for x in GDP_column_years:
        new_columns.append(x)
    GDP.columns = new_columns
    GDP.rename(columns={'Country Name': 'Country'}, inplace=True)
    
    #Adding and cleaning journal data
    SciData = pd.read_excel('assets/scimagojr-3.xlsx')
    ScimEn = pd.DataFrame(SciData)
    
    #Merging the 3 df's and cleaning the final df
    dfs = [ScimEn, Energy, GDP]
    task1_df = reduce(lambda left,right: pd.merge(left,right,on=['Country'],how='inner'), dfs)
    years2drop = []
    years = range(1960, 2006)
    for year in years:
        years2drop.append(year)
    task1_df.drop(years2drop, axis=1, inplace=True) 
    task1_df.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis=1, inplace=True)
    task1_df.columns = task1_df.columns.astype(str)
    task1_df.set_index('Country', inplace=True)
    first_answer = task1_df
    first_answer = first_answer[first_answer['Rank'].lt(16)]
    
    return first_answer

print(answer_one())