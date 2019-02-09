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
	
def encryption_ECB(pt,key):
	"""
	This function is for encrypting plaintext in ECB mode

	parameters:
		pt: str 
				palintext to be encrypted
		key: str
				key for ECB mode encryption whose lenght is always a multiple of 16 in this case
	"""

	from Crypto.Cipher import AES
	cipher=AES.new(key,AES.MODE_ECB)
	ct=cipher.encrypt(pad(pt))	
	
	return (ct)

	
def decryption_ECB(ct,key):
	"""
	This function is for decrypting ciphertext in ECB mode
	
	parameters:
		ct: str
				ciphertext to be decrypted
		key: str
				key for ECB mode encryption whose lenght is always a multiple of 16 in this case
	"""
	from Crypto.Cipher import AES
	plaintxt=AES.new(key,AES.MODE_ECB)
	pt=plaintxt.decrypt(ct)
	
	return revpad(pt)			           #After decrypting padding should be removed


def drawbacks_ECB(key):
	#this function is to convey the drawback of AES_ECB mode encryption
	
	a="abcdefghijklmnopabcdefghijklmnop"	           # An example of plain text in which two blocks are same
	k=(encryption_ECB(a,key))
	print(k[:16])
	print(k[16:32])
	if(k[:16]==k[16:32]):
		return "This is the main Drawback"

