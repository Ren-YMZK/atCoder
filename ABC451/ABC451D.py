N = int(input())

parts = []
x = 1
while x <= 10**9:
  parts.append(str(x))
  x *= 2

good = set()
todo = []

for p in parts:
  num = int(p)
  if num <= 10**9:
    good.add(num)
    todo.append(p)

i = 0
while i < len(todo):
  s = todo[i]
  i += 1

  for p in parts:
    new_s = s + p
    num = int(new_s)

    if num <= 10**9 and num not in good:
      good.add(num)
      todo.append(new_s)

ans = sorted(good)
print(ans[N - 1])