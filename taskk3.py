

a, b = map(int, input().split())
def fast_power(a, b, mod):
    result = 1 # sth to the power 0 is 1 
    a = a % mod  
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b //= 2
    return result

print(fast_power(a, b, 107))







a, b = map(int, input().split())
def fast_power(a, b, mod):
    ans = 1
    a %= mod
    while b:
        if b & 1:
            ans = ans * a % mod
        a = a * a % mod
        b >>= 1
    return ans

print(fast_power(a, b, 107))

