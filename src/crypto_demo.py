import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA256 
from Crypto.Signature import pkcs1_15
from Crypto.Cipher import PKCS1_OAEP

def generate_key(KEY_LENGTH=2048):
    random_value = Random.new().read
    key_pair = RSA.generate(KEY_LENGTH, random_value)
    return key_pair

def generate_signature(key_pri, message):
    hash = SHA256.new(message)
    signature = pkcs1_15.new(key_pri).sign(hash) 
    return signature

def vertify_signature(message, key_pub, signature):
    message_hash = SHA256.new(message)
    try:
        pkcs1_15.new(key_pub).verify(message_hash, signature)
        vertify = True
    except ValueError:
        vertify = False
    return vertify

# 署名が妥当であるかを出力
def print_vertify_signature(isVertify):
    if isVertify:
        print('この署名は妥当です。')
    else:
        print('この署名は不当です。')

key_1_pri = generate_key()
key_2_pri = generate_key()

# 生成した鍵の公開鍵を表示
key_1_pub = key_1_pri.public_key()
key_2_pub = key_2_pri.public_key()
print('鍵1の公開鍵：', key_1_pub)
print('鍵2の公開鍵：', key_2_pub)

message = b'This is an exercise in cryptography procedures.'

# key_1の公開鍵を使用しメッセージを暗号化
publick_cipher = PKCS1_OAEP.new(key_1_pub)
cipher_message = publick_cipher.encrypt(message)

# key_1の秘密鍵を使用してメッセージを復号化
private_cipher = PKCS1_OAEP.new(key_1_pri)
decryption_message = private_cipher.decrypt(cipher_message)

print('送信メッセージ：', message.decode())
print('復号メッセージ：', decryption_message.decode())

# 秘密メッセージの署名を生成
sign_1 = generate_signature(key_1_pri, message)

# key_1の公開鍵から署名文の妥当性確認
print_vertify_signature(vertify_signature(message, key_1_pub, sign_1))

# key_2の公開鍵から署名文の妥当性確認
print_vertify_signature(vertify_signature(message, key_2_pub, sign_1))