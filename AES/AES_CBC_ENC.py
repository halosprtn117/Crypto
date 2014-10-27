import sys

from Crypto import Random
from Crypto.Cipher import AES

IV = Random.new().read(16)
key = Random.new().read(16)
K = open('Encryption Key.txt','w')
K.write((key + "\n").encode('hex'))


MSGS = []
I = open('Messages.txt', 'r')
    
for line in I:
    MSGS.append(line.rstrip('\n').encode('hex'))
    
#MSGS[0]="00000000000000000000000000000000"

#Strings have to be decoded if the string is in hex
def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


def addIV(MSGS,m):
    MSGS[m]=IV.encode('hex')+"" + MSGS[m]
    

def padd(IV,msg):
    mess_length=len(msg)/2
    IV_len=len(IV.encode('hex'))/2
    extra_bytes=mess_length%IV_len
    padd_bytes=IV_len-extra_bytes
    
    for x in range(0,padd_bytes):
        msg+="{:02x}".format(padd_bytes)

    return msg

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
