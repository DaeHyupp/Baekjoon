import sys
input = sys.stdin.readline

N = int(input())

positive=[]
negative =[]
cnt =0
for _ in range(N):
    tmp = int(input())
    if tmp > 1: positive.append(tmp)
    elif tmp< 1: negative.append(tmp)
    else: cnt += tmp
positive.sort()
negative.sort()
while positive:
    if len(positive) == 1:
        cnt += positive.pop(-1)
        break
    a = positive.pop(-1)
    b = positive.pop(-1)
    cnt += a*b

while negative:
    if len(negative) == 1:
        cnt += negative.pop(0)
        break
    a = negative.pop(0)
    b = negative.pop(0)
    cnt += a*b
print(cnt)

