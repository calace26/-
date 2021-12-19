'''
集合の全探索
集合に対する全探索を行う問題。集合を整数として扱い、ビット演算を用いて和集合や差集合を求める
前半O(N^2*2^N),後半はO((2^N)^2=4^N)なのでO(4^N)
第一回アルゴリズム実技検定 G問題
https://atcoder.jp/contests/past201912-open/tasks/past201912_g
'''
N = int(input())
A = []
for i in range(N-1):
    # A[i]はA[i][i+1]からスタートするため、0から1までの(i+1)個はダミーで埋める
    lst = list(map(int,input().split()))
    A.append([0]*(i+1) + lst)

# 集合としてあり得るものの個数。2**Nでも同じ
ALL = 1<<N

# happy[n]:nで表現される集合をグループにしたときの幸福度
happy = [0]*ALL

# nで表現される集合に要素iが含まれるかを判定してTrue/Falseを返す関数
def has_bit(n, i):
    return (n & (1<<i) > 0)

# happyの値を前もって計算する
for n in range(ALL):
    for i in range(N):
        for j in range(i+1,N):
            if has_bit(n,i) and has_bit(n,j):
                happy[n] += A[i][j]

# 答えの値。非常に小さい値で初期化して、maxで更新する
ans = -10**100

for n1 in range(ALL):
    for n2 in range(ALL):
        # n1とn2で重複があれば無視する
        if n1&n2 > 0:
            continue
        # n3を補集合として求めて答えを更新する
        n3 = ALL-1 - (n1|n2)
        ans = max(ans, happy[n1] + happy[n2] + happy[n3])

print(ans)
