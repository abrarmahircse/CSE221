N = int(input())
A = list(map(int, input().split()))
result = []
def build_order(arr, l, r, result):
    if l > r:
        return
    mid = (l + r) // 2
    result.append(arr[mid])
    build_order(arr, l, mid - 1, result) 
    build_order(arr, mid + 1, r, result)  
    


build_order(A, 0, N - 1, result)
print(' '.join(map(str, result)))



"""Find an order to insert the elements such that the height of the resulting BST is minimized.
The input array is sorted, but you don't have to insert in that order.

You want to rearrange the insertion order so that the tree is as balanced as possible (which leads to minimum height).

If there are multiple valid orders that result in the minimum height, any one of them is acceptable.

Why is this challenging?
If you insert the sorted array in the given order, the BST will be skewed (like a linked list), leading to maximum height (worst case).

To minimize height, you want the BST to be balanced: the root is the middle element, the left subtree built from left half, the right subtree from the right half.

So the problem boils down to finding an insertion order that corresponds to a balanced BST.

5
1 2 3 4 5
Output (one possible):

Copy
Edit
3 1 2 4 5
Inserting 3 first makes it the root.

Then insert left half [1, 2] and right half [4, 5].

This order keeps the BST balanced and minimizes height.


"""