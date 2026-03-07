N, X = map(int, input().split())
A_list = list(map(int, input().split()))

for a in A_list:
  if a < X:
    X = a
    print(1)
  else:
    print(0)