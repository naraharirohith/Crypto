def CTR_encryption(pt,key,nonce):     #encryption using CTR mode
	ctr = Counter.new(32, prefix=nonce)
	cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
	ciphertext = cipher.encrypt(pt)

	return ciphertext
def CTR_decryption(ct,key,nonce):	#decryption using CTR mode
	ctr = Counter.new(32, prefix=nonce)
	cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
	pt=cipher.decrypt(ct)
	return pt


def function1(username,key,nonce):
	username="comment1=cooking%20MCs;userdata="+username+";comment2=%20like%20a%20pound%20of%20bacon"
	username=username.replace(";","?")	#Qouting out the ";" and "="
	username=username.replace("=","?")
	return CTR_encryption(username,key,nonce)

def function2(cookie,key,nonce):	
	username=CTR_decryption(cookie,key,nonce)	
	print(username)
	if ";admin=true;" in username:  	#checking for ";admin=true;" in the username that is 							finally decrytpted
		return "YES"
	else:
		return "NO"


if __name__=="__main__":
	from Crypto.Cipher import AES
	from Crypto.Util import Counter
	from os import urandom
	nonce = urandom(12)
	key = urandom(16)

	username=";admin=true;"
	ct=function1(username,key,nonce)
	print(function2(ct,key,nonce))
	
	ct=ct.replace(ct[32],chr(ord(ct[32]) ^ ord("?") ^ ord(";")))	#flipping byte from "?" to ";" 
	ct=ct.replace(ct[38],chr(ord(ct[38]) ^ ord("?") ^ ord("="))) 
	ct=ct.replace(ct[43],chr(ord(ct[43]) ^ ord("?") ^ ord(";"))) 

	print(function2(ct,key,nonce))
