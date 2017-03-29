# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv


input_file = csv.DictReader(open("football.csv"))


def calc_min_dif(data):
    min_dif = None
    team = None
    for row in data:
        dif = abs(int(row['Goals']) - int(row['Goals Allowed']))
        if min_dif == None or min_dif > dif:
            min_dif = dif
            team = row["Team"]
    return(team + " had the smallest difference in for/against goals with a difference of " + str(min_dif) + ".")
