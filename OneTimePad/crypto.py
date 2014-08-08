'''
Created on Aug 5, 2014

@author: root
'''

import sys

MSGS = []
KEY = ""
#Strings have to be decoded if the string is in hex
def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
   
def search(i,j,MSGS):
    for x in xrange(10):
        count=0
        for y in xrange(10):
            temp=strxor(MSGS[x][i:j].decode('hex'),MSGS[y][i:j].decode('hex'))
            if ((temp>= "A" and temp<= "Z") or (temp>= "a" and temp<= "z")):
                count+=1
            if count > 5:
                return MSGS[x][i:j]
    return "00"

def findKey(MSGS):
    key=""
    for x in range(0,1024,2):
        key += search(x,x+2,MSGS)
        
    return key
            
def test():
    
    i=4
    j=6
    
    for x in xrange(10):
        count=0
        for y in xrange(10):
            temp=strxor(MSGS[x][i:j].decode('hex'),MSGS[y][i:j].decode('hex'))
            print "M" +str(x)+ " x M" + str(y) + "    " + temp.encode('hex')
            if ((temp>= "A" and temp<= "Z") or (temp>= "a" and temp<= "z")):
                count+=1
            if count > 5:
                print 
                print x
                print MSGS[x][i:j]
                return MSGS[x][i:j]
    return "00".decode('hex')
    
def test2():
    x=0
    y=1
    i=0
    j=2
    print MSGS[x][i:j]
    print MSGS[y][i:j]
    print strxor(MSGS[x][i:j].decode('hex'),MSGS[y][i:j].decode('hex')).encode('hex')
    
    #for x in range(0,1024,2):
    #    print x

    
    
def main():
    MSGS = []
    I = open('Output.txt', 'r')
    K = open('Key.txt','r')
    O = open('Decrypted.txt','w')
    
    for line in I:
        MSGS.append(line.rstrip('\n'))
    
    key = K.readline().rstrip('\n')
    ciphertexts = [decrypt(key, msg) for msg in MSGS]
    for msg in MSGS:
        O.write(decrypt(key, msg)+ "\n")
    
    
    #print findKey(MSGS)
    print strxor(findKey(MSGS).decode('hex'),MSGS[0].decode('hex'))
    #test()

if __name__ == "__main__":
    main()
    
