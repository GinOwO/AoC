from collections import defaultdict as dd

def helper(s):
    s = s.split(':')[1]
    a, b = s.split('|')
    a = set(a.split())
    b = set(b.split())
    return a, b

def solve1(s):
    a, b = helper(s)
    if(len(a&b)):return 1<<(len(a&b)-1)
    return 0

ddict = dd(lambda:1)
k = 1

def solve2(s):
    global k
    a, b = helper(s)
    for i in range(len(a&b)):
        ddict[k+i+1]+=ddict[k]
    k+=1
    

ans = 0
q=0
while 1:
    try:
        s = input()
        if (not s): break
    except: break
    #ans+=solve1(s)
    solve2(s)
    q+=1
    
#print(ans)
print(sum((ddict[i] for i in range(1, q+1)))) # 2nd part