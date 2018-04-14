#!/usr/bin/python3
# https://cryptopals.com/sets/1/challenges/4
import sys
import binascii
import re
import logging
from functools import reduce

logging.basicConfig()
logger = logging.getLogger('dscxor')
# logger.setLevel(logging.DEBUG)


def process_line(line):
    def process(cypher_char, enc_msg_bytes):
        byte_length = len(enc_msg_bytes)
        out_bytes = bytearray(byte_length)
        for i in range(0, byte_length):
            src_curr = enc_msg_bytes[i]
            xor_result = src_curr ^ cypher_char
            out_bytes[i] = xor_result
        without_alphabet = out_bytes.translate(None, b' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
        letters_count = byte_length - len(without_alphabet)
        return {
            'score': letters_count,
            'msg': out_bytes,
            'input': enc_msg_bytes,
            'cypher_key': cypher_char
        }

    best_scoring_results = {
        'score': 0,
        'records': []
    }
    possible_keys = list(range(0, 256))
    src_hex_bytes_text = line.strip()
    src_parsed_bytes = binascii.unhexlify(src_hex_bytes_text)
    logger.debug('Parsed bytes (len=%d): %s' % (len(src_parsed_bytes), src_parsed_bytes))
    for i in possible_keys:
        r = process(i, src_parsed_bytes)
        curr_score = r['score']
        if curr_score == 0:
            continue
        if curr_score > best_scoring_results['score']:
            best_scoring_results['records'] = [r]
            best_scoring_results['score'] = curr_score
            continue
        if curr_score == best_scoring_results['score']:
            best_scoring_results['records'] += [r]
    return best_scoring_results['records']


global_bests = []
with open(sys.argv[1], 'rb') as f:
    for line in f:
        logger.debug('Raw hex-text line: %s' % line)
        best_results = process_line(line)
        global_bests += best_results

logger.info('Qualifying decoded lines: %d' % len(global_bests))

def getkey(rec):
    return rec['score']
global_bests.sort(key=getkey)
records_to_display=1
for curr in global_bests[-1 * records_to_display:]:
    print('score: %d using key "%s" for result \n    %s\n  with input\n    %s' % (
            curr['score'],
            chr(curr['cypher_key']),
            curr['msg'],
            curr['input'],
        ))
