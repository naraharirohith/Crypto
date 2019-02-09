def pad(s):
	"""	
	This function is to pad a plaintext.
	
	parameters:
		s: str
				string to be Padded

	"""
	pad_byte=16-(len(s)%16)                         #Number of bytes to be Padded.
 	
	return s+pad_byte*(chr(pad_byte))	        #String of padded palintext.


def revpad(s):
	"""	
	This function is to remove padding.
	
	parameters:
		s:str
				string to be reverse padded
							

	"""

	k=ord(s[-1])                             
	temp=0					        #temporary variable to check padding  
	for i in range (1,k):                           #for loop to check padding
		if(s[-i]!=s[-1]):		        #comparision of bytes with the last Byte
			temp=1
	
	if(temp==0):
		return (s[:-k])			        #Reverse padded string
	else:
		return ("Wrong padding")
	





from Crypto.Cipher import AES
from Crypto import Random
iv=Random.new().read(AES.block_size)

def xor_strings(s, t):
	"""
	This function is to XOR two strings .
	"""
    return (''.join(chr(ord(a)^ord(b)) for a, b in zip(s, t)))


def encryption_CBC(pt,key,iv):
	"""
	This function is for encrypting plaintext to ciphertext in CBC mode

	parameters:
		pt:str
			palintext to be encrypted
		key:str
			key used for CBC encryption
		iv:str
			intiallisation vector in CBC.
	"""

	cipher=AES.new(key,AES.MODE_CBC, iv)
	return cipher.encrypt(pad(pt))



def decryption_CBC(ct,key,iv):
	"""
	This function is for decrypting ciphertext to plaintext in CBC mode

	parameters:
		ct:str
			ciphertext to be decrypted
		key:str
			key used for CBC encryption
		iv:str
			intiallisation vector in CBC.
	"""

	plaintxt=AES.new(key,AES.MODE_CBC, iv)
	return revpad(plaintxt.decrypt(ct))
