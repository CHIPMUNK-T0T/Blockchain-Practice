import math

# Diffie-Hellman鍵交換アルゴリズムを使用して両者のカギを好感するアルゴリズム
# x ^ exp mod P の値を返す関数
def modulo(x, exp, P):
    return math.pow(x, exp) % P

P = 23 # 素数Pを決定
G = 9  # Pに対する元始根Gを合意

a = 4  # 選択された秘密の値（2 <= a < P）
b = 4  # 選択された秘密の値（2 <= a < P）

x = modulo(G, a, P)
y = modulo(G, b, P)

key_1 = modulo(y, a, P)
key_2 = modulo(x, b, P)

print('key_1:', key_1)
print('key_2:', key_2)