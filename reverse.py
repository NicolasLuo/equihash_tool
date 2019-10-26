
def reverse(strhex):
    a_bytes = bytearray.fromhex(strhex)
    a_bytes.reverse()
    return a_bytes.hex()

