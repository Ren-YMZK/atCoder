N, S = map(int, input().split())
T_list = list(map(int, input().split()))

sleep_time = S + 0.5
current_time = 0
getup = True

for i in range(N):
  time = T_list[i] - current_time
  if time > sleep_time:
    getup = False
    break
  else:
    current_time += time

if getup == True:
  print("Yes")
else:
  print("No")