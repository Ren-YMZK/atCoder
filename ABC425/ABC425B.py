N = int(input())
A_list = list(map(int, input().split()))

used = set()

for a in A_list:
  if a == -1:
    continue
  if a in used:
    print("No")
    exit()
  used.add(a)

remain = []

for x in range(1, N + 1):
    if x not in used:
        remain.append(x)

idx = 0

P = []
for a in A_list:
    if a == -1:
        P.append(remain[idx])
        idx += 1
    else:
        P.append(a)

print("Yes")
print(*P)