S_list = list(map(str, input()))

upper_list = []

for s in S_list:
  if s.isupper():
    upper_list.append(s)

result = ''.join(upper_list)

print(result)