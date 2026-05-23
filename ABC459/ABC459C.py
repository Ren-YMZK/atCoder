N, Q = map(int, input().split())

blocks = [0] * (N + 1)
results = []
offset = 0

for _ in range(Q):
  query = input().split()
  t = int(query[0])
  v = int(query[1])

  if t == 1:
    blocks[v] += 1

    all_have_block = True
    for i in range(1, N + 1):
      if blocks[i] - offset == 0:
        all_have_block = False
        break

    if all_have_block == True:
      offset += 1

  else:
    count = 0
    for i in range(1, N + 1):
      if blocks[i] - offset >= v:
        count += 1
    results.append(count)

for r in results:
  print(r)