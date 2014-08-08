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

def decrypt(key, msg):
    #strxor(MSGS[x][i:j].decode('hex'),MSGS[y][i:j].decode('hex')).encode('hex')
    c = strxor(key.decode('hex'), msg.decode('hex'))
    print
    print c
    return c

def main():
    MSGS = []
    I = open('Encrypted2.txt', 'r')
    K = open('FoundKey.txt','r')
    O = open('Decrypted.txt','w')
    
    for line in I:
        MSGS.append(line.rstrip('\n'))
    
    key = K.readline().rstrip('\n')
    for msg in MSGS:
        O.write(decrypt(key, msg)+ "\n")

        
if __name__ == "__main__":
    main()
