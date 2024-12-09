from itertools import permutations

def parse_input(filename):
    ret = {}
    with open(filename) as f:
        for i,r in enumerate(f):
            for j,c in enumerate(r.strip()):
                ret[i+j*1j] = c
        return ret
    

def calculate(grid, niter=1):
    anti = []
    for freq in {*grid.values()} - {'.'}:
        pairs = permutations([p for p in grid if grid[p] == freq],2)
        anti += [x+i*(x-y) for x,y in pairs
                           for i in niter]
        
    return len(set(anti) & set(grid))
def part1(grid):
    return calculate(grid,[1])

def part2(grid):
    return calculate(grid,range(50))

def main():
    grid = parse_input('input/day8.txt')
    print(part1(grid))
    print(part2(grid))

if __name__ == '__main__':
    main()
