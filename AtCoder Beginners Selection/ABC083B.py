
n, a, b = map(int, input().split())

# n=20
# a=2
# b=5

nums = []
total = 0

# 1-nの数字リストを作る
for i in range(n):
  nums.append(i+1)

# 桁を分解して、各桁を足す。
for i in range(1, n+1):
  
  # 桁をばらしたリストを作る
  digits = [int(x) for x in str(i)]

  # ばらしたのを足す
  digit_sum = 0
  for digit in digits:
    digit_sum += digit
  
  if a <= digit_sum <= b:
    total += i


print(total)
