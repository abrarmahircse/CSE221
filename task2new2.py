
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    mid = [pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + mid + quicksort(right)


n = int(input())
A = list(map(int, input().split()))


squares = [x ** 2 for x in A]

all_vals = squares + A


unique_vals = list(set(all_vals))


unique_vals = quicksort(unique_vals)


val_to_idx = {}
for idx, val in enumerate(unique_vals):
    val_to_idx[val] = idx + 1  


class BIT:
    def __init__(self, size):
        self.N = size + 2
        self.tree = [0] * (self.N)

    def update(self, idx, val):
        while idx < self.N:
            self.tree[idx] += val
            idx += idx & -idx

    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res


bit = BIT(len(unique_vals))
ans = 0

for i in reversed(range(n)):
    x = A[i]
    idx = val_to_idx[x] - 1  
    ans += bit.query(idx)

    sq_idx = val_to_idx[x ** 2]
    bit.update(sq_idx, 1)

print(ans)
