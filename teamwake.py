import random
import sys
def doTeamwake(*args):
    humannum = len(args)
    team1num = humannum // 2
    team2num = humannum - team1num
    cnt = team1num
    team1 = random.sample(args,k=team1num)
    team2 = list(set(args) - set(team1))
    return team1,team2
# print(teamwake.doTeamwake('ramune','nasuline','hirama','chibacchi'))