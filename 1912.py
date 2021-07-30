import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ans = []
ans.append(arr[0])
for i in range(len(arr) - 1):
    ans.append(max(ans[i] + arr[i + 1], arr[i + 1]))
print(max(ans))
        
            

