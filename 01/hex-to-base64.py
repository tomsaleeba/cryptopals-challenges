# thanks to https://www.devdungeon.com/content/working-binary-data-python
from __future__ import print_function
import sys
import binascii
hex_bytes_text = sys.argv[1]
parsed_bytes = binascii.unhexlify(hex_bytes_text)
result = binascii.b2a_base64(parsed_bytes)
print(result.rstrip(), end='')
