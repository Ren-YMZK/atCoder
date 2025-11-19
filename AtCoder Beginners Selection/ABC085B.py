n = int(input())
dList = [int(input()) for i in range(n)]

min_mochi = 0
count = 0

for i in range(n):
  mochi = min(dList)
  
  if min_mochi < mochi:
    min_mochi = mochi
    count += 1
  dList.remove(min_mochi)

print(count)