def binary_search_right(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

def insert_sorted(arr, value):
    index = binary_search_right(arr, value)
    arr.insert(index, value)

def count_pairs(A):
    sorted_list = []
    count = 0
    for num in reversed(A):  
        idx = binary_search_right(sorted_list, num)
        count += idx  
        insert_sorted(sorted_list, num * num) 
    return count

N = int(input())
A = list(map(int, input().split()))
print(count_pairs(A))
