#!/usr/bin/python3
# https://cryptopals.com/sets/1/challenges/3
import sys
import binascii
import re

best_scoring_result = {'score': 0}

src_hex_bytes_text = sys.argv[1]
src_parsed_bytes = binascii.unhexlify(src_hex_bytes_text)
byte_length = len(src_parsed_bytes)

def process(cypher_char):
    out_bytes = bytearray(byte_length)
    for i in range(0, byte_length):
        src_curr = src_parsed_bytes[i]
        xor_result = src_curr ^ cypher_char
        out_bytes[i] = xor_result
    decoded_ascii = out_bytes.decode('utf-8')
    total_length = len(decoded_ascii)
    without_alphabet = re.sub(r'[A-Za-z]', '', decoded_ascii)
    letters_count = total_length - len(without_alphabet)
    return {
        'score': letters_count,
        'msg': decoded_ascii,
        'cypher_key': cypher_char
    }

for i in range(ord('A'), ord('Z') + 1):
    r = process(i)
    if best_scoring_result['score'] < r['score']:
        best_scoring_result = r

for i in range(ord('a'), ord('z') + 1):
    r = process(i)
    if best_scoring_result['score'] < r['score']:
        best_scoring_result = r

print('Best score: %d using key "%s" with result "%s"' % (
        best_scoring_result['score'],
        chr(best_scoring_result['cypher_key']),
        best_scoring_result['msg'],
    ))
