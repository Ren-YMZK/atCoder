N, M = map(int, input().split())

used = set()
ans = []

for _ in range(N):
  L = int(input())
  X_list = list(map(int, input().split()))

  select = 0

  for i in X_list:
    if i not in used:
      select = i
      used.add(i)
      break

  ans.append(select)

for x in ans:
  print(x)