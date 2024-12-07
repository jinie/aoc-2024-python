#!/usr/bin/env python
from itertools import product
from functools import cache

def parse_input(filename):
    ret = []
    with open(filename) as f:
        for l in f:
            testvalue,right = l.split(":")
            values = [int(i) for i in right.strip().split(" ")]
            values.insert(0,int(testvalue))
            ret.append(tuple(values))
        return tuple(ret)

calc = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '|': lambda x, y: int(f"{x}{y}"),
}

def evaluate_tests(test_data, operators):
    
    @cache
    def evaluate(test, numbers, operators):
        first, *rest = numbers
        for ops in product(operators, repeat=len(rest)):
            result = first
            for op, num in zip(ops, rest):
                result = calc[op](result, num)
            if(result == test):
                return True
        return False
    
    ret = 0
    for tval, *numbers in test_data:
        if(evaluate(tval, tuple(numbers),operators)):
            ret+=tval
    return ret


def main():
    data = parse_input("input/day7.txt")
    print(evaluate_tests(data,"+*"))
    print(evaluate_tests(data,"+*|"))


if __name__ == "__main__":
    main()