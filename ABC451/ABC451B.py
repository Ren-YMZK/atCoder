N, M = map(int, input().split())

konki = [0] * M
raiki = [0] * M

for _ in range(N):
  a, b = map(int, input().split())
  konki[a - 1] += 1
  raiki[b - 1] += 1

for i in range(M):
  print(raiki[i] - konki[i])