H, W, Q =map(int, input().split())

h, w = H, W

for _ in range(Q):
  type, n = map(int, input().split())

  if type == 1:
    print(n * w)
    h -= n
  else:
    print(n * h)
    w -= n