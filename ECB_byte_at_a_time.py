from os import urandom

junk="Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK".decode('base64')
iv=urandom(16)
key=urandom(16)

def pad(s):
	pad_byte=16-(len(s)%16)                  
 	return s+pad_byte*(chr(pad_byte))	 

def encryption(pt,key,junk,iv):
	from Crypto.Cipher import AES
	cipher=AES.new(key,AES.MODE_CBC)
	ct=cipher.encrypt(pad(pt+junk))
	return ct



def decryption(ct,key,iv):       
	from Crypto.Cipher import AES
	plaintxt=AES.new(key,AES.MODE_CBC)
	pt=plaintxt.decrypt(revpad(ct))
	return pt

new_junk=""
s="a"*15

for j in range (len(junk)):
	s=s[len(s)-15:len(s)]
	print(s)
	k=encryption(s,key,junk[j:],iv)
	for i in range (256):
		s=s+chr(i)
		ct=encryption(s,key,junk[j:],iv)[:16]
		s=s[:-1]
		if(ct==k[:16]):		
			new_junk=new_junk+chr(i)
			s=s+chr(i)
			s=s[1:]
			print(s)	
		
	 
print("here is your secret text: ")
print(new_junk)

if(new_junk==junk):
	print("YES , YOU GOT THE SECRET TEXT ")
else:
	print("NO SECRET TEXT FOR U ")
