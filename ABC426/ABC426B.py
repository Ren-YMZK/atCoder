S = input()

for i in S:
  count = 0
  for j in S:
    if i == j:
      count += 1
  if count == 1:
    print(i)