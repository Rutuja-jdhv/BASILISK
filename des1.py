from Crypto.Cipher import DES3
from hashlib import md5

from Crypto.Util.Padding import pad, unpad

while True:
    print('Choose one of the following operations:\n\t1- Encrypt\n\t2- Decrypt')
    operation = input('Your choice: ')
    if operation not in ['1', '2']:
        break
    plaintext = input('Enter message: ')
    key = input('TDES key: ')

    key_hash = md5(key.encode('utf-8')).digest()  # 16-byte key

    BS = DES3.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    unpad = lambda s: s[0:-ord(s[-1])]

    tdes_key = DES3.adjust_key_parity(key_hash)
    cipher = DES3.new(tdes_key, DES3.MODE_ECB)

    if operation == '1':
        # Encrypt
        #cipher = DES3.new(tdes_key, DES3.MODE_EAX)
        plaintext = pad(plaintext)
        ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
        print(f'Encrypted message is: {ciphertext}')

    else:
        # Decrypt
        #cipher = DES3.new(tdes_key, DES3.MODE_EAX,nonce=b'0')
        decrypted_text = cipher.decrypt(ciphertext.decode('utf-8'))
        decrypted_text = unpad(decrypted_text)
        print(f'Decrypted message is: {decrypted_text}')
