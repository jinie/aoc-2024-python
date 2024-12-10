from aoc import profile
import heapq

def parse_input(filename):
    with open(filename) as file:
        grid = {(i, j): int(c) for i, r in enumerate(file) for j, c in enumerate(r.strip())}
        return grid

@profile
def find_paths_and_scores(grid):
    start_positions = [pos for pos, height in grid.items() if height == 0]
    total_score = 0
    total_ratings = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for start in start_positions:
        pq = [(0, start, 0, [])]  # (path_length, (x, y), height, path)
        visited = set()
        distinct_paths = set()

        while pq:
            path_length, (x, y), height, path = heapq.heappop(pq)

            if ((x, y), height, tuple(path)) in visited:
                continue
            visited.add(((x, y), height, tuple(path)))
            
            if grid[(x, y)] == 9:
                distinct_paths.add(tuple(path + [(x, y)]))
                continue

            for dx, dy in directions:
                neighbor = (x + dx, y + dy)
                if neighbor in grid:
                    if grid[neighbor] == height + 1:
                        heapq.heappush(pq, (path_length + 1, neighbor, grid[neighbor], path + [(x, y)]))

        score = len(distinct_paths)  
        rating = len(set([path[-1] for path in distinct_paths]))  
        total_score += score
        total_ratings += rating

    return total_score, total_ratings

def main():
    grid = parse_input('input/day10.txt')
    total_score, total_ratings = find_paths_and_scores(grid)
    print("part 1:", total_ratings)
    print("part 2:", total_score)

if __name__ == '__main__':
    main()
