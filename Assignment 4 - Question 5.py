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

# Question 5
# In this question I would like you to explore the hypothesis that given that an area has two sports teams in different sports,
# those teams will perform the same within their respective sports. How I would like to see this explored is with a series
# of paired t-tests (so use ttest_rel) between all pairs of sports. Are there any sports where we can reject the null hypothesis?
# Again, average values where a sport has multiple teams in one region. Remember, you will only be including, for each sport,
# cities which have teams engaged in that sport, drop others as appropriate. This question is worth 20% of the grade for this
# assignment.

def sports_team_performance():
    import pandas as pd
    import numpy as np
    import scipy.stats as stats
    import re

    mlb_df=pd.read_csv("assets/mlb.csv")
    nhl_df=pd.read_csv("assets/nhl.csv")
    nba_df=pd.read_csv("assets/nba.csv")
    nfl_df=pd.read_csv("assets/nfl.csv")
    cities=pd.read_html("assets/wikipedia_data.html")[1]
    cities=cities.iloc[:-1,[0,3,5,6,7,8]]

    #Cleaning up the format of the cities data
    phrase = '[[].+[]]'
    cities = (cities.replace(to_replace=phrase, value='', regex=True)
            .rename(columns = {'Population (2016 est.)[8]': 'Pop.'})
            .replace(r'^\s*$', np.nan, regex=True)
            .replace(r'^\u2014$', np.nan, regex=True)
            .replace(r'^-$', np.nan, regex=True)
            .sort_values('Metropolitan area', ascending=True)
             )
    cities.set_index('Metropolitan area', inplace=True)
    cities['Pop.'] = cities['Pop.'].apply(lambda x: int(x))

    #Cleaning up and arranging the NHL data
    nhl_df = (nhl_df[nhl_df['year'].eq(2018)])
    nhl_df.drop([0,9,18,26], inplace=True)
    nhl_df['W'] = nhl_df['W'].apply(lambda x: int(x))
    nhl_df['L'] = nhl_df['L'].apply(lambda x: int(x))
    nhl_df['W/L ratio'] = nhl_df['W'] / (nhl_df['W'] + nhl_df['L'])

    #Assigning NHL teams to states
    nhl_states = ['Tampa Bay Area', 'Boston', 'Toronto', 'Miami–Fort Lauderdale',
                 'Detroit', 'Montreal', 'Ottawa', 'Buffalo', 'Washington, D.C.', 'Pittsburgh',
                 'Philadelphia', 'Columbus', 'New York City', 'Raleigh', 'New York City', 'New York City',
                 'Nashville', 'Winnipeg', 'Minneapolis–Saint Paul', 'Denver', 'St. Louis', 'Dallas–Fort Worth',
                 'Chicago', 'Las Vegas', 'Los Angeles', 'San Francisco Bay Area', 'Los Angeles',
                 'Calgary', 'Edmonton', 'Vancouver', 'Phoenix']
    nhl_df['state'] = nhl_states

    #Calculating avg W/L ratio per state
    cities['NHL W/L'] = nhl_df.groupby('state')['W/L ratio'].mean()

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

    #Sorting MLB data
    mlb_df = mlb_df[mlb_df['year'].eq(2018)]
    mlb_states = ['Phoenix', 'Atlanta', 'Baltimore', 'Boston', 'Chicago', 'Chicago', 'Cincinnati', 'Cleveland',
             'Denver', 'Detroit', 'Houston', 'Kansas City', 'Los Angeles', 'Los Angeles', 'Miami–Fort Lauderdale',
             'Milwaukee', 'Minneapolis–Saint Paul', 'New York City', 'New York City', 'San Francisco Bay Area',
             'Philadelphia', 'Pittsburgh', 'San Diego', 'San Francisco Bay Area', 'Seattle',
             'St. Louis', 'Tampa Bay Area', 'Dallas–Fort Worth', 'Toronto', 'Washington, D.C.']
    mlb_df['state'] = mlb_states
    cities['MLB W/L'] = mlb_df.groupby('state')['W-L%'].mean()

    #Sorting nfl data
    nfl_df = nfl_df[nfl_df['year'].eq(2018)]
    nfl_df.drop([0,5,10,15,20,25,30,35], inplace=True)
    nfl_df['W-L%'] = nfl_df['W-L%'].apply(lambda x: float(x))
    nfl_states = ['Phoenix', 'Atlanta', 'Baltimore', 'Buffalo', 'Charlotte', 'Chicago',
             'Cincinnati', 'Cleveland', 'Dallas–Fort Worth', 'Denver', 'Detroit', 'Green Bay', 'Houston',
             'Indianapolis', 'Jacksonville', 'Kansas City', 'Los Angeles', 'Los Angeles', 'Miami–Fort Lauderdale',
             'Minneapolis–Saint Paul', 'Boston', 'New Orleans', 'New York City', 'New York City', 'San Francisco Bay Area',
             'Philadelphia', 'Pittsburgh', 'San Francisco Bay Area', 'Seattle', 'Tampa Bay Area', 'Nashville',
             'Washington, D.C.']
    nfl_df['state'] = nfl_states
    cities['NFL W/L'] = nfl_df.groupby('state')['W-L%'].mean()
    
    #Getting regions with more than one team in more than one league
    q5_df = cities[['NFL W/L', 'MLB W/L', 'NBA W/L', 'NHL W/L']]
    q5_df['not in'] = q5_df.isnull().sum(axis=1)
    nearly_there = q5_df[q5_df['not in'].lt(3)]
    nearly_there.drop('not in', axis=1, inplace=True)
    
    #Getting p-values
    sports = ['NFL', 'MLB', 'NBA', 'NHL']
    p_values = pd.DataFrame({k:np.nan for k in sports}, index=sports)
    NFL = []
    MLB = []
    NBA = []
    NHL = []
    (at_stat, ap) = stats.ttest_rel(nearly_there['NFL W/L'], nearly_there['MLB W/L'], nan_policy='omit')
    (bt_stat, bp) = stats.ttest_rel(nearly_there['NFL W/L'], nearly_there['NBA W/L'], nan_policy='omit')
    (ct_stat, cp) = stats.ttest_rel(nearly_there['NFL W/L'], nearly_there['NHL W/L'], nan_policy='omit')
    (dt_stat, dp) = stats.ttest_rel(nearly_there['MLB W/L'], nearly_there['NBA W/L'], nan_policy='omit')
    (et_stat, ep) = stats.ttest_rel(nearly_there['MLB W/L'], nearly_there['NHL W/L'], nan_policy='omit')
    (ft_stat, fp) = stats.ttest_rel(nearly_there['NBA W/L'], nearly_there['NHL W/L'], nan_policy='omit')
    NFL.append('')
    NFL.append(ap)
    NFL.append(bp)
    NFL.append(cp)
    MLB.append(ap)
    MLB.append('')
    MLB.append(dp)
    MLB.append(ep)
    NBA.append(bp)
    NBA.append(dp)
    NBA.append('')
    NBA.append(fp)
    NHL.append(cp)
    NHL.append(ep)
    NHL.append(fp)
    NHL.append('')
    p_values['NFL'] = NFL
    p_values['NBA'] = NBA
    p_values['NHL'] = NHL
    p_values['MLB'] = MLB
    p_values.replace(to_replace='', value=np.nan, regex=True)
    
    
    assert abs(p_values.loc["NBA", "NHL"] - 0.02) <= 1e-2, "The NBA-NHL p-value should be around 0.02"
    assert abs(p_values.loc["MLB", "NFL"] - 0.80) <= 1e-2, "The MLB-NFL p-value should be around 0.80"
    return p_values

print(sports_team_performance())