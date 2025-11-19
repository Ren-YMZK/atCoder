n = int(input())

plans = []

for _ in range(n):
  t, x, y = map(int, input().split())
  plans.append((t, x, y))

# こっちでも可
# plans = [list(map(int, input().split())) for _ in range(n)]
  
print(plans)

t_prev, x_prev, y_prev = 0, 0, 0
OK = True

for i in range(n):
  
  t, x, y = plans[i]
  
  dt = t - t_prev
  distance = abs(x - x_prev) + abs(y - y_prev)
  over = dt - distance

  if distance > dt or over % 2 != 0:
    OK = False
    break
  
  t_prev, x_prev, y_prev = t, x, y

if OK:
  print("Yes")
else:
  print("No")