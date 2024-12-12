def find_areas_and_perimeters(grid):
    def dfs(x, y, char):
        # If out of bounds or not the target character, return
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or visited[x][y] or grid[x][y] != char:
            return 0, 0

        # Mark the cell as visited
        visited[x][y] = True

        # Initialize area and perimeter for the current cell
        area = 1
        perimeter = 0

        # Iterate over the 4 cardinal directions (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            # Check if the neighboring cell is out of bounds or not the target character
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != char:
                perimeter += 1
            else:
                # Recur for unvisited neighbors
                if not visited[nx][ny]:
                    sub_area, sub_perimeter = dfs(nx, ny, char)
                    area += sub_area
                    perimeter += sub_perimeter

        return area, perimeter

    # Initialize visited matrix
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Result list to store area * perimeter for each region
    results = []

    # Iterate through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j]:
                char = grid[i][j]
                area, perimeter = dfs(i, j, char)
                if area > 0:
                    results.append((char, area, perimeter, area * perimeter))

    return results

with open("input/day12.txt") as f:
    grid = [list(line.strip()) for line in f]

result = find_areas_and_perimeters(grid)
p1 = sum(area * perimeter for _, area, perimeter, _ in result)
#for char, area, perimeter, price in result:
#    print(f"Region {char}: Area = {area}, Perimeter = {perimeter}, Price = {price}")
print(f"sum of area * perimeter: {p1}")