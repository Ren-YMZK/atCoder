N = int(input())
A_list = list(map(int, input().split()))
X = int(input())

ans = False

for i in range(N):
  if A_list[i] == X:
    ans = True
    break

if ans == True:
  print("Yes")
else:
  print("No")