import heapq


def heapify(arr, left, right):
    temp = arr[left]

    parent = left
    while parent < (right + 1) // 2:
        cl = parent * 2 + 1
        cr = cl + 1
        child = cr if cr <= right and arr[cr] > arr[cl] else cl
        if temp >= arr[child]:
            break
        arr[parent] = arr[child]
        parent = child
    arr[parent] = temp


nums = [1, 5, 3, 2, 4]
n = len(nums)
for i in range((n-1)//2, -1, -1):
    heapify(nums, i, n-1)
print(nums)

heap = []
for i in range(n):
    heapq.heappush(heap, -(i+1))
for i in range(n):
    print(-heapq.heappop(heap))
