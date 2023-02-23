import hashlib

md = hashlib.md5()
md.update(b'The quick brown fox jumps over the razy dog')
print(md.digest())
print('ダイジェストサイズ：', md.digest_size)
print('ブロックサイズ　　：', md.block_size)

print('ダイジェストSHA224', hashlib.sha224(b'The quick brown fox jumps over the razy dog').hexdigest())
print('ダイジェストSHA256', hashlib.sha256(b'The quick brown fox jumps over the razy dog').hexdigest())
print('ダイジェストSHA384', hashlib.sha384(b'The quick brown fox jumps over the razy dog').hexdigest())
print('ダイジェストSHA512', hashlib.sha512(b'The quick brown fox jumps over the razy dog').hexdigest())

h = hashlib.new('ripemd160')
h.update(b'The quick brown fox jumps over the razy dog')
print('RIPEMD160:', h.hexdigest())

import hashlib, binascii
algolithm = 'sha256'
password = b'HomeWifi'
salt = b'salt' # salt は一方向性関数への追加入力として使えるランダムなデータ
nu_rounds = 1000
key_length = 64
dk = hashlib.pbkdf2_hmac(algolithm, password, salt, nu_rounds, dklen=key_length)
print('導出した鍵：', dk)
print('導出した鍵の16進数：', binascii.hexlify(dk))

import hashlib
input = 'Sample Input Text'
for i in range(20):
    input_text = input + str(i)
    print(input_text, ':', hashlib.sha256(input_text.encode('utf-8')).hexdigest())
