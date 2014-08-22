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
   
def searchSpace(i,j,MSGS):
    greatestcount = 0
    
    indexMSGS=[]
    
    for x in MSGS:
        if indexMSGS.count(x[i:j]) == 0:
            indexMSGS.append(x[i:j])    
    
    for m in indexMSGS:
        count=0
        
        for n in indexMSGS:
            temp=strxor(m.decode('hex'),n.decode('hex'))
            if ((temp>= "A" and temp<= "Z") or (temp>= "a" and temp<= "z")):
                count+=1
                #print "count: " + str(count) + "    Message M: " + str(MSGS.index(m)) + "    " + m + "    Message N: " + str(MSGS.index(n)) + "    " + n + "    Xor: " + temp.encode('hex')
            if count > greatestcount:
                greatestcount = count
                final = m.decode('hex')
    if greatestcount > 0:
        return strxor(final,"20".decode('hex')).encode('hex')
    return "00"

def findKey(MSGS):
    key=""
    for x in range(0,1024,2):
        key += searchSpace(x,x+2,MSGS)
        
    return key
            
    
    
def main():
    MSGS = []
    I = open('Encrypted Text.txt', 'r')
    K = open('Encryption Key.txt','w')
    
    for line in I:
        MSGS.append(line.rstrip('\n'))
        
    print findKey(MSGS)
    K.write(findKey(MSGS) + "\n")

if __name__ == "__main__":
    main()
    
