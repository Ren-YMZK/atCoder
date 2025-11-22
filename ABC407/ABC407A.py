A, B = map(int, input().split())

q, r = divmod(A, B)

if 2 * r < B:
  print(q)
else:
  print(q + 1)