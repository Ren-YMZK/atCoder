N = int(input())
C = [[0] * N for _ in range(N)]

for i in range(N - 1):
    row = list(map(int, input().split()))

    for j in range(len(row)):
        C[i][i + 1 + j] = row[j]

isOk = False

for a in range(N):
    for b in range(a + 1, N):
        for c in range(b + 1, N):
          if C[a][c] > C[a][b] + C[b][c]:
                isOk = True

if isOk == True:
  print("Yes")
else:
  print("No")