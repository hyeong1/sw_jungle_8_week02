import sys

N = int(input())
circles = []
for _ in range(N):
    center, radius = map(int, sys.stdin.readline().split())
    left = ["L", center - radius]
    right = ["R", center + radius]
    circles.append(left)
    circles.append(right)
circles.sort(key=lambda x: x[0], reverse=True)  # R이 L보다 먼저 오도록 정렬
circles.sort(key=lambda x: x[1])

answer = 1  # 밖 영역
stack = []
for c in circles:
    if c[0] == "L":
        stack.append(c)
        continue

    total_width = 0  # 현재 원 안에 원이 있으면, 그 원들의 너비를 전부 더해서 담을 변수 -> 이 변수와 감싸고 있는 원의 너비가 같으면(중첩 원) answer+2
    while stack:
        prev = stack.pop()
        if prev[0] == "L":  # 꺼낸게 "L"이면 원 생성
            width = c[1] - prev[1]
            if total_width == width:
                answer += 2
            else:  # 중첩 원 없는 경우
                answer += 1
            stack.append(["C", width])
            break
        elif prev[0] == "C":  # 꺼낸게 완성된 원이면
            total_width += prev[1]

print(answer)

# 원 범위 L ~ R -> L: "(", R: ")"로 치환
# [L or R, 좌표]
# ) 다음 바로 ( 나오면 합쳐서 +1
# 1 실패
# while circles:
#     current = circles.pop()
#     if current[0] == "L":
#         if circles and circles[-1][0] == "R":
#             answer += 1
#             circles.pop()
#         else:
#             answer += 1
#     elif current[0] == "R":
#         if circles and circles[-1][0] == "L":
#             answer += 1
#             circles.pop()
#         else:
#             answer += 1
