n = int(input())
a = list(map(int, input().split()))

bob_sum = 0
alice_sum = 0

for i in range(n):
  item = 0
  
  if i%2 == 0:
    alice_sum += max(a)
    item = max(a)
    
  else:
    bob_sum += max(a)
    item = max(a)

  a.remove(item)
    
result = alice_sum - bob_sum

print(result)