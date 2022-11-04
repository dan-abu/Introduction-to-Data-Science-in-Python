# Assignment 3
# All questions are weighted the same in this assignment. This assignment requires more individual learning then
# the last one did - you are encouraged to check out the pandas documentation to find functions or methods you might not
# have used yet, or ask questions on Stack Overflow and tag them as pandas and python related. All questions are worth the
# same number of points except question 1 which is worth 17% of the assignment grade.
# Note: Questions 3-13 rely on your question 1 answer.

# Question 8
# Create a column that estimates the population using Energy Supply and Energy Supply per capita. What is the third
# most populous country according to this estimate?
# This function should return the name of the country

def answer_eight():
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
    task1_df.set_index('Country', inplace=True) 
    q1 = task1_df
    
    #Creating estimated population column
    q1['Estim. pop.'] = q1['Energy Supply'] / q1['Energy Supply per Capita']
    q1.sort_values(by='Estim. pop.', ascending=False, inplace=True)
    
    return q1.index[2]

print(answer_eight())