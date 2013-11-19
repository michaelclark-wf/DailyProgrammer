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
        print i,fletcher_hash_16(s)
        i+=1

def fletcher_hash_16(s):
    sum1 = sum(map(ord,s)) % 255
    sum2 = (sum(map(ord,s)) + sum1) % 255
    return hex((sum2 << 8) | sum1)

if __name__ == '__main__':
    main()