'''
Created on Aug 5, 2014

@author: root
'''

import sys


#Strings have to be decoded if the string is in hex
def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
   
def search(i,j,MSGS):
    for m in MSGS:
        
        
        
        
        count=0
        
        
        
        
        
        for n in MSGS:
            temp=strxor(m[i:j].decode('hex'),n[i:j].decode('hex'))
            if ((temp>= "A" and temp<= "Z") or (temp>= "a" and temp<= "z")):
                count+=1
            if count > 3:
                
                return strxor(m[i:j].decode('hex'),"20".decode('hex')).encode('hex')
    return "00"

def findKey(MSGS):
    key=""
    for x in range(0,1024,2):
        key += search(x,x+2,MSGS)
        
    return key
    
def main():
    MSGS = []
    I = open('Encrypted2.txt', 'r')
    K = open('FoundKey.txt','w')
    
    for line in I:
        MSGS.append(line.rstrip('\n'))
        
    print findKey(MSGS)
    K.write(findKey(MSGS) + "\n")


if __name__ == "__main__":
    main()
    
