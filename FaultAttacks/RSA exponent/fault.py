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
 
