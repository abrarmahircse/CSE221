T = int(input())
MOD = 10**9 + 7

def mat_mult(A, B):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
         (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
         (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    ]

def mat_ad(matrix, pwr):
    result = [[1, 0], [0, 1]]  # identity mat taken
    while pwr > 0:
        if pwr % 2 == 1:
            result = mat_mult(result, matrix)
        matrix = mat_mult(matrix, matrix)
        pwr //= 2
    return result



for _ in range(T):
    a11, a12, a21, a22 = map(int, input().split())
    A = [[a11, a12], [a21, a22]]
    X = int(input())
    result = mat_ad(A, X)
    print(f"{result[0][0]} {result[0][1]}")
    print(f"{result[1][0]} {result[1][1]}")

