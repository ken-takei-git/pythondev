# +-----------------+ #
#   フィボナッチ数列   #
# +-----------------+ #
def fibonacci(num):
    # 2以下の場合
    if num < 2:
        return num
    else:
        # 再帰的関数 最終的に直前の2つの数値の和を返す
        return (fibonacci(num-1) + fibonacci(num-2))