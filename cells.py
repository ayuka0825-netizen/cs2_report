# cells.py
# 細胞の数を計算するプログラム
# 1分ごとに2つに分かれて、そのあと4つ死ぬ
# 最初は10個
import sys

INITIAL = 10  # 最初の数
DIE = 4       # 死ぬ数

def cells(n):
    """n分後の細胞の数を出す"""
    # 0分のときは最初の数
    if n == 0:
        return INITIAL
    # 1分前の数を2倍して4を引く
    # （ここで自分をもう一回呼んでいる）
    c = cells(n - 1) * 2 - DIE
    # マイナスにならないように
    return max(c, 0)

def main():
    # 引数があったらそれを使う
    # なかったら入力してもらう
    if len(sys.argv) > 1:
        s = sys.argv[1]
    else:
        s = input("経過時間n（分）: ")
    # 数字かどうかチェック
    if not s.isdigit():
        print("0以上の整数を入力すること")
        return
    n = int(s)
    # nが大きいとエラーになるので回数を増やしておく
    sys.setrecursionlimit(max(1000, n + 100))
    # 0分からn分まで表示
    for t in range(n + 1):
        print(f"{t:3d}分後: {cells(t)}個")

if __name__ == "__main__":
    main()
