X, Y = map(str, input().split())

if X == "Ocelot":
  X_ver = 1
elif X == "Serval":
  X_ver = 2
else:
  X_ver = 3
  
if Y == "Ocelot":
  Y_ver = 1
elif Y == "Serval":
  Y_ver = 2
else:
  Y_ver = 3
  
if X_ver >= Y_ver:
  print("Yes")
else:
  print("No")