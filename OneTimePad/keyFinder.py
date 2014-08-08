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
            
def test(MSGS):
    
    i=8
    j=10
    #print MSGS[0][i:j]
    
    for x in xrange(5):
        count=0
        for y in xrange(5):
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
    
def test2(MSGS):
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
    I = open('Encrypted2.txt', 'r')
    K = open('FoundKey.txt','w')
    
    for line in I:
        MSGS.append(line.rstrip('\n'))
        
    print findKey(MSGS)
    K.write(findKey(MSGS) + "\n")


if __name__ == "__main__":
    main()
    
