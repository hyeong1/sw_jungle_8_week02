import sys


def get_area(low, high):
    if low == high:
        return histogram[low]
    mid = (low + high) // 2
    left_max = get_area(low, mid)
    right_max = get_area(mid+1, high)
    return max(left_max, right_max, get_mid_area(low, high, mid))


def get_mid_area(low, high, mid):
    to_left, to_right = mid, mid
    height = histogram[mid]
    max_area = height
    while to_left > low or to_right < high:
        if to_left > low and (to_right == high or histogram[to_left - 1] > histogram[to_right + 1]):
            to_left -= 1
            height = min(height, histogram[to_left])
        elif to_right < high and (to_left == low or histogram[to_left - 1] <= histogram[to_right + 1]):
            to_right += 1
            height = min(height, histogram[to_right])
        max_area = max(max_area, height * (to_right - to_left + 1))

    return max(max_area, height * (to_right - to_left + 1))


while True:
    histogram = list(map(int, sys.stdin.readline().split()))
    n = histogram[0]
    histogram = histogram[1:]
    if n == 0:
        break
    print(get_area(0, len(histogram)-1))

