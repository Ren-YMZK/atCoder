N, M = map(int, input().split())

if N > M:
  for i in range(N):
    if i <= M-1:
      print("OK")
    else:
      print("Too Many Requests")
else:
  for i in range(N):
    print("OK")