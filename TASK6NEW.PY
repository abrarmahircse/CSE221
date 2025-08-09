import sys # NOT WORKING    
sys.setrecursionlimit(1 << 20)

def solve(l, r):
    if l > r:
        return []
    mid = (l + r) // 2
    return [A[mid]] + solve(l, mid - 1) + solve(mid + 1, r)

n = int(input())
A = list(map(int, input().split()))
result = solve(0, n - 1)
print(*result)
