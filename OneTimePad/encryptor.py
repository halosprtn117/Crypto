'''
Created on Aug 5, 2014

@author: root
'''
import sys

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    this=open("/dev/urandom").read(size)
    return this

def encrypt(key, msg):
    c = strxor(key, msg)
    print
    print c.encode('hex')
    return c

def main():
    MSGS = []
    I = open('Input.txt', 'r')
    K = open('Key.txt', 'w')
    O = open('Output.txt','w')
    for line in I:
        MSGS.append(line.rstrip('\n'))
        
    key = random(1024)
    K.write(key.encode('hex') + "\n")

    ciphertexts = [encrypt(key, msg) for msg in MSGS]
    for msg in MSGS:
        O.write(encrypt(key, msg).encode('hex') + "\n")
        
if __name__ == "__main__":
    main()
