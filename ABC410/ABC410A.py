N = int(input())
A_list = list(map(int, input().split()))
K = int(input())

count = 0

for i in range(N):
  if A_list[i] >= K:
    count += 1
    
print(count)