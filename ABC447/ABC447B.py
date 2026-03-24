S = input()

count = {}

for s in S:
  if s in count:
    count[s] += 1
  else:
    count[s] = 1

max_count = 0

for s in count:
  if count[s] > max_count:
    max_count = count[s]

answer = []

for s in S:
  if count[s] != max_count:
    answer.append(s)

print("".join(answer))