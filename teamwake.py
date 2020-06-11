import random
import sys
def doTeamwake(lst):
    team = list(lst)
    random.shuffle(team)
    #print(len(team))
    team1 = team[0:len(team)//2]
    team2 = team[len(team)//2:len(team)]
    #print(team)
    return team1,team2

def makeResult(team,team1,team2):
    mes1 = 'チーム' + team1[0] + ': \n'
    mes2 = 'チーム' + team2[0] + ': \n'
    for i in range (len(team1)):
        mes1 += team1[i] + '\n'
    for i in range (len(team2)):
        if(i == len(team2) - 1):
            mes2 += team2[i]
        else:
            mes2 += team2[i] + '\n'
    result = (mes1 + '\n' + mes2)
    return result