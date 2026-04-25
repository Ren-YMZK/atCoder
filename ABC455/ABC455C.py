N, K = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
cnt = {}

for x in A:
  if x in cnt:
    cnt[x] += 1
  else:
    cnt[x] = 1
#print(cnt)

decrease = []

for x in cnt:
  decrease.append(x * cnt[x])

decrease.sort(reverse=True)
#print(decrease)

if K < len(decrease):
  loop = K
else:
  loop = len(decrease)

for i in range(loop):
  total = total - decrease[i]

print(total)