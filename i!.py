#!/usr/bin/env python3

# A module implementing a custom and fun binary language composed of i/¡ and !.

ALPHABET = {'0': '!',
            '1': '¡'} # ¡ or i

ALPHABET_DECODE = dict(zip(ALPHABET.values(), ALPHABET.keys())) # Reverses ALPHABET keys and values


def encode(data_in):
    """Encodes an int to i! str."""

    digits = list(data_in)
    bytes = []
    for digit in digits:
        bytes.append(bin(int(digit)))

    data_out = ''
    for byte in bytes:
        data_out += ALPHABET['0'] * (8 - len(byte[2:])) # Adding '0s' to reach for 8 bits byte
        for bit in byte[2:]: # Skipping '0b'
            data_out += ALPHABET[bit]

    return data_out


def decode(data_in):
    """Decodes a i! str to an int."""

    chars = list(data_in)
    data_out = ''
    group = ''
    for char in chars:
        group += ALPHABET_DECODE[char]
        if len(group) == 8:
            data_out += str(int(group, 2))
            group = ''

    return int(data_out)


if __name__ == '__main__':
    print(encode(input("Int to encode: ")))
    print(decode(input("Str to decode: ")))
