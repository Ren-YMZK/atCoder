T = int(input())

for _ in range(T):
  X1, Y1, R1, X2, Y2, R2 = map(int, input().split())
  d2 = (X1-X2)**2 + (Y1-Y2)**2
  lower = (R1-R2)**2
  upper = (R1+R2)**2

  if lower <= d2 <= upper:
    print("Yes")
  else:
    print("No")