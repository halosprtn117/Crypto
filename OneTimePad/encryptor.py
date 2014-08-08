'''
Created on Aug 5, 2014

@author: root
'''
import sys

MSGS = ["this", "that"]

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        print "Message 1:    " + a.encode('hex')
        print "Message 2:    " + b.encode('hex')
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        print "Message 1:    " + b.encode('hex')
        print "Message 2:    " + a.encode('hex')
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    this=open("/dev/urandom").read(size)
    print "KEY:    " + this.encode('hex')
    return this

def encrypt(key, msg):
    c = strxor(key, msg)
    print
    print c.encode('hex')
    return c

def main():
    key = random(1024)
    ciphertexts = [encrypt(key, msg) for msg in MSGS]
        
        
if __name__ == "__main__":
    main()
