R, X = map(int, input().split())

in_r = 0
max_r = 0

if X == 1:
  min_r = 1600
  max_r = 2999
else:
  min_r = 1200
  max_r = 2399
  
if min_r <= R <= max_r:
  print("Yes")
else:
  print("No")