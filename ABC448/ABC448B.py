N, M = map(int, input().split())
C_list = list(map(int, input().split()))
AB_list = [list(map(int, input().split())) for _ in range(N)]

need = [0] * M

for a, b in AB_list:
  need[a-1] += b

S = 0
for i in range(M):
  S += min(C_list[i], need[i])

print(S)