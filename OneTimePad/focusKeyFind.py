import decryptor, encryptor, keyFinder

def main():
    MSGS=[]
    K = open('FoundKey.txt','r')
    key = K.readline().rstrip('\n')
    K.close()
    
    I = open('Encrypted2.txt', 'r')
    for line in I:
        MSGS.append(line.rstrip('\n'))
        
    msg_num = int(raw_input('Enter message index: '))
    char_num = int(raw_input('Enter character index: '))
    char_guess = raw_input('Enter character guess: ')
    
    temp = decryptor.strxor(char_guess, MSGS[msg_num][(2*char_num-2):(2*char_num)].decode('hex')).encode('hex')   
    

    key = key[0:(2*char_num-2)] + temp + key[(2*char_num):len(key)]
    K = open('FoundKey.txt','w')
    K.write(key + "\n")
    

if __name__ == "__main__":
    main()
