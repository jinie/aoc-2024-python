from itertools import permutations

def parse_input(filename):
    ret = {}
    with open(filename) as f:
        for i,r in enumerate(f):
            for j,c in enumerate(r.strip()):
                ret[i+j*1j] = c
        return ret
    
def part1(grid):
    anti = []
    for freq in {*grid.values()} - {'.'}:
        pairs = permutations([p for p in grid if grid[p] == freq],2)
        anti += [x+i*(x-y) for x,y in pairs
                           for i in [1]]
    return len(set(anti) & set(grid))

def part2(grid):
    anti = []
    for freq in {*grid.values()} - {'.'}:
        pairs = permutations([p for p in grid if grid[p] == freq],2)
        anti += [x+i*(x-y) for x,y in pairs
                           for i in range(50)]
    return len(set(anti) & set(grid))


def main():
    grid = parse_input('input/day8.txt')
    print(part1(grid))
    print(part2(grid))

if __name__ == '__main__':
    main()
