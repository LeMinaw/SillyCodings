#!/usr/bin/env python3

# A module implementing Kocal's GuillemetsEtApostrophes language encoding and decoding capabilities.

ALPHABET = {'0': "''''''",
            '1': "''''\"",
            '2': "'''\"'",
            '3': "''\"''",
            '4': "'\"'''",
            '5': "\"''''",
            '6': "''\"\"",
            '7': "'\"\"'",
            '8': "\"\"''",
            '9': "\"\"\""}


ALPHABET_DECODE = dict(zip(ALPHABET.values(), ALPHABET.keys())) # Reverses ALPHABET keys and values


def encode(data_in):
    """Encodes an int to a GuillemetsEtApostrophes string."""

    chars = list(str(data_in))
    data_out = ""

    for char in chars:
        data_out += ALPHABET[char]

    return data_out


def decode(data_in):
    """Decodes a GuillemetsEtApostrophes string to an int."""

    chars = list(data_in)
    group = ""
    group_len = 0
    data_out = ""

    for char in chars:
        if char == "'":
            group_len += 1
        elif char == "\"":
            group_len += 2
        else:
            raise ValueError
        group += char

        if group_len == 6:
            data_out += ALPHABET_DECODE[group]
            group = ""
            group_len = 0
        elif group_len > 6:
            raise ValueError

    return int(data_out)


if __name__ == '__main__':
    print(encode(input("Int to encode: ")))
    print(decode(input("Str to decode: ")))
