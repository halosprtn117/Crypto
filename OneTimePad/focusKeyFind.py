import decryptor, encryptor, keyFinder

def edit(msg_num, char_num,char_guess):
    MSGS=[]
    K = open('Encryption Key.txt','r')
    key = K.readline().rstrip('\n')
    K.close()
    
    I = open('Encrypted Text.txt', 'r')
    for line in I:
        MSGS.append(line.rstrip('\n'))
        
    temp = decryptor.strxor(char_guess, MSGS[msg_num][(2*char_num-2):(2*char_num)].decode('hex')).encode('hex')   
    

    key = key[0:(2*char_num-2)] + temp + key[(2*char_num):len(key)]
    K = open('Encryption Key.txt','w')
    K.write(key + "\n")
    K.close()
    I.close()
    decryptor.main()



def main():
    MSGS=[]
    K = open('Encryption Key.txt','r')
    key = K.readline().rstrip('\n')
    K.close()
    
    I = open('Encrypted Text.txt', 'r')
    for line in I:
        MSGS.append(line.rstrip('\n'))
        
    msg_num = int(raw_input('Enter message index: '))
    msg_num = msg_num - 1
    char_num = int(raw_input('Enter character index: '))
    char_guess = raw_input('Enter character guess: ')
    
    temp = decryptor.strxor(char_guess, MSGS[msg_num][(2*char_num-2):(2*char_num)].decode('hex')).encode('hex')   
    

    key = key[0:(2*char_num-2)] + temp + key[(2*char_num):len(key)]
    K = open('Encryption Key.txt','w')
    K.write(key + "\n")
    K.close()
    I.close()
    decryptor.main()
    

if __name__ == "__main__":
    main()
