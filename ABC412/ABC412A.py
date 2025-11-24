N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

count = 0

for i, j in AB:
  if i < j:
    count += 1

print(count)