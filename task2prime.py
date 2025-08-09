N = int(input())
A = list(map(int, input().split()))
def binary_search_right(arr, target):         # target to comparr
   
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left                    #Eventually, left and right meet at the exact spot where all values to the left are ≤ target and all values to the right are > target.

def insert_sorted(arr, value):
   
    index = binary_search_right(arr, value)
    arr.insert(index, value)

def count_pairs(A):
    sorted_list = []
    count = 0
    for num in A:
        square = num * num         # here the logic         
        idx = binary_search_right(sorted_list, square)
        count += len(sorted_list) - idx
        
        insert_sorted(sorted_list, num)
    return count

print(count_pairs(A))



""" #sorted_list = [1, 2, 5, 7, 9]
square = 4
We do idx = binary_search_right(sorted_list, 4) → idx = 2

Because position 2 is where 4 would be inserted:

[1, 2, (4), 5, 7, 9]

Number of elements > 4 is:
len(sorted_list) - idx = 5 - 2 = 3

These elements are [5, 7, 9] """