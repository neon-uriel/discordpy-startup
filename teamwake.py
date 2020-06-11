import random
import sys
def doTeamwake(*args):
    team = list(args)
    random.shuffle(team)
    print(len(team)//2 - 1)
    team1 = team[0:len(team)//2]
    team2 = team[len(team)//2:len(team)]
    print(team)
    return team1,team2