n, y = map(int, input().split())
OK = False

for i in range(n+1):
  for j in range(n-i+1):
    k = n - (i + j)
    money_sum = 10000 * i + 5000 * j + 1000 * k
    if money_sum == y:
      ichiman = i
      gosen = j
      sen = k
      
      OK = True

if OK == True:
  print(ichiman, gosen, sen)
else:
  print(-1, -1, -1)