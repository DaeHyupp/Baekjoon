from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input())
que = PriorityQueue()
for _ in range(N):
    que.put(int(input()))

def solve():
    ans = 0
    if N ==1 :
        print(0)
        return
    while 1:
        a =que.get()
        b =que.get()
        if que.empty():
            ans += a+b
            print(ans)
            return
        else:
            que.put(a+b)
            ans += a+b

solve()

