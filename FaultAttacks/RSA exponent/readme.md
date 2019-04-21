Here is attacker objective is to retrive the RSA secret exponent with the faulty and fault free cipher. This black box attack assumes the attacker has access to the device in which the secret exponent (d) is embedded and targetting the decryption fuction.
Suppose the public key (e,N) is (7,77) and the cipher text value is 37. Given the fault free and faulty messages as 9 and 67 respectively. Assume the fault is at the fourth bit of secret exponent [d3]. Attackers job is to find the value of d3.


code

#!/usr/bin/env python
faulty_msg = 67
def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1
a = []
for i in range(6):
	a.append((9*(37**(2**i)))%77)
temp = []
for j in range(0,6):
	temp.append(modInverse((37**(2**j)),77))
b = []
for i in temp:
	b.append((9*i)%77)
 
if a[3] == faulty_msg:
	print("Target key bit: 0")
elif b[3] == faulty_msg:
	print("Target key bit: 1")
else:
	print("Attack failed!")
 
