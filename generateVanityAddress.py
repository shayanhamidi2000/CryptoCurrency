import generateAddress
import base58   

def find_vanity_address(first_bytes):
    if (len(first_bytes) > 3):
        return "error","Three first characters(except n/m),at most, must be entered!"
    try:
        base58.b58decode(first_bytes)
    except:
        return "error","Your characters are not in Base58 format!"
    produced_private_key, produced_public_key = generateAddress.produce_keys()
    while produced_public_key.decode("utf-8")[1:(len(first_bytes) + 1)] != first_bytes:
        produced_private_key, produced_public_key = generateAddress.produce_keys()
    return produced_private_key, produced_public_key        

first_three_bytes = input()
private_key, public_key = find_vanity_address(first_three_bytes)
if private_key == "error":
    print(public_key)
else:
    print(private_key.decode("utf-8"))
    print(public_key.decode("utf-8"))