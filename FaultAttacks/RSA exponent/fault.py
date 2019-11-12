#!/usr/bin/env python

"""
__Author__      : Paulson Mathew
__Email__       : paulsonmathew21irtn@gmail.com

Licence


Actual Private Key : 43 = 0b101011
Private key: (d, N) is (43, 77)
Public key: (e, N) is (7,77)
cipher text value is 37

"""

k_priv = 43             # Private Key
faulty_msg = 67         # Faulty message after decryption
ct = 37                 # Actual Cipher Text
pt = 9                  # Actual Plain Text after RSA decryption
f_pt = 67               # Faulty plain text after decryption and introducing fault
N = 77                  # Public prime used for RSA crypto


def mod_inverse(val, m):
    val = val % m
    for x in range(1, m):
        if (val * x) % m == 1:
            return x
    return 1


def simple_rsa_encrypt(m, k_pub, prime):
    """
    Method to do simple rsa operation. Note that this is not an efficient implementation for crypto application.
    :param m: Message
    :param k_pri: Private key
    :param prime: Prime number
    :return: Cipher text
    """
    return (m**k_pub)%prime


def simple_rsa_decrypt(ct, k_pri, prime):
    """
    Method to decrypt. This method can be used to determine faulty cipher text for experiment
    :param ct: Cipher Text
    :param k_pri: Private
    :param prime: RSA prime
    :return: Decrypted Plain Text
    """
    return (ct ** k_pri) % prime


def attack(pt, f_pt, N, i):
    """
    This method performs the attack.
    :param pt: Actual plain text value
    :param f_pt: Faulty plain text value
    :param N: Prime
    :return: Key bit if attack successful, and FALSE otherwise
    """

    if pt == (f_pt*37**(2**i)) % N:
        print("----- Attack Successful -----")
        print("Bit %5d is: 1 " % (i + 1))
        return 1
    elif f_pt == (pt*37**(2**i)) % N:
        print("----- Attack Successful -----")
        print("Bit %5d is: 0 " % (i + 1))
        return 0

    print("----- Attack Failed -----")
    return -1


def key_extraction(pt, ct, n):                       # Automate the key extraction feature
    k_priv_binary = bin(k_priv)[2:]
    print(k_priv_binary)
    for i in range(6):
        if k_priv & (1 << i):
            mask = ~(1 << i)                        # Mask for clearing i th bit
            f_k_priv = k_priv & mask
        else:
            mask = (1 << i)                         # Mask for set the i th bit
            f_k_priv = k_priv | mask
        if attack(pt, (simple_rsa_decrypt(ct, f_k_priv, n)), n, i) == -1:
            print ("Terminating simulator..!")
            break
    pass

key_extraction(9, 37, 77)

# print (simple_rsa_encrypt(9, 7, 77))
# print (simple_rsa_decrypt(37, 43, 77))                   # 43 : 0b101011

# print (simple_rsa_decrypt(37, 35, 77))
# attack(9, 67, 77)


# print (simple_rsa_decrypt(37, 47, 77))
# attack(9, 60, 77)


def __initial_approach__():
    """
    This was the initial approach
    :return:
    """
    a = []
    for i in range(6):
        a.append((9 * (37 ** (2 ** i))) % 77)
    temp = []
    for j in range(0, 6):
        temp.append(mod_inverse((37 ** (2 ** j)), 77))
    b = []
    for i in temp:
        b.append((9 * i) % 77)

    if a[3] == faulty_msg:
        print("Target key bit: 0")
    elif b[3] == faulty_msg:
        print("Target key bit: 1")
    else:
        print("Attack failed!")
