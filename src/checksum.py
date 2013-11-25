#!/usr/bin/python
# demo.py - CMD Args Demo By nixCraft

## Sample Input
    # 3
    # Fletcher
    # Sally sells seashells by the seashore.
    # Les chaussettes de l'archi-duchesse, sont-elles seches ou archi-seches ?
## Sample Output
    # 1 D330
    # 2 D23E
    # 3 404D

import sys

def main():
    i = 1
    for s in sys.stdin.readlines()[1:]:
        print i,fletcher_hash_16_optimized(s)
        i+=1

def fletcher_hash_16(s):
    sum1 = sum(map(ord,s)) % 255
    sum2 = (sum(map(ord,s)) + sum1) % 255
    return hex((sum2 << 8) | sum1)

def fletcher_hash_16_optimized(s):
    words = len(s.split(' '))
    ascii_sum = sum(map(ord, s))
    print "words:",words
    print "ascii_sum:",ascii_sum
    # slen = slen > 359 ? 359 : slen  #why isn't ternary working!?
    sum1,sum2 = 0,0
    while words:
        tlen = words
        if words <= 359:
            tlen=359
        words = words - tlen
        while tlen:
            ascii_sum = ascii_sum + 1
            sum1 = sum1 + ascii_sum
            sum2 = sum2 + sum1
            tlen = tlen - 1

    sum1 = (sum1 & 0xffff) + (sum >> 16)
    sum2 = (sum2 & 0xffff) + (sum >> 16)
    return sum2 << 16 | sum1





    return

if __name__ == '__main__':
    main()