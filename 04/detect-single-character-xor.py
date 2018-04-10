#!/usr/bin/python3
# https://cryptopals.com/sets/1/challenges/3
import sys
import binascii
import re
from functools import reduce

global_bests = []

def process_line(line):
    best_scoring_results = {
        'score': 0,
        'records': []
    }

    def process(cypher_char, enc_msg_bytes):
        src_parsed_bytes = enc_msg_bytes
        # src_parsed_bytes = binascii.unhexlify(enc_msg_bytes)
        # print(enc_msg_bytes[0])
        # print(src_parsed_bytes[0])
        byte_length = len(src_parsed_bytes)
        out_bytes = bytearray(byte_length)
        for i in range(0, byte_length):
            src_curr = src_parsed_bytes[i]
            xor_result = src_curr ^ cypher_char
            out_bytes[i] = xor_result
        try:
            decoded_ascii = out_bytes.decode('utf-8')
        except UnicodeDecodeError:
            return {'score': 0, 'bytes': out_bytes}
        total_length = len(decoded_ascii)
        without_alphabet = re.sub(r'[A-Za-z\'\.]', '', decoded_ascii)
        letters_count = total_length - len(without_alphabet)
        return {
            'score': letters_count,
            'msg': out_bytes,
            'input': enc_msg_bytes,
            'cypher_key': cypher_char
        }

    possible_keys = list(range(ord('0'), ord('z') + 1))
    src_hex_bytes_text = line.strip()
    for i in possible_keys:
        r = process(i, src_hex_bytes_text)
        curr_score = r['score']
        if curr_score > best_scoring_results['score']:
            best_scoring_results['records'] = [r]
            best_scoring_results['score'] = curr_score
            continue
        if curr_score == 0:
            continue
        if curr_score == best_scoring_results['score']:
            best_scoring_results['records'].append(r)
    return best_scoring_results

with open(sys.argv[1], 'rb') as f:
    for line in f:
        best_results = process_line(line)
        if best_results['score'] > 0:
            global_bests.append(best_results['records'][0])
            if len(best_results['records']) > 1:
                print('more than 1 best record, dumping')
                for curr_best in best_results['records']:
                    print('  %s' % curr_best['msg'])
        # break # remove

print('Processed %d lines' % len(global_bests))

def highest_score(accum, curr):
    # print(curr)
    if curr['score'] >= accum['score']:
        accum['score'] = curr['score']
        accum['matches'] = [curr]
    elif curr['score'] == accum['score']:
        accum['matches'].append(curr)
    return accum

best_best = reduce(highest_score, global_bests, {
    'score': 0,
    'matches': []})
for curr in best_best['matches']:
    print('Best score: %d using key "%s" for input "%s" with result "%s"' % (
            curr['score'],
            chr(curr['cypher_key']),
            curr['input'],
            curr['msg'],
        ))
