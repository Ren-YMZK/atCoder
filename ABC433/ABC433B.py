N = int(input())
A_list = list(map(int, input().split()))

for i in range(N):
  ans = -1
  
  for j in range(i):
    if A_list[j] > A_list[i]:
      ans = j + 1

  print(ans)