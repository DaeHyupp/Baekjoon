N = int(input())
li = list(int(input()) for _ in range(N))
li.sort()
ans = 0
for i in range(N, 0,-1):
    ans = max(ans, li.pop(0)*i)
print(ans)


# it can took less time with checking arrays not sorting
# ropes = [0] * 10001
# num_ropes = int(input())
# for _ in range(num_ropes):
#   ropes[int(input())] += 1
#
# ans = 0
# cnt = 0
# for i in range(1, 10001):
#   if ropes[i] !=0:
#       tmp = i * (num_ropes - cnt)
#       ans = max(ans,tmp)
#       cnt += ropes[i]
#       if num_ropes == cnt: break
# print(ans)


# it can be faster with sys.stdin.readline

