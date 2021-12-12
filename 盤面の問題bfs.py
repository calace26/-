'''
盤面の問題のbfs
R*Cの盤面とスタート地点、ゴール地点の座標が与えられる。
スタートからゴールまでの最小手数を答える問題
ABC007-C
https://atcoder.jp/contests/abc007/tasks/abc007_3
'''
from collections import deque
# 入力R、Cを受け取る
R, C = map(int,input().split())
# スタート地点の座標を受け取る
sy, sx = map(int,input().split())
# ゴール地点の座標を受け取る
gy, gx = map(int,input().split())
# 盤面を入力するための空のリストを作成する
S = []
for i in range(R):
    s = input()
    S.append(s)
sy -= 1
sx -= 1
gy -= 1
gx -= 1

# 始点からの最小移動回数を管理数r2次元配列。-1なら未訪問
dist = []
for i in range(R):
    dist.append([-1]*C)

# キューを用意して始点を入れる
Q = deque()
Q.append([sy,sx])
dist[sy][sx] = 0

# キューから取り出しながら探索する
while len(Q) > 0:
    i,j = Q.popleft()
    # 4つの隣マスを確認する
    for i2, j2 in [[i+1, j],[i-1, j],[i, j+1],[i, j-1]]:
        # もし盤面の範囲内でなければ無視する
        if not (0 <= i2 < R and 0 <= j2 < C):
            continue
        # もし壁マスであれば無視する
        if S[i][j] == '#':
            continue
        # もし未訪問(dist[i2][j2]が-1)であれば、距離を更新してキューに入れる
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1
            Q.append([i2, j2])
# 始点から終点までの最小移動回数を出力
print(dist[gy][gx])
