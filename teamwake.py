import random
import sys
def doTeamwake(lst):
    team = list(lst)
    random.shuffle(team)
    print(len(team))
    team1 = team[0:len(team)//2]
    team2 = team[len(team)//2:len(team)]
    print(team)
    return team1,team2