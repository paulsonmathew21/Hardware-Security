Here is attacker objective is to retrive the RSA secret exponent with the faulty and fault free cipher. This black box attack assumes the attacker has access to the device in which the secret exponent (d) is embedded and targetting the decryption fuction.
Suppose the public key (e,N) is (7,77) and the cipher text value is 37. Given the fault free and faulty messages as 9 and 67 respectively. Assume the fault is at the fourth bit of secret exponent [d3]. Attackers job is to find the value of d3.

A slight modification of the code allows the attacker to find the key index if its not given.

