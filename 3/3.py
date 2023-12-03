import re
from itertools import combinations as comb
from collections import defaultdict
from functools import reduce

R1 = re.compile(r"(\d+)")
R2 = re.compile(r"([^\d\.])")

def solve1(s, q=0):
    ans = 0
    for j in range(len(s)):
        for i in R1.finditer(s[j]):
            x, y = i.span(1)
            p = int(i.group(1))
            if y<q and R2.findall(s[j][y]): ans+=p
            elif x-1>=0 and R2.findall(s[j][x-1]): ans+=p
            elif j-1>=0 and R2.findall(s[j-1][x-(x>0):y+1]): ans+=p
            elif j+1<len(s) and R2.findall(s[j+1][x-(x>0):y+1]): ans+=p
    return ans

def solve2(s, q=0):
    tmp = defaultdict(list)
    for j in range(len(s)):
        for i in R1.finditer(s[j]):
            x, y = i.span(1)
            p = int(i.group(1))
            if y<q and s[j][y]=='*': tmp[(j, y)].append(p)
            if x-1>=0 and s[j][x-1]=='*': tmp[(j, x-1)].append(p)
            if j-1>=0 and s[j-1][x-(x>0):y+1].find('*')!=-1: tmp[(j-1, x-(x>0)+s[j-1][x-(x>0):y+1].find('*'))].append(p)
            if j+1<len(s) and s[j+1][x-(x>0):y+1].find('*')!=-1: tmp[(j+1, x-(x>0)+s[j+1][x-(x>0):y+1].find('*'))].append(p)
    
    return sum(reduce(lambda p,x:p+x[0]*x[1], comb(v,2), 0) for v in tmp.values())

arr = []

while 1:
    try: 
        s = input()
        if not s: break
    except: break
    arr.append(s)

print(solve2(arr, len(arr[0])))

