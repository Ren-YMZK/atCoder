import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A_list = list(map(int, input().split()))

OK = False

for i in range(N):
  popped_item = A_list.pop(0)
  A_list_sum = sum(A_list)
  if A_list_sum == M:
    OK = True
    break
  else:
    A_list.append(popped_item)

if OK == True:
  print("Yes")
else:
  print("No")