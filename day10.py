import heapq

def parse_input(filename):
    with open(filename) as file:
        grid = {(i, j): int(c) for i, r in enumerate(file) for j, c in enumerate(r.strip())}
        return grid

def find_paths(grid):
    start_positions = [pos for pos, height in grid.items() if height == 0]
    total_score = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for start in start_positions:
        pq = [(0, start, 0)]  # (path_length, (x, y), height)
        visited = set()
        reachable_nines = set()

        while pq:
            path_length, (x, y), height = heapq.heappop(pq)

            if ((x, y), height) in visited:
                continue
            visited.add(((x, y), height))
            
            if grid[(x, y)] == 9:
                reachable_nines.add((x, y))
                continue

            for dx, dy in directions:
                neighbor = (x + dx, y + dy)
                if neighbor in grid and ((neighbor, grid[neighbor])) not in visited:
                    # Check if the neighbor height is the next in sequence
                    if grid[neighbor] == height + 1:
                        heapq.heappush(pq, (path_length + 1, neighbor, grid[neighbor]))

        score = len(reachable_nines)
        total_score += score

    return total_score

def main():
    grid = parse_input('input/day10.txt')
    result = find_paths(grid)
    print("Total score:", result)

if __name__ == '__main__':
    main()
