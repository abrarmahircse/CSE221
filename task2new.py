from bisect import bisect_left, insort
n = int(input())
A = list(map(int, input().split()))
squares = []
ans = 0
for i in reversed(range(n)):
    x = A[i]

    pos = bisect_left(squares, x)
    ans += pos
    insort(squares, A[i] ** 2)
print(ans)
