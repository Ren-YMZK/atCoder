N = int(input())
S_list = [input() for _ in range(N)]

lengths = []
for s in S_list:
  lengths.append(len(s))

max = max(lengths)

for s in S_list:
  n = (max - len(s)) // 2
  print("." * n + s + "." * n)