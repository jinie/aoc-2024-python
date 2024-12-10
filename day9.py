#!/usr/bin/env python3

def parse_input(filename):
    with open(filename) as f:
        fs, files_p1, files_p2, free_space_p1, free_space_p2 = [], [], [], [], []
        for j,l in enumerate([int(x) for x in list(f.readline().strip())]):
            ix = j//2 if j%2 == 0 else -1
            if(ix >= 0):
                files_p1.extend(i for i in range(len(fs), len(fs) + l))             
                files_p2.append((len(fs), l))
            else:
                free_space_p1.extend(i for i in range(len(fs), len(fs) + l))
                free_space_p2.append((len(fs), l))
            fs.extend([ix] * l)
        return fs, files_p1, free_space_p1, files_p2, free_space_p2

def part1(fs, files, free_space):
    while free_space[0] <= files[-1]:
        i, j = files[-1], free_space[0]
        fs[i], fs[j] = fs[j], fs[i]
        del files[-1]
        del free_space[0]
    return sum([i * n for i, n in enumerate(fs) if n >= 0])
    
def part2(fs, files, free_space):
    for file, file_len in files[::-1]:
        for i, (free, free_len) in enumerate(free_space):
            if file_len <= free_len and file > free:
                for j in range(file_len):
                    fs[free + j], fs[file + j] = (
                        fs[file + j],
                        fs[free + j],
                    )
                free_space[i] = (free + file_len, free_len - file_len)
                break
    return sum([i * n for i, n in enumerate(fs) if n >= 0])

def main():
    fs, files_p1, free_space_p1, files_p2, free_space_p2 = parse_input('input/day9.txt')
    print(f"Part 1: {part1(fs[::],files_p1,free_space_p1)}")
    print(f"Part 2: {part2(fs[::],files_p2,free_space_p2)}")

if __name__ == "__main__":
    main()