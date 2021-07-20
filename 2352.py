import sys
input = sys.stdin.readline
while 1:
    N = int(input().rstrip())
    if N== -1: break
    ports = list(map(int,list(input().rstrip().split(" "))))

    lines = []
    lines.append(100000)

    for target in ports:
        if target < lines[0]:
            lines[0] = target
            print(lines)
            continue
        if target > lines[-1] :
            lines.append(target)
            print(lines)
            continue

        start = 0
        end = len(lines)-1

        print(lines)
    
        while start <= end:
            mid = (start + end) //2
            if mid == start:
                if lines[end] > target and lines[start] < target:
                    lines[end] = target
                    break
                else : lines[start] = target
            if lines[mid] == target : break
            elif lines[mid] < target : start = mid
            else: end = mid
    print(lines)
    print(len(lines))

