import random

def netaGen():
    verb = [
        'してみた！',
        'やってみた！',
        'に行きます。',
        '凸待ち。',
        '作ってみた！'
    ]

    S1 = [
        'えじますが',
        'chibacchiが',
        '平間太規が',
        'ヒカキンさんから',
        '乙武さんと'
    ]

    C1 = [
        'キャッチボール',
        'ドライブ',
        '飲み会コールの練習',
        'ゲイバー',
        'LINEスタンプ'
    ]
    rand_num1 = random.randint(0,4)
    rand_num2 = random.randint(0,4)
    rand_num3 = random.randint(0,4)
    # SS = S1[rand_num1] + C1[rand_num2] + verb[rand_num3]
    return S1[rand_num1] + C1[rand_num2] + verb[rand_num3]