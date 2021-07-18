import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().rstrip().split(" ")))
lis = []
lis.append(10**9)

def bs(start,end,target):
    if target < lis[0]:
        lis[0]=target
        return
    if target > lis[end]:
        lis.append(target)
        return
    
    while start<= end:
        mid = (start+end)//2
        if mid == start:
            if lis[mid] !=target:
                lis[start+1] = target
                return
        if lis[mid] == target : return
        elif lis[mid] <target: start = mid
        else: end = mid
    
    return

for i in arr:
    bs(0,len(lis)-1,i)
    print(lis)
print(len(lis))

