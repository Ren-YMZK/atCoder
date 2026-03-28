Q = int(input())

trees = []

for _ in range(Q):
  t, h = map(int, input().split())

  if t == 1:
    trees.append(h)
  else:
    new_trees = []
    for i in trees:
      if i > h:
        new_trees.append(i)
    trees = new_trees

  print(len(trees))