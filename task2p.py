def merge_sort_count(nums, left, right):
    if left >= right:
        return 0
    mid = (left + right) // 2
    count = merge_sort_count(nums, left, mid) + merge_sort_count(nums, mid + 1, right)
    
    # count pairs
    j = mid + 1
    for i in range(left, mid + 1):
        while j <= right and nums[i] > 2 * nums[j]:
            j += 1
        count += j - (mid + 1)
    
    # merge step:
    temp = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
    temp.extend(nums[i:mid + 1])
    temp.extend(nums[j:right + 1])
    nums[left:right + 1] = temp
    return count

n = int(input())
A = list(map(int, input().split()))
print(merge_sort_count(A, 0, n - 1))
