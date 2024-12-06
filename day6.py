#!/usr/bin/env python3

def parse_input(filename):
    with open(filename) as file:
        grid = {i+j*1j: c for i,r in enumerate(file) for j,c in enumerate(r.strip())}
        start = min(p for p in grid if grid[p] == '^')
        return grid, (start, -1)

def traverse_loop(grid, start):
    pos = start[0]
    direction = start[1]
    visited = set()

    while pos in grid and (pos, direction) not in visited:
        visited |= {(pos, direction)}

        if grid.get(pos + direction) == "#":
            direction *= -1j
        else:
            pos += direction    
    return {p for p, _ in visited}, (pos, direction) in visited

def part1(grid, start):
    return traverse_loop(grid, start)


def part2(grid, visited, start):
    return sum(traverse_loop(grid | {o: '#'}, start)[1] for o in visited[0])


def main():
    grid, start = parse_input('input/day6.txt')
    visited = part1(grid, start)
    print(f"Number of unique positions visited: {len(visited[0])}")
    wall_count = part2(grid, visited, start)
    print(f"Number of valid wall placements: {wall_count}")


if __name__ == '__main__':
    main()
