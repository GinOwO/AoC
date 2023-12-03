import re

R = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))")

def helper(s: str):
    if(s == 'one'): return 1
    if(s == 'two'): return 2
    if(s == 'three'): return 3
    if(s == 'four'): return 4
    if(s == 'five'): return 5
    if(s == 'six'): return 6
    if(s == 'seven'): return 7
    if(s == 'eight'): return 8
    if(s == 'nine'): return 9
    return int(s)

ans = 0
while 1:
    try:
        s = input()
    except: break
    arr = R.findall(s)
    ans += helper(arr[0])*10 + helper(arr[-1])
print(ans)