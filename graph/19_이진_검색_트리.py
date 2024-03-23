import sys
sys.setrecursionlimit(10**9)

nums = []
while True:
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break


def solve(arr):
    if len(arr) == 0:
        return

    mid = arr[0]
    temp_l, temp_r = [], []
    for i in range(1, len(arr)):
        if mid < arr[i]:
            temp_l = arr[1:i]
            temp_r = arr[i:]
            break
    else:  # 모두 mid 보다 작은 경우 (모두 왼쪽 서브 트리)
        temp_l = arr[1:]

    solve(temp_l)
    solve(temp_r)
    print(mid)


solve(nums)
