import secrets as sec
import base58 as base58
from generateAddress import Sha256, RipeMD160

def calculate_checksum(key):
    hashed_data = Sha256(Sha256(key))
    return hashed_data[:4]

def produce_WIF_private_key():
    pure_hex_private_key = sec.token_bytes(32)
    extended = b"\xef" + pure_hex_private_key
    checksum = calculate_checksum(extended)
    WIF_private_key_not_encoded = extended + checksum
    return pure_hex_private_key, base58.b58encode(WIF_private_key_not_encoded)

pk, pkWIP = produce_WIF_private_key()
print(pk)
print(pkWIP)
