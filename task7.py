import sys
sys.setrecursionlimit(2000)

def build_postorder(in_order, pre_order):
    n = len(in_order)
    in_index_map = {val: idx for idx, val in enumerate(in_order)}

    def helper(in_left, in_right, pre_left, pre_right):
        if in_left > in_right or pre_left > pre_right:
            return []

        root_val = pre_order[pre_left]
        root_index = in_index_map[root_val]
        left_size = root_index - in_left

        left_postorder = helper(in_left, root_index - 1, pre_left + 1, pre_left + left_size)
        right_postorder = helper(root_index + 1, in_right, pre_left + left_size + 1, pre_right)

        return left_postorder + right_postorder + [root_val]

    return helper(0, n - 1, 0, n - 1)


n = int(input())
in_order = list(map(int, input().split()))
pre_order = list(map(int, input().split()))


post_order = build_postorder(in_order, pre_order)
print(" ".join(map(str, post_order)))
