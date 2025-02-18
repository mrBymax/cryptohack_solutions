#!/usr/bin/env python3
import codecs

from pwn import *  # pip install pwntools
import json
import base64
from Crypto.Util.number import long_to_bytes

HOST = "socket.cryptohack.org"
PORT = 13377

# Connect to the server
r = remote(HOST, PORT)


def json_recv():
    line = r.readline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)



while True:
    # Receive the challenge
    line = r.readline()
    response = json.loads(line.decode())

    # If the challenge is the flag, print it and break
    if "flag" in response:
        print(response["flag"])
        break

    # Decode the challenge
    encoding_type = response["type"]
    encoded_value = response["encoded"]

    # Decode the challenge based on the encoding type
    if encoding_type == "base64":
        decoded = base64.b64decode(encoded_value).decode()
    elif encoding_type == "hex":
        decoded = bytes.fromhex(encoded_value).decode()
    elif encoding_type == "utf-8":
        decoded = "".join([chr(b) for b in encoded_value])
    elif encoding_type == "rot13":
        decoded = codecs.decode(encoded_value, 'rot_13')
    elif encoding_type == "bigint":
        decoded = long_to_bytes(int(encoded_value, 16)).decode()

    # Send the decoded challenge back to the server
    json_send({"decoded": decoded})
    print(decoded)

    print(response)
