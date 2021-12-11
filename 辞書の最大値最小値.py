d = {'a':100, 'b':20, 'c':50, 'd':100, 'e':80}

'''
辞書のキー(key)の最大値・最小値を取得
キーの最大値はa,最小値はe(アルファベット順)となる
'''
max_d = max(d)
print(max_d)
# e　これは辞書はイテラブルオブジェクトとして要素のキーを列挙するため
min_d = min(d)
print(min_d)
# a


'''
辞書の値(value)の最大値，最小値を取得
値の最大値は100,最小値は20となる
'''
max_v = max(d.values())
print(max_d)
# 100
min_v = min(d.values())
print(min_v)
# 20


'''
辞書の値(value)が最大・最小となるキーを取得
値の最大値は100なのでそのキーaを取得,最小値は20なのでそのキーbを取得する
get()メソッドを使用することで値が返されるため
'''
max_k = max(d,key=d.get)
print(max_k)
# a 複数当てはまる場合は1つのみ返される
min_k = min(d,key=d.get)
print(min_k)
# b 複数当てはまる場合は1つのみ返される


'''
辞書の値(value)が最大・最小となるキーと値を同時に取得
値の最大値は100なのでそのキーaと値100を取得,最小値は20なのでそのキーbと値20を取得する
items()メソッドを使用して辞書のキーと値のタプル(key,value)のビューを返す。
lambda関数を使用している
'''
max_kv = max(d.items(), key=lambda x: x[1])
print(max_kv)
# ('a', 100)
print(type(max_kv))
# <class 'tuple'>
min_kv = min(d.items(), key=lambda x: x[1])
print(min_kv)
# ('b', 20)
max_k, max_v = max(d.items(), key=lambda x: x[1])
print(max_k)
# a
print(max_v)
# 100


'''
最大・最小となる値が複数存在する場合
リスト内包表記を使用することで最大・最小となる値が複数存在する場合、そのキーまたはキーと値のタプルを
リストとして取得する
この方法では、最大・最小となる値が一つの場合でも要素数が1のリストが取得できる
'''
#キーと値のタプルを取得する例
max_kv_list = [kv for kv in d.items() if kv[1] == max(d.values())]
print(max_kv_list)
# [('a', 100), ('d', 100)]

#キーのみのリストを取得する例
max_k_list = [kv[0] for kv in d.items() if kv[1] == max(d.values())]
print(max_k_list)
# ['a', 'd']
