import encryptor

def main():
    MSGS = []
    CYPH = []
    I1 = open('Decrypted.txt', 'r')
    I2 = open('Encrypted2.txt', 'r')
    K = open('FoundKey.txt','w')
    
    for line in I1:
        MSGS.append(line.rstrip('\n'))
        
    for line in I2:
        CYPH.append(line.rstrip('\n'))

    key = encryptor.strxor(MSGS[6],CYPH[6].decode('hex')).encode('hex')
    
    K.write(key + "\n")
    
if __name__ == "__main__":
    main()