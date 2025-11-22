N = int(input())
S_list = [input() for _ in range(N)]
X, Y = map(str, input().split())

if S_list[int(X)-1] == Y:
  print("Yes")
else:
  print("No")