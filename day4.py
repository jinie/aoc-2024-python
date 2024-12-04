#!/usr/bin/env python3

def count_word_instances(s, word):
    H, W = len(s), len(s[0])-1
    grid = {(y,x):s[y][x] for y in range(H) for x in range(W)}
    deltas = [(dy,dx) for dy in [-1,0,1] for dx in [-1,0,1] if (dx!=0 or dy!=0)]
    count = 0
    for y, x in grid:
        for dy,dx in deltas:
            candidate = "".join(grid.get((y+dy*i, x+dx*i),"") for i in range(len(word)))
            count += candidate == word
    return count

def count_x_shapes(s):
    H, W = len(s), len(s[0])-1
    grid = {(y,x):s[y][x] for y in range(H) for x in range(W)}
    count = 0
    for y, x in grid:
        if grid[y,x]=="A":
            lr = grid.get((y-1,x-1),"")+grid.get((y+1,x+1),"")
            rl = grid.get((y-1,x+1),"")+grid.get((y+1,x-1),"")
            count += {lr, rl} <= {"MS", "SM"}

    return count


def main():
    with open("input/day4.txt") as f:
        input = f.readlines()
        print(count_word_instances(input, "XMAS"))
        print(count_x_shapes(input))

if __name__ == '__main__':
    main()