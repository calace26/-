'''
木に対する動的計画法_閉路のない有効グラフ(有向非巡回グラフ)
閉路を含まない有効パスの最長の長さを調べる。
トポロジカルソートが重要
閉路のないグラフにおいて、辺に沿って進むほど値が大きくなるように、N個の頂点0,1,・・・,N-1の番号を割り当てることを指す。
正確には、すべての辺についてその始点の番号より終点の番号のほうが大きいという条件を満たすとき、
そのような番号の割り当て方をグラフのトポロジカルソートと呼ぶ。
閉路のない有効グラフには、必ずトポロジカルソートが存在する。
閉路があるグラフではトポロジカルソートが存在せず、今回の動的計画法では解けない
AtCoder Educational DP Contest G 問題
https://atcoder.jp/contests/dp/tasks/dp_g
'''
# 再帰上限を増やす
import sys
sys.setrecursionlimit(1000000)

N,M = map(int,input().split())

# edges[i]:頂点iから辺が伸びている頂点たち(隣接リスト)
edges = []
for i in range(N):
    edges.append([])
# 入次数。始点の判定に使う
indeg = [0]*N

# 辺の入力を受け取り、隣接リストを作る
for i in range(M):
    x,y = map(int,input().split())
    edges[x-1].append(y-1)
    indeg[y-1] += 1

# length[i]:頂点iから始まるパスの最大長
length = [0]*N
# done[i]:cost[i]がすでに計算済みであることを示すフラグ
done = [False]*N

# メモ化再帰の実装
def rec(i):
    # 計算済みであれば、即座に値を返す
    if done[i]:
        return length[i]
    # そうでなければ値を計算する
    length[i] = 0
    for j in edges[i]:
        length[i] = max(length[i], rec(j) + 1)
    # 計算済みフラグを立てて値を返す
    done[i] = True
    return length[i]

# 始点すべてについてrecを呼び出す
for i in range(N):
    if indeg[i] == 0:
        rec(i)

# 答えはlengthの最大値
print(max(length))
