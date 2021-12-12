'''
動的計画法の入門問題。
N個の足場の高さが与えられるので、N番目にたどり着いた時の最小の高さコストを調べる問題
AtCoder Educational DP Contest A
https://atcoder.jp/contests/dp/tasks/dp_a
'''
N = int(input())
h = list(map(int, input().split()))

# cost[i]:足場iにたどり着くための最小コスト。サイズNを確保する
cost = [0]*N

# 初期条件
cost[0] = 0
# 2つ目の足場はジャンプ元が1通り
cost[1] = cost[0] + abs(h[0]-h[1])
# それ以降の足場はジャンプ元が2通りあるため、コストが小さいほうを採用する
for i in range(2,N):
    cost[i] = min(cost[i-1] + abs(h[i-1]-h[i]), cost[i-2] + abs(h[i-2]-h[i]))

# 答えは最後の足場までの最小コスト
print(cost[N-1])
