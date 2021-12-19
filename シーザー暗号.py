'''
Pythonでアルファベット文字列をN文字分ずらす：シーザー暗号
AtCoder Beginner Contest B 問題
https://atcoder.jp/contests/abc232/tasks/abc232_b
'''
'''
ord関数
1 文字の Unicode 文字を表す文字列に対し、
その文字の Unicode コードポイントを表す整数を返します。
https://docs.python.org/ja/3/library/functions.html#ord
'''
ord('A')    # 65
ord('D')    # 68

'''
chr関数
Unicode コードポイントが整数 i である文字を表す文字列を返します。
https://docs.python.org/ja/3/library/functions.html#chr
'''
chr(65)     # 'A'
chr(70)     # 'F'

# 平文
PLAIN = input()
# 比較用の文字
T = input()
# 平文1文字目
s = PLAIN[0]
# 比較用の文字の1文字目
t = T[0]

# 秘密鍵:平文➡比較用の文字で何文字ずらすか
KEY = ord(t) - ord(s)

# 平文からKEY文字ずらした文字列を作成する用
enc = ""

for char in list(PLAIN):
    Unicode = ord(char)
    # ord('a')は97
    num = Unicode - 97
    num = (num + KEY) % 26
    Unicode = num + 97
    enc += chr(Unicode)

if enc == T:
  print("Yes")
else:
  print("No")
