# +-----------------+ #
#   フィボナッチ数列   #
# +-----------------+ #
def fibonacci(num):
    fst_num = 1 # 1つ目の番号
    snd_num = 1 # 2つ目の番号
    ans_num = 0 # 答え

    # 1番目と2番目の場合
    if (num == 1) or (num == 2):
        return 1;
    # 入力された数値まで、繰り返し処理
    for i in range(3, num+1):
        # 加算処理
        ans_num = fst_num + snd_num
        # 入力された数値まで、繰り返し処理をしたら
        if (i == num):
            return ans_num # 答えを返す
        fst_num = snd_num # 1つ目の番号に2つ目の番号を代入
        snd_num = ans_num # 2つ目の番号に答えを代入