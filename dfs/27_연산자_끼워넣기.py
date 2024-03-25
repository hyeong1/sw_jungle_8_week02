import sys

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
sum_v, sub_v, mul_v, div_v = map(int, input().split())
max_value, min_value = float("-inf"), float("inf")


def dfs(num_idx, pre_result):
    global max_value, min_value, sum_v, sub_v, mul_v, div_v

    if num_idx == N:
        max_value = max(pre_result, max_value)
        min_value = min(pre_result, min_value)
    else:
        if sum_v > 0:
            sum_v -= 1
            dfs(num_idx + 1, pre_result + nums[num_idx])
            sum_v += 1
        if sub_v > 0:
            sub_v -= 1
            dfs(num_idx + 1, pre_result - nums[num_idx])
            sub_v += 1
        if mul_v > 0:
            mul_v -= 1
            dfs(num_idx + 1, pre_result * nums[num_idx])
            mul_v += 1
        if div_v > 0:
            div_v -= 1
            dfs(num_idx + 1, int(pre_result / nums[num_idx]))
            div_v += 1


dfs(1, nums[0])
print(max_value)
print(min_value)
