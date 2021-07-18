import sys
input = sys.stdin.readline

N = int(input())
local = list(map(int,list(input().rstrip().split(" "))))
bud = int(input())
local.sort()

start = 1
end = local[-1]


def bs(start,end):
    while start <= end:
        cnt =0
        mid = (start+end)//2
        if mid == start:
            for i in local:
                if i<=start+1:
                    cnt += i
                else: cnt +=start+1
            if cnt>bud: break
            else:
                mid = start +1
                break
            
        for i in local:
            if i<=mid:
                cnt += i
            else: cnt +=mid

        if cnt==bud:break
        elif cnt > bud : end=mid-1
        else: start=mid
    return mid
print(bs(start,end))
    

