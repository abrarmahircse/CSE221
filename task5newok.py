import sys
input = sys.stdin.read


def mod_pow(a, b, m):
    result = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result


def sum_powers(a, n, m):
    if n == 1:
        return a % m
    if n % 2 == 0:
        half = sum_powers(a, n // 2, m)
        return (half + (mod_pow(a, n // 2, m) * half) % m) % m
    else:
        return (sum_powers(a, n - 1, m) + mod_pow(a, n, m)) % m


data = input().split()
T = int(data[0])
index = 1
results = []

for _ in range(T):
    a = int(data[index])
    n = int(data[index + 1])
    m = int(data[index + 2])
    index += 3
    res = sum_powers(a, n, m)
    results.append(res)

print("\n".join(map(str, results)))
