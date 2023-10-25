abjadDictionary = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
abjadTabel = {letter: index for index, letter in enumerate(abjadDictionary)}

def display_abjad_tabel():
    print("Abjad Tabel:")
    for letter, value in abjadTabel.items():
        print(f"{letter}: {value}")

def autokey_encrypt(plaintext, key):
    keyLength = len(key)
    plaintextLength = len(plaintext)
    
    if keyLength < plaintextLength:
        
        keystream = (key * (plaintextLength // keyLength)) + key[:plaintextLength % keyLength]
    else:
        keystream = key
    
    keyinDict = [abjadTabel[i.lower()] for i in keystream]
    result = ''

    for i in range(plaintextLength):
        if plaintext[i] == ' ':
            result += ' '
        else:
            value = (abjadTabel[plaintext[i].lower()] + keyinDict[i % keyLength])
            result += abjadDictionary[value % 52]
            keyinDict.append(abjadTabel[plaintext[i].lower()])

    return result

  

def autokey_decrypt(ciphertext, key):
    keyLength = len(key)
    keyinDict = [abjadTabel[letter] for letter in key]
    result = ''

    for i in range(len(ciphertext)):
        if ciphertext[i] == ' ':
            result += ' '
        else:
            letter = ciphertext[i].lower()
            value = (abjadTabel[letter] - keyinDict[i % keyLength])
            result += abjadDictionary[value % 52]
            keyinDict.append(abjadTabel[letter])

    return result

def main():
    display_abjad_tabel()
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")
    
    encrypted = autokey_encrypt(plaintext, key)
    decrypted = autokey_decrypt(encrypted, key)

    print("Autokey Vigenere Cipher")
    print("Key: %s" % key)
    print("Plaintext: %s" % plaintext)
    print("Encrypted: %s" % encrypted)
    print("Decrypted: %s" % decrypted)

if __name__ == '__main__':
    main()
