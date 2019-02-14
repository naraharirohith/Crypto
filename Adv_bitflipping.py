from pwn import *
from itertools import cycle
def xor(a,b):
    return ''.join(chr(ord(i)^ord(j)) for i,j in zip(a,cycle(b)))

a = remote("13.234.27.172", 1337)
a.recvuntil("choice: ")
a.sendline("1")
a.recvuntil("register: ")
a.sendline("admix")
cookie=a.recvline()
a.close()
cookie=cookie[29:-1]
print(cookie)
cookie=cookie.decode('hex')
q=chr(ord(cookie[20]) ^ ord('n') ^ ord('x'))
cookie=cookie[:20]+q+cookie[21:]
cookie=cookie.encode('hex')



a = remote("13.234.27.172", 1337)
a.recvuntil("choice: ")
a.sendline("2")
a.recvuntil("cookie: ")
a.sendline(cookie)
a.recvline()
k=a.recvline()
a.close()
print(k)
k=k[:-5]
cookie=cookie.decode('hex')
cookie=xor(cookie[:16],xor("cookie?username=",k[:16]))+cookie[16:]
cookie=cookie.encode('hex')
print(cookie)
a = remote("13.234.27.172", 1337)
a.recvuntil("choice: ")
a.sendline("2")
a.recvuntil("cookie: ")
a.sendline(cookie)
j=a.recvline()
a.close()
print(j)
