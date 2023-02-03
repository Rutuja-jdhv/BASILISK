import random
import string
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.Padding import pad


def IV_Generation():
    IV = ""
    for i in range(15):
        C = random.choice(string.ascii_letters + string.digits)
        IV = IV + C
    print('\nYour 16-Bit Initialization vector for AES is :', IV)
    response = input('\nDo you want to return to the Main Page?[Y/N]: ')
    if response == 'y' or response == 'Y':
        main()
    elif response == 'n' or response == 'N':
        print('\nExiting RC4...\n')
        exit()


def Encrypt():
    key = ""
    iv = ""
    plain_text = ""
    print('AES Encryption')
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    iv = bytes(input('\nEnter your 16-Bit Initialization vector : '), 'utf-8')
    key = bytes(input('\nEnter your Key : '), 'utf-8')
    plain_text = bytes(input('\nEnter your Plaintext: '), 'utf-8')
    cipher = AES.new(pad(key, AES.block_size), AES.MODE_CBC, pad(iv, AES.block_size))
    cipher_text = cipher.encrypt(pad(plain_text, AES.block_size))
    print('\nYour encrypted CipherText: ', cipher_text)
    response = input('\n\nDo you want to return to the Main Page?[Y/N]: ')
    if response == 'y' or response == 'Y':
        main()
    elif response == 'n' or response == 'N':
        print('\nExiting AES...\n')
        exit()


def Decrypt():
    key = ""
    iv = ""
    cipher_text = ""
    print('AES Encryption')
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    iv = bytes(input('\nEnter your 16-Bit Initialization vector : '), 'utf-8')
    key = bytes(input('\nEnter your Key : '), 'utf-8')
    cipher_text = input('\nEnter your Cipher_text: ')
    print(cipher_text)
    cipher = AES.new(pad(key, AES.block_size), AES.MODE_CBC, pad(iv, AES.block_size))
    plain_text = cipher.decrypt(cipher_text)
    print('\nYour encrypted PlainText is : ', plain_text)
    response = input('\n\nDo you want to return to the Main Page?[Y/N]: ')
    if response == 'y' or response == 'Y':
        main()
    elif response == 'n' or response == 'N':
        print('\nExiting AES...\n')
        exit()


def main():
    print('Welcome to AES Algorithm\n')
    print('1. Generate Initialization vector (Recommended)')
    print('2. Encryption')
    print('3. Decryption')
    print('4. Exit')
    response = input('\nEnter your response: ')
    if response == '1':
        IV_Generation()
    elif response == '2':
        Encrypt()
    elif response == '3':
        Decrypt()
    elif response == '4':
        print('\nExiting AES...\n')
        exit()


try:
    main()
except KeyboardInterrupt:
    print('\n\nKeyboard Interrupt found\n\nExiting AES...\n')
    exit()