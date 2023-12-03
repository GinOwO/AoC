import re

R1 = re.compile(r"Game (\d+)")
R2 = re.compile(r"(?:(\d+) (\w+))+|(;)")

def solve1(s):
    for j in R2.findall(s):
        if j[2] == ';': continue
        if int(j[0])>[12,13,14][{'blue':2, 'red':0, 'green':1}[j[1]]]: return 0
    return int(R1.findall(s)[0])

def solve2(s):
    t = [1]*3
    for j in R2.findall(s):
        if j[2] == ';': continue
        k = {'blue':2, 'red':0, 'green':1}[j[1]]
        t[k] = max(t[k], int(j[0]))
    return t[0]*t[1]*t[2]

ans = 0
while 1:
    try: 
        s = input()
        if not s: break
    except: break
    ans += solve1(s)

print(ans)