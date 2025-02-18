from Crypto.Cipher import AES
import requests
import time
import string


def enc(payload):
    url = 'https://aes.cryptohack.org/ecb_oracle/encrypt/'
    r = requests.get(url + payload + '/')
    return r.json()['ciphertext']


def print_in_blocks(hex_blks, size):
    for i in range(0, len(hex_blks), size):
        print(hex_blks[i:i + size])
    print()


def bruteforce():
    flag = 'crypto{'  # 7
    total = 31
    alphabet = string.digits + string.ascii_lowercase + '_' + '@' + '}'

    print('Flag: ' + flag)

    while True:
        # payload = '1' * (total - len(flag))
        payload = "crypto{" + '1' * (total - len(flag) - 7)
        expected = enc(payload.encode().hex())
        # print('E = ' + expected)
        # print_in_blocks(expected, 32)

        for c in alphabet:
            res = enc((payload + flag + c).encode().hex())
            # print(c, ' ', end='')
            # print_in_blocks(res, 32)

            if res[:total * 2] == expected[:total * 2]:
                flag += c
                print('Flag: ' + flag)
                break
            time.sleep(1)

        if '}' in flag:
            print('Flag: ' + flag)
            return flag

bruteforce()
