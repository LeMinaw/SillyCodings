#!usr/env python3

ALPHABET = {0: '!',
            1: 'i'}

ALPHABET_DECODE = dict(zip(ALPHABET.values(), ALPHABET.keys())) # Reverses ALPHABET keys and values

def encode(data_in):
    """Encodes an int to i! str."""
    
    digits = list(data_in)
    bytes = []
    for digit in digits:
        bytes.append(bin(digit))
    
    data_out = ''
    for byte in bytes:
        for bit in byte:
            data_out += ALPHABET[bit]
    
    return data_out

def decode(data_in):
    """Decodes a i! str to an int."""
    
    chars = list(data_int)
    data_out = ''
    
    for char in chars:
        data_out += ALPHABET_DECODE[char]
    
    return int(bin(int(data_out)))