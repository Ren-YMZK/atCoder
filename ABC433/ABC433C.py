S = input()
n = len(S)

left = [0] * n

for i in range(n):
  if i == 0:
    left[i] = 1
  else:
    if S[i] == S[i - 1]:
      left[i] = left[i - 1] + 1
    else:
      left[i] = 1
# print(left)
      
right = [0] * n

for i in range(n - 1, -1, -1):
  if i == n - 1:
    right[i] = 1
  else:
    if S[i] == S[i + 1]:
      right[i] = right[i + 1] + 1
    else:
      right[i] = 1
# print(right)

result = 0

for i in range(n - 1):
  x = int(S[i])
  y = int(S[i + 1])
  
  if x + 1 == y:
    l = left[i]
    r = right[i + 1]
    result += min(l, r)
    
print(result)