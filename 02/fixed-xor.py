#!/usr/bin/python3
# https://cryptopals.com/sets/1/challenges/2
import sys
import binascii
src1_hex_bytes_text = sys.argv[1]
src1_parsed_bytes = binascii.unhexlify(src1_hex_bytes_text)
src2_hex_bytes_text = sys.argv[2]
src2_parsed_bytes = binascii.unhexlify(src2_hex_bytes_text)
byte_length = len(src1_parsed_bytes)
out_bytes = bytearray(byte_length)
for i in range(0, byte_length):
  src1_curr = src1_parsed_bytes[i]
  src2_curr = src2_parsed_bytes[i]
  xor_result = src1_curr ^ src2_curr
  out_bytes[i] = xor_result
result = binascii.hexlify(out_bytes)
sys.stdout.buffer.write(result)
