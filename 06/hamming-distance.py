def hamming_distance(s1, s2): # thanks https://en.wikipedia.org/wiki/Hamming_distance
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))

def ascii_to_binary(s):
  """Converts an ASCII byte array to a string of the binary bit (as bytes) equivalent"""
  result = ''
  for curr in s:
    bin_str = bin(curr)
    clean_bin_str = bin_str.replace('0b', '')
    byte_bin_str = ('0000000' + clean_bin_str)[-8:]
    result += byte_bin_str
  return result

in1 = b'this is a test'
bin_in1 = ascii_to_binary(in1)
in2 = b'wokka wokka!!!'
bin_in2 = ascii_to_binary(in2)
print('%s = %s' % (in1, bin_in1))
print('%s = %s' % (in2, bin_in2))
print(hamming_distance(bin_in1, bin_in2))
