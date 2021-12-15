'''
計算する順序を工夫する動的計画法

第二回アルゴリズム実技検定 H 問題
https://atcoder.jp/contests/past202004-open/tasks/past202004_h
マス数はNMとなるためO(N^2*M^2)となる
'''
N,M = map(int, input().split())
A = []
for i in range(N):
    s = input()
    A.append(s)

# 番号ごとに座標を分類。スタートは0、ゴールは10とする
group = []
for n in range(11):
    group.append([])
for i in range(N):
    for j in range(M):
        if A[i][j] == 'S':
            n = 0
        elif A[i][j] == 'G':
            n = 10
        else:
            n = int(A[i][j])
        group[n].append([i,j])

# cost[i][j]:数字を正しく通ってマス[i, j]にたどり着く最小移動回数
# 非常に大きい値で初期化していく
cost = []
INF = 10**100
for i in range(N):
    cost.append([INF]*M)

# 初期条件。スタート地点の座標はgroup[0][0]
si ,sj = group[0][0]
cost[si][sj] = 0

# nが小さい方から順番に求めていく
for n in range(1, 11):
    # 更新したいマスそれぞれについてループ
    for i, j in group[n]:
        # 数字がn-1であるマスをすべて試す
        for i2, j2 in group[n-1]:
            cost[i][j] = min(cost[i][j], cost[i2][j2] + abs(i-i2) + abs(j-j2))

# ゴール地点の座標はgroup[10][0]
# ただしゴール地点のcostがINFであれば、到達不可能なため-1を答えとする
gi, gj = group[10][0]
ans = cost[gi][gj]
if ans == INF:
    ans = -1

print(ans)
