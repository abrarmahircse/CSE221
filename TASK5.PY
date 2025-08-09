import sys
input = sys.stdin.readline

sys.setrecursionlimit(1 << 25)

def mod_pow(a, b, m):
    res = 1
    a %= m
    while b:
        if b & 1:
            res = res * a % m
        a = a * a % m
        b >>= 1
    return res

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def solve(a, n, m):
    if a == 1:
        return n % m
    num = (mod_pow(a, n + 1, m) - a + m) % m
    den = (a - 1) % m
    inv = modinv(den, m)
    return (num * inv) % m

T = int(input())
for _ in range(T):
    a, n, m = map(int, input().split())
    print(solve(a, n, m))
