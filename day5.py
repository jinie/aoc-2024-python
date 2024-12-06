rules, pages = open('input/day5.txt').read().split('\n\n')

a = [0, 0]
for page in pages.split():
    page = page.split(',')
    s = sorted(page, key=lambda x: -sum(x+'|'+y in rules for y in page))
    a[page!=s] += int(s[len(s)//2])

print(*a)