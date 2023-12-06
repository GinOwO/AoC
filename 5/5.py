import multiprocessing

def ub(arr, x):
    l, r = 0, len(arr)-1
    while l<=r:
        m = l+r>>1
        if(arr[m][1]<=x): l=m+1
        else: r = m-1
    return r

def shelp(seeds, arr):
    for i in range(len(seeds)):
        idx = ub(arr, seeds[i])
        if(idx == -1 or arr[idx][1]+arr[idx][2]<seeds[i]): continue
        seeds[i] +=arr[idx][0]-arr[idx][1]

def solve1(seeds, arr):
    for i in arr: shelp(seeds, i)
    return min(seeds)

def solve2(seeds, arr):
    mn = 1e100
    for i in range(0,len(seeds),2):
        mn = min(mn, solve1(list(range(seeds[i], seeds[i]+seeds[i+1])), arr))
    return mn

def worker(args):
    seeds, arr, q = args
    mn = 1e100
    for i in range(seeds[0], seeds[0] + seeds[1]):
        mn = min(solve1([i], arr), mn)
    print(f"{q} is done with {mn}")
    return mn

def solve2Parallel(seeds, arr):
    with multiprocessing.Pool() as pool:
        args_list = [(seeds[i:i + 2], arr, i) for i in range(0, len(seeds), 2)]
        results = pool.map(worker, args_list)
        
    return min(results)
    
arr = []
L = []
seeds = [int(i) for i in input().split()[1:]]

while 1:
    try:
        s = input()
        if(not s): continue
        if(s[0].isalpha()):
            if(L):
                L.sort(key = lambda x:x[1])
                arr.append(L)
                L = []
            else: continue
        else:
            L.append([int(i) for i in s.split()])
    except:
        L.sort(key = lambda x:x[1])
        arr.append(L)
        break

#print(solve1(seeds, arr))
print(solve2Parallel(seeds, arr)) # 2008785 - Fuck this im not running it again

"""
Running all tests in /home/gin/Desktop/AOC/5
----------------------------------------------------------------------
Running 5.py
-----------------------------------
Test 1: input.txt
0 is done with 4283162641
8 is done with 3191770485
16 is done with 749391108
2 is done with 780711947
14 is done with 332248829
18 is done with 412475023
6 is done with 13286162
10 is done with 295741384
4 is done with 194991402
12 is done with 2008785
2008785

real    54m23.668s
user    228m51.690s
sys     0m6.388s
-----------------------------------
----------------------------------------------------------------------
"""