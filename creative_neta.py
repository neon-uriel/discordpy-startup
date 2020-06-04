import random

def netaGen():

    S1 = [
        '手を入れる',
        '手を入れる',

    ]

    S2 = [
        'が',
        'と',
        'と一緒に',
        '、'
    ]
    rand_1 = random.randint(0,len(S1) - 1)
    rand_2 = random.randint(0,len(S2) - 1)
    ans = S1[rand_1] + S2[rand_2]
    return ans