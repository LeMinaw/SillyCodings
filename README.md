# SillyCodings

Useless data encoding and decoding features.

## guillemets-et-apostrophes.py

Implementation of Kocal's GuillemetsEtApostrophes coding language in Python.

Original : https://github.com/Kocal/GuillemetsEtApostrophes

### Coding table :

  Int  | `'` & `"`
-------|-----------
   0   | `''''''`
   1   |  `''''"`
   2   |  `'''"'`
   3   |  `''"''`
   4   |  `'"'''`
   5   |  `"''''`
   6   |   `''""`
   7   |   `'""'`
   8   |   `""''`
   9   |    `"""`

## i!.py

A module implementing a custom and fun binary language composed of `i` and `!`.
Alternatively, the i can be replaced by a 'spanish' `¡`.

### Coding table :

  Int  |    `i!`
-------|-----------
    0  |    `!`
    1  | `i` or `¡`
