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

class Fletcher16Input:
    numLines = 0
    lines    = []
    out      = []



def main():
    data = get_input()
    for i in xrange(0,len(data.lines)):
        line = data.lines[i]
        line_len = len(line)
        ascii_line = line_to_ascii(line)
        fletch = fletch16(ascii_line, line_len)
        data.out.append("%d %s" % (i, fletch))
    send_output(data.out)
    return

def get_input():
    inputData = Fletcher16Input()
    lines     = sys.stdin.readlines()
    # inputData.numLines = int(lines[0])  #first line will be integer representing total # of checksums to preform
    inputData.lines  = lines[1:] #fill data array with remaining lines
    return inputData

def send_output(output):
    for line_out in output:
        print line_out
    return

def line_to_ascii(line):
    ret = []
    for char in line:
        ret.append(ord(char))
    return ret

def fletch16(data, count):
    sum1, sum2 = 0,0
    for i in xrange(0,count):
        sum1 = (sum1 + data[i]) % 255
        sum2 = (sum2 + sum1) % 255
    ret = (sum2 << 8) | sum1
    return hex(ret).split('x')[1]


if __name__ == '__main__':
    main()