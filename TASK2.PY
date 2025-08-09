def merge_and_count(arr, left, mid, right):
    left_sub = arr[left:mid+1]
    right_sub = arr[mid+1:right+1]
    i = j = 0
    k = left
    inv_count = 0
    while i < len(left_sub) and j < len(right_sub):
        if left_sub[i] <= right_sub[j] ** 2:
            arr[k] = left_sub[i]
            i += 1
        else:
            arr[k] = right_sub[j]
            j += 1
            inv_count += (len(left_sub) - i)
        k += 1
    while i < len(left_sub):
        arr[k] = left_sub[i]
        i += 1
        k += 1
    while j < len(right_sub):
        arr[k] = right_sub[j]
        j += 1
        k += 1
    return inv_count

def merge_sort_and_count(arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort_and_count(arr, left, mid)
        inv_count += merge_sort_and_count(arr, mid+1, right)
        inv_count += merge_and_count(arr, left, mid, right)
    return inv_count

n = int(input())
A = list(map(int, input().split()))
print(merge_sort_and_count(A, 0, n-1))
