#!/usr/bin/env python3
import sys
import binascii
import logging

logging.basicConfig()
l = logging.getLogger()
l.setLevel(logging.INFO)

line_wrap_length = 38
is_pretty = True # flip to write raw bytes
line_wrap_index = line_wrap_length - 1

input_filename = sys.argv[1]
key = bytes(sys.argv[2], 'ascii')

result = bytearray()
with open(input_filename, 'rb') as f:
    curr_key_index = 0
    for line in f:
        for i in range(0, len(line)):
            curr_char = line[i]
            curr_key_char = key[curr_key_index]
            curr_key_index = (curr_key_index + 1) % 3
            xor_result = curr_char ^ curr_key_char
            l.debug('%s: %d %% %d = %d (%s)' %
                (chr(curr_char), curr_char, curr_key_char, xor_result, hex(xor_result)))
            result.append(xor_result)

def write(bytes_to_write):
    if is_pretty:
        # the challenge page wraps the expected output mid-byte, it's weird and we won't do that
        print(binascii.hexlify(bytes_to_write))
        return
    sys.stdout.buffer.write(binascii.hexlify(bytes_to_write))

pos = 0
accum = bytearray()
for curr in result:
    l.debug('pos=%d, curr=%s' % (pos, hex(curr)))
    if pos == line_wrap_index:
        write(accum)
        pos = 0
        accum = bytearray()
    accum.append(curr)
    pos += 1
write(accum)
