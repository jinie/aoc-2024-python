#!/usr/bin/env python3

def parse_input(filename):
    data = [*map(int, open(filename).read().split())]
    col1, col2 = sorted(data[0::2]), sorted(data[1::2])
    return list(map(int,col1)), list(map(int,col2))

def part1(col1,col2):
    return sum(map(lambda a, b: abs(a-b), col1, col2))

def part2(col1,col2):
    return sum(map(lambda a: a * col2.count(a), col1))

def main():
    (col1, col2) = parse_input('input/day1.txt')
    print(part1(col1, col2)) 
    print(part2(col1, col2)) 

if __name__ == "__main__":
    main()
