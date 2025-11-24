N, L, R = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]

count = 0

for i, j in XY:
  if i <= L and R <= j:
    count += 1

print(count)