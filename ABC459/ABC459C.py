N, Q = map(int, input().split())

blocks = [0] * (N + 1)

for _ in range(Q):
  query = input().split()
  t = int(query[0])
  v = int(query[1])

  if t == 1:
    blocks[v] += 1

    all_have_block = True
    for i in range(1, N + 1):
      if blocks[i] == 0:
        all_have_block = False
        break

    if all_have_block == True:
      for i in range(1, N + 1):
        blocks[i] -= 1

  else:
    count = 0
    for i in range(1, N + 1):
      if blocks[i] >= v:
        count += 1
    print(count)