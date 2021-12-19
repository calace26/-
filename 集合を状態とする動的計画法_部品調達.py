'''
部品調達
集合をキーとする動的計画法。遷移でビット演算を使用する
状態数は(M+1)*2^Nであり、各状態からの遷移は2通りとなるため、計算量は(M*2^N)となる。
第一回アルゴリズム実技検定 I問題
https://atcoder.jp/contests/past201912-open/tasks/past201912_i
'''
N,M = map(int,input().split())
# 1始まりにするためダミーを入れる。Sは整数に直す
S = [0]
C = [0]
for i in range(M):
    s,c = input().split()
    s_val = 0
    for j in range(N):
        if s[j] == 'Y':
            s_val |= 1<<j
    S.append(s_val)
    C.append(int(c))

# 集合としてあり得るものの個数。2**Nでも同じ
ALL = 1<<N

# cost[i][n]:セットiまで見て揃った部品の集合がnであるときのコスト最小値
cost = []
INF = 10**100
for i in range(M+1):
    cost.append([INF]*ALL)

# 初期条件
cost[0][0] = 0

# iが小さいところから順に計算
for i in range(1,M+1):
    for n in range(ALL):
        # セットiを買わない
        cost[i][n] = min(cost[i][n], cost[i-1][n])
        # セットiを買う
        cost[i][n|S[i]] = min(cost[i][n|S[i]], cost[i-1][n] + C[i])

# 答えは部品が全部そろっている状態の最小コスト
# ただしINFのままなら、部品を揃えることは不可能
ans = cost[M][ALL-1]
if ans == INF:
    ans = -1

print(ans)
