n = int(input())
arr = list(map(int, input().split()))
def merge(a, b):
    merged = []
    i = j = count = 0
    while i < len(a) and j < len(b): # while loop exists
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else: #Since a and b are both already sorted, all remaining elements in a (from i onward) are greater than b[j].
            merged.append(b[j]) #Place b[j] in the merged list — it goes before a[i] because it’s smaller.
            count += len(a) - i  
            j += 1

    merged.extend(a[i:])# leftovers
    merged.extend(b[j:])
    return merged, count

def mergeSort(arr):
    if len(arr) <= 1: # recursive base case 
        return arr, 0
    else:
        mid = len(arr) // 2
        a1, inv1 = mergeSort(arr[:mid]) # inv hoilo inversion koita
        a2, inv2 = mergeSort(arr[mid:])  # a1,a2 sorted here 
        merged, inv_merge = merge(a1, a2)
        total_inv = inv1 + inv2 + inv_merge
        return merged, total_inv

sorted_arr, count = mergeSort(arr)
print(count)
print(*sorted_arr)
