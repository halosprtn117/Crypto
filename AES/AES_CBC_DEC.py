import sys

from Crypto.Cipher import AES

K = open('Encryption Key.txt','r')
key = K.readline().rstrip('\n')

MSGS = []
M = open('Encrypted Test.txt', 'r')
    
for line in M:
    MSGS.append(line.rstrip('\n'))

#Strings have to be decoded if the string is in hex
def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def unpadd(msg):
    temp=msg
    padd_bytes = temp[len(temp)-2:len(temp)].decode('hex')
    
    return temp[0:len(temp)-ord(padd_bytes)*2]

def cbc(previous, next):
    temp = strxor(previous.decode('hex'),next.decode('hex'))
    aes = AES.new(key)
    return aes.encrypt(temp).encode('hex')

def encryption(msg):
    length = len(msg)
    num_mess = length/len(key.encode('hex'))
    temp=IV.encode('hex')
    
    for x in range(0,num_mess):
        temp+=cbc(temp[x*32:(x+1)*32],msg[x*32:(x+1)*32])

    return temp



def main():
    print "Message: \t\t" + MSGS[0]


    print "IV: \t\t\t" + IV.encode('hex')
    #addIV(MSGS,0)
    prepared=padd(IV,MSGS[0])
    print "Prepared Message: \t" + prepared
    print "KEY: \t\t\t" + key.encode('hex')
    
    print "My Encryption: \t\t" + encryption(prepared)
    
    aes=AES.new(key,AES.MODE_CBC, IV)
    print "Python Encryption: \t" + IV.encode('hex') + aes.encrypt(prepared.decode('hex')).encode('hex')



if __name__ == "__main__":
    main()
