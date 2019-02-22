from Crypto.Cipher import AES
from Crypto.Util import Counter
from os import urandom
plaintext = raw_input()
nonce = urandom(12)
key = urandom(16)

def CTR_encryption(pt,key,nonce):
	ctr = Counter.new(32, prefix=nonce)
	cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
	ciphertext = cipher.encrypt(pt)

	return ciphertext
def CTR_decryption(ct,key,nonce):
	ctr = Counter.new(32, prefix=nonce)
	cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
	plaintextt=cipher.decrypt(ct)
	return plaintext

ct=CTR_encryption(plaintext,key,nonce)
pt=CTR_decryption(ct,key,nonce)
print(ct)
print(pt)

