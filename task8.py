import sys
sys.setrecursionlimit(2000)

def build_preorder(in_order, post_order):
    n = len(in_order)
    in_index_map = {val: idx for idx, val in enumerate(in_order)}

    def helper(in_left, in_right, post_left, post_right):
        if in_left > in_right or post_left > post_right:
            return []

        root_val = post_order[post_right]
        root_index = in_index_map[root_val]

        left_size = root_index - in_left

        left_preorder = helper(in_left, root_index - 1, post_left, post_left + left_size - 1)
        right_preorder = helper(root_index + 1, in_right, post_left + left_size, post_right - 1)

        return [root_val] + left_preorder + right_preorder

    return helper(0, n - 1, 0, n - 1)


n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))


pre_order = build_preorder(in_order, post_order)
print(" ".join(map(str, pre_order)))
