#!/usr/bin/env python3
from aoc import profile

def parse_input(filename):
    ret = []
    with open(filename) as f:
        for line in f:
            ret.append([int(x) for x in line.split()]) 
    return ret

increasing = lambda line: all(x < y for x, y in zip(line, line[1:])) or all(x > y for x, y in zip(line, line[1:]))
diff = lambda line: all(abs(x-y) <= 3 for x, y in zip(line, line[1:]))

@profile               
def part1(data):
    return sum(1 for line in data if increasing(line) and diff(line))

@profile
def part2(data, valid):
    count = 0
    for line in data:
        if not increasing(line) or not diff(line):
            for i in range(len(line)):
                if increasing(line[:i] + line[i+1:]) and diff(line[:i] + line[i+1:]):
                    count+=1
                    break
    return count+valid

def main():
    input = parse_input("input/day2.txt")
    valid = part1(input)
    print(valid)
    print(part2(input,valid))

if __name__ == "__main__":
    main()