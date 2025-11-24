N, M = map(int, input().split())
A_list = list(map(int, input().split()))

sum = 0

for i in A_list:
  sum += i
  
if sum <= M:
  print("Yes")
else:
  print("No")