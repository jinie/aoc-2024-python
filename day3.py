#!/usr/bin/env python3

import re

def parse_input(filename):
    with open(filename) as f:
        return f.read().strip()

def part2(s):
    mul = 1
    ret = 0
    for x, y, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", s):
        if do or dont:
            mul = 1 if do else 0
        else:   
            ret += int(x) * int(y) * mul
    return ret

def part1(input):
    return sum([int(x) * int(y) for x, y in re.findall(r'mul\((\d+),(\d+)\)', input)])

def main():
    input = parse_input('input/day3.txt')
    print(part1(input))
    print(part2(input))

if __name__ == '__main__':
    main()