def pad(s):   
	
	#This function is for padding
	
	pad_byte=16-(len(s)%16)
	return s+pad_byte*(chr(pad_byte))	        
	pad_byte=16-(len(s)%16)            
 
from Crypto.Cipher import AES
from Crypto import Random
iv=Random.new().read(AES.block_size)
key=Random.new().read(AES.block_size)

def xor_strings(s, t):
	#This is for xoring two strings.
    return (''.join(chr(ord(a)^ord(b)) for a, b in zip(s, t)))


def encryption_CBC(pt,key,iv):
	#This for encryption using CBC.
	
	cipher=AES.new(key,AES.MODE_CBC, iv)
	return cipher.encrypt(pad(pt))



def decryption_CBC(ct,key,iv):
	#This function is for decrypting using CBC mode.
	plaintxt=AES.new(key,AES.MODE_CBC, iv)
	return plaintxt.decrypt(ct)

def function1(a):
	# First qoutes out ";" and "=" and adds the given strings and encrypts it.
	for i in range (len(a)):
		if(a[i]==";"  or a[i]=="="):
			a=a.replace(a[i],"?")
	a="comment1=cooking%20MCs;userdata="+a+";comment2=%20like%20a%20pound%20of%20bacon"
	enc = encryption_CBC(a,key,iv)
	return enc

def function2 (enc):                      
	# This function checks for the string.
	dec=decryption_CBC(enc,key,iv)
	if ";admin=true;" in dec:
		return ("YES")
	else:
		return ("NO")


l=function1(";admin=true;")               
k=list(function1(";admin=true;"))

ivblock=k[16:32]	#As the requried string is in third block it should be xored with second block.
reqblock=k[32:48]	
k[16]=chr(ord(k[16]) ^ ord(";") ^ ord("?"))
k[22]=chr(ord(k[22]) ^ ord("=") ^ ord("?"))
k[27]=chr(ord(k[27]) ^ ord(";") ^ ord("?"))

l=l.replace(''.join(l[16:32]),''.join(k[16:32]))     #Replacing the string with string whick is flipped
print(function2(l))                        #Prints "YES" if ";admin=true;" is present in decrypted function.

