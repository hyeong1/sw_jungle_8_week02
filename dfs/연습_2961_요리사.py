N = int(input())
ingredients = []
answer = float("inf")
for _ in range(N):
    ingredients.append(list(map(int, input().split())))


def dfs(idx, s, b, used):
    global answer

    if idx == N:
        if used == 0:
            return
        answer = min(abs(s - b), answer)
        return

    dfs(idx+1, s*ingredients[idx][0], b+ingredients[idx][1], used+1)  # 현재 재료 선택
    dfs(idx+1, s, b, used)  # 현재 재료를 선택하지 않은 경우


dfs(0, 1, 0, 0)
print(answer)
