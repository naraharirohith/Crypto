from pwn import *
r= remote("13.234.27.172", 1337)	
r.recvuntil("choice: ")
r.sendline("1")
r.recvuntil("register: ")
r.sendline("abcdefghijklmnopabcdefghijklmnop")      #plain text having two same blocks
k=r.recvline()[len("[+] Here, take your cookie:  "):]

if(k[:16]==k[16:]):		#checking the ciphertext blocks
	print("Two blocks are same.This is ECB mode encryption")
else:
	print("This is CBC mode encryption")
r.close()


def pad(s):
	pad_byte=16-(len(s)%16)               	
	return s+pad_byte*(chr(pad_byte))	

def encryption_ECB(pt,key):

	from Crypto.Cipher import AES
	cipher=AES.new(key,AES.MODE_ECB)
	ct=cipher.encrypt(pad(pt))	
	
	return (ct)


a="abcdefghijklmnopabcdefghijklmnop"		#plain text having two same blocks
k=(encryption_ECB(a,"rohithnaraharikk"))
print(k[:16])
print(k[16:32])
if(k[:16]==k[16:32]):			#checking the ciphertext blocks
	print("This is ECB mode encryption")

