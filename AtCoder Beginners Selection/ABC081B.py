n = int(input())
a= list(map(int, input().split()))

# n = 3
# a = [8,12,40]

count= 0
allEven = True


while allEven:
  # print(a)
  b = []
  for i in range(n):
    a_int= a[i]
    
    if a_int % 2 != 0:
      allEven = False
      break
    else:
      b.append(a_int // 2)
  if allEven == False:
    break
  count += 1
  a = b


print(count)