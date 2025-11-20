N = int(input())
A_list = list(map(int, input().split()))

result = 0

for n in range(1, N+1):
  if n % 2 == 1:
    result += A_list[n-1]

print(result)