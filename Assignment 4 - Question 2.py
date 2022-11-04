# Assignment 4

# Description
# In this assignment you must read in a file of metropolitan regions and associated sports teams from
# assets/wikipedia_data.html and answer some questions about each metropolitan region. Each of these regions may
# have one or more teams from the "Big 4": NFL (football, in assets/nfl.csv), MLB (baseball, in assets/mlb.csv),
# NBA (basketball, in assets/nba.csv or NHL (hockey, in assets/nhl.csv). Please keep in mind that all questions are
# from the perspective of the metropolitan region, and that this file is the "source of authority" for the location of a
# given sports team. Thus teams which are commonly known by a different area (e.g. "Oakland Raiders") need to be mapped into the
# metropolitan region given (e.g. San Francisco Bay Area). This will require some human data understanding outside of the data
# you've been given (e.g. you will have to hand-code some names, and might need to google to find out where teams are)!
# For each sport I would like you to answer the question: what is the win/loss ratio's correlation with the
# population of the city it is in? Win/Loss ratio refers to the number of wins over the number of wins plus the number of
# losses. Remember that to calculate the correlation with pearsonr, so you are going to send in two ordered lists of values, the
# populations from the wikipedia_data.html file and the win/loss ratio for a given sport in the same order. Average the
# win/loss ratios for those cities which have multiple teams of a single sport. Each sport is worth an equal amount in this
# assignment (20%*4=80%) of the grade for this assignment. You should only use data from year 2018 for your analysis -- this is
# important!

# Notes
# Do not include data about the MLS or CFL in any of the work you are doing, we're only interested in the Big 4 in this assignment.
# I highly suggest that you first tackle the four correlation questions in order, as they are all similar and worth the majority of grades for this assignment. This is by design!
# It's fair game to talk with peers about high level strategy as well as the relationship between metropolitan areas and sports teams. However, do not post code solving aspects of the assignment (including such as dictionaries mapping areas to teams, or regexes which will clean up names).
# There may be more teams than the assert statements test, remember to collapse multiple teams in one city into a single value!

Question 2
For this question, calculate the win/loss ratio's correlation with the population of the city it is
in for the NBA using 2018 data.

def nba_correlation():
    import pandas as pd
    import numpy as np
    import scipy.stats as stats
    import re

    nba_df=pd.read_csv("assets/nba.csv")
    cities=pd.read_html("assets/wikipedia_data.html")[1]
    cities=cities.iloc[:-1,[0,3,5,6,7,8]]
     #Cleaning up the format of the cities data
    phrase = '[[].+[]]'
    cities = (cities.replace(to_replace=phrase, value='', regex=True)
            .rename(columns = {'Population (2016 est.)[8]': 'Pop.'})
            .replace(r'^\s*$', np.nan, regex=True)
            .replace(r'^\u2014$', np.nan, regex=True)
            .sort_values('Metropolitan area', ascending=True)
             )
    cities.set_index('Metropolitan area', inplace=True)
    cities['Pop.'] = cities['Pop.'].apply(lambda x: int(x))
    
    #Arranging NBA data
    nba_df = nba_df[nba_df['year'].eq(2018)]
    nba_df['W/L%'] = nba_df['W/L%'].apply(lambda x: float(x))
    nba_states = ['Toronto', 'Boston', 'Philadelphia', 'Cleveland', 'Indianapolis', 'Miami–Fort Lauderdale',
             'Milwaukee', 'Washington, D.C.', 'Detroit', 'Charlotte', 'New York City', 'New York City',
             'Chicago', 'Orlando', 'Atlanta', 'Houston', 'San Francisco Bay Area', 'Portland',
             'Oklahoma City', 'Salt Lake City', 'New Orleans', 'San Antonio', 'Minneapolis–Saint Paul',
             'Denver', 'Los Angeles', 'Los Angeles', 'Sacramento', 'Dallas–Fort Worth', 'Memphis',
             'Phoenix']
    nba_df['state'] = nba_states
    cities['NBA W/L'] = nba_df.groupby('state')['W/L%'].mean()
    
    #Creating a new df with no blanks of the population and state W/L ratio data
    nba_stats = cities[['Pop.', 'NBA W/L']].dropna()
    
    population_by_region = nba_stats['Pop.'].to_list() # pass in metropolitan area population from cities
    win_loss_by_region = nba_stats['NBA W/L'].to_list() # pass in win/loss ratio from nba_df in the same order as cities["Metropolitan area"]

    assert len(population_by_region) == len(win_loss_by_region), "Q2: Your lists must be the same length"
    assert len(population_by_region) == 28, "Q2: There should be 28 teams being analysed for NBA"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]

print(nba_correlation())