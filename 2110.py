import sys
input = sys.stdin.readline

N, C = map(int,input().rstrip().split(" "))
house = []
for i in range(N):
    house.append(int(input().rstrip()))

house.sort()

start = 1
end = house[-1] - house[0]

ans = 0
def DS(start,end):
    global ans
    while start <= end:
        mid = (start+end)//2
        point = house[0]
        cnt = 1
        for i in range(1,N):
            if house[i]>=point+mid:
                cnt += 1
                point = house[i]
                
        if cnt >= C:
            start = mid +1
            ans = mid
        else :
            end = mid -1

DS(start,end)
print(ans)

