#!/usr/bin/python3
# https://cryptopals.com/sets/1/challenges/1
# thanks to https://www.devdungeon.com/content/working-binary-data-python
import sys
import binascii
hex_bytes_text = sys.argv[1]
parsed_bytes = binascii.unhexlify(hex_bytes_text)
result = binascii.b2a_base64(parsed_bytes)
print(result.rstrip(), end='')
