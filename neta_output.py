import random

def netaGen():

    verb = [
        'してみた！',
        'やってみた！',
        'に行きます。',
        '凸待ち。',
        '作ってみた！',
        'をする人に募金をします。',
        '買った結果ｗｗｗｗ',
        'やった結果ｗｗｗｗ',
        'した結果ｗｗｗｗ',
        'することとなりました。',
        'した件について語る。'

    ]

    S1 = [
        'ejimasu',
        'chibacchi',
        '平間太規',
        'ヒカキンさん',
        '乙武さん',
        '小池都知事',
        'ラムネ',
        '香取慎吾',
        'ヒカキンゲームズ',
        'SEIKIN',
        'セイキンさん',
        'シバター',
        'ワイ',
        'ヒロック',
        '廣川龍'
    ]

    tenioha = [
        'が',
        'と',
        'と一緒に',
        '、'
    ]

    C1 = [
        'キャッチボール',
        'ドライブ',
        '飲み会コールの練習',
        'ゲイバー',
        'LINEスタンプ制作',
        'エゴサーチ',
        '盗撮',
        'UUUM脱退',
        'ボビー・オロゴンに1億円寄付',
        '料理',
        '退学'
    ]
    rand_num1 = random.randint(0,len(S1) - 1)
    rand_num2 = random.randint(0,len(C1) - 1)
    rand_num3 = random.randint(0,len(verb) - 1)
    rand_num_teni = random.randint(0,len(tenioha) - 1)
    ans = [
        S1[rand_num1] + tenioha[rand_num_teni] + C1[rand_num2] + verb[rand_num3],
        S1[rand_num1] + tenioha[rand_num_teni] + C1[rand_num2] + verb[rand_num3],
        S1[rand_num1] + "を救いたい。",
        C1[rand_num2] + "、キモチェェ〜〜",
        '【悲報】' + S1[rand_num1] + tenioha[rand_num_teni] + C1[rand_num2] + verb[rand_num3],
        '【朗報】' + S1[rand_num1] + tenioha[rand_num_teni] + C1[rand_num2] + verb[rand_num3],
        '【漫画】' + S1[rand_num1] + tenioha[rand_num_teni] + C1[rand_num2] + verb[rand_num3] + '【マンガ動画】'
    ]
    rand_num4 = random.randint(0,len(ans) - 1)
    return ans[rand_num4]

def ramuline():

    ramu = [
        'まだ終わってねえんだよ。',
        '死が救済訳ないだろ',
        'こんな戦況からでも勝てるのが僕ら',
        '死体撃ちする奴がいるとゲームが楽しくなくなる。',
        'Valorantに全てを賭けれるのかよ',
        '動画見た。リロードの最中に逃げろよ。と思うのは俺がFPSに慣れてるからか？\n銃声で即座に敵の位置を確認、遮蔽物を利用してのタイミングを計った立ち回り\nうずくまってて撃たれてる連中は馬鹿としか言いようがないよ\nでも流石に一般人に要求するのは酷か'
    ]
    rand_num1 = random.randint(0,len(ramu) - 1)
    return ramu[rand_num1] + " --- ramuline"
