N, K = map(int, input().split())
S = str(input())

str_list = []

for i in range(N-K+1):
  str_list.append(S[i:i+K])
  
count_dict = {}
for i in str_list:
  if i in count_dict:
    count_dict[i] += 1
  else:
    count_dict[i] = 1

max_str_count = 0

for i in count_dict:
  if count_dict[i] > max_str_count:
    max_str_count = count_dict[i]

results = []
for i in str_list:
  if max_str_count == count_dict[i] and i not in results:
    results.append(i)
    
results.sort()

result = ' '.join(results)

print(max_str_count)
print(result)