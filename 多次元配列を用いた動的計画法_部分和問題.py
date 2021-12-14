'''
部分和問題
いくつかの配点が与えられるので、何通りの点数を取り得るかや、和を○○点ぴったりにできるかが問われる
AtCoder Typical DP Contest A
https://atcoder.jp/contests/tdpc/tasks/tdpc_contest
O(NP)で解く
'''
N = int(input())
# 1始まりにするために先頭にダミーを入れる
ps = [0] + list(map(int,input().split()))

# Pには取り得る最大値を代入する。existにて配列のサイズを指定するときに使用する
P = sum(ps)

# exist[i][s]:iまでの問題で得点合計をsにできる
exist = []
for i in range(N+1):
    exist.append([False]*(P+1))

#初期条件
exist[0][0] = True

# iが小さい順にexistの値を求めていく
for i in range(1, N+1):
    for s in range(P+1):
        # 問題を解かない場合、i-1問目の点数(True)を引き継ぐ
        if exist[i-1][s]:
            exist[i][s] = True
        # 問題iを解く場合 (sの方がiの配点ps[i]以上かつi-1番目の段階でiを解いたとき点数がsとなりうる値が存在するとき)
        if s >= ps[i] and exist[i-1][s-ps[i]]:
            exist[i][s] = True

# 答えはexist[N][s]の中でTrueになっているsの個数
ans = 0
for s in range(P+1):
    if exist[N][s]:
        ans += 1

print(ans)
