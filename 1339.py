import sys
input = sys.stdin.readline

N = int(input().rstrip())
words = [list(input().rstrip()) for _ in range(N)]
numbers = [[0] for _ in range(N)]
check = [0]* 30
cnt = [0]* 30
num = 9
for length in range(8,0,-1):
    for i in words:
        if length <= len(i):
            cnt[ord(i[len(i)-length])-65] +=10**(length-1)
print(cnt)
while max(cnt) != 0:
    check[cnt.index(max(cnt))] = num
    cnt[cnt.index(max(cnt))] = 0
    num -= 1
    if num == 0: break


for i in range(N):
    for j in range(len(words[i])):
        if words[i][j] != int:
            words[i][j] = str(check[ord(words[i][j])-65])

ans = 0
for i in range(N):
    temp = ""
    temp = "".join(j for j in words[i])
    ans += int(temp)
print(ans)

