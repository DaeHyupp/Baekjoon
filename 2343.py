import sys
input = sys.stdin.readline


N, M = map(int, input().rstrip().split(" "))
lesson = list(map(int,list(input().rstrip().split(" "))))

min_blue = max(lesson)
max_blue = sum(lesson)

while min_blue <=max_blue:
    mid = (min_blue+max_blue)//2
    add=0
    cnt=0
    for i in range(N):
        if add+lesson[i]<=mid:
            add += lesson[i]
        else:
            add = lesson[i]
            cnt += 1
    cnt +=1
    if cnt <=M:
        ans = mid
        max_blue = mid-1
    else: min_blue = mid+1
print(ans)



