a = "nhlie~q4"
b = "dj:fiRz?"
c = "Oc!e'{qj"
t = a + b + c

for i in range(len(t)):
    print(chr(ord(t[i]) ^ i), end="")

print("")
