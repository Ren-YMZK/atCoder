N = int(input())
T_list = list(input())
A_list = list(input())

judge = False

for i in range(N):
  if T_list[i] == "o" and A_list[i] == "o":
    judge = True

if judge == True:
  print("Yes")
else:
  print("No")