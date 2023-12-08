from collections import Counter

ranks = dict(zip("AKQJT98765432", range(13,-1,-1)))

def weight(s: str, sec: bool = False):
    k, x, p, ranks['J'] = Counter(s), 0, 0, 10*(1-sec)
    if(sec):
        p = k['J']
        del k['J']
    if  (len(k)<=1): x=10
    elif(len(k)==2): x=8+(max(k.values())+p==4)
    elif(len(k)==3): x=6+(max(k.values())+p==3)
    elif(len(k)==4): x=4
    return x, [ranks.get(i, -1) for i in s]

def solve1(arr: list[tuple[str, int]], sec: bool = False):
    return sum(i*j[1] for i, j in enumerate(sorted(arr, key = lambda x: weight(x[0], sec)), start=1))

solve2 = lambda arr: solve1(arr, True)

""" 
# OOOOOOOR
from collections import Counter as C
r = dict(zip("AKQJT98765432", range(13,-1,-1)))
w=lambda s,q:((10,10,8+(max(C(s.replace('J','')).values()or[0])+C(s)['J']==4),6+(max(C(s.replace('J','')).values()or[0])+C(s)['J']==3),4,0)[len(C(s.replace('J','')))],[(r[i],10*(1-q))[i=='J']for i in s])
s1=lambda a,s=0:sum(i*j[1]for i,j in enumerate(sorted(a,key=lambda x:w(x[0],s)),1))
s2=lambda a:s1(a,1)

# Alternate w
def w(s,q):
    k,p,r['J'] = C(s),0,10*(1-q)
    if(q): 
        p=k['J']; del k['J']
        if(p==5): return 10,[0]*5
    return (10,10,8+(max(k.values())+p==4),6+(max(k.values())+p==3),4,0)[len(k)],[r[i] for i in s]
"""


arr = []

while 1:
    try:
        s = input()
        if not s: break
        h, v = s.split()
        arr.append((h, int(v)))
    except: break

# print(solve1(arr))
print(solve2(arr))