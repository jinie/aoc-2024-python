from functools import cache

def parse_input(filename):
    with open(filename) as file:
        return list(map(int,file.read().split()))

@cache
def apply_rules(n: int):
    if n == 0: return [1]
    if len(str(n)) % 2 == 0:
        return [int(str(n)[:len(str(n))//2]), int(str(n)[len(str(n))//2:])]
    return [n * 2024]

@cache
def calculate_num_stones(stone, blinks):
    if blinks == 0: return 1
    transformed_stones = apply_rules(stone)
    return sum(calculate_num_stones(num, blinks - 1) for num in transformed_stones)

if __name__ == "__main__":
    input = parse_input('input/day11.txt')
    print(sum(calculate_num_stones(stone, 25) for stone in input[:]))
    print(sum(calculate_num_stones(stone, 75) for stone in input))