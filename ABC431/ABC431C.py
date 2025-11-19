import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))

H.sort(reverse=True)
B.sort(reverse=True)

count, i, j = 0, 0, 0

while i < N and j < M and count < K:
  if H[i] <= B[j]:
    count += 1
    i += 1
    j += 1
    
  else:
    i += 1
    
if count >= K:
  print("Yes")
else:
  print("No")
    







# 以下失敗作。時間オーバー。

# N, M, K = map(int, input().split())
# H = list(map(int, input().split()))
# B = list(map(int, input().split()))

# count = 0

# if N < M:
#   minimum = N
# else:
#   minimum = M

# for i in range(minimum):
#   max_h = max(H)
#   max_b = max(B)
  
#   if max_h <= max_b:
#     H.remove(max_h)
#     B.remove(max_b)
#     count += 1
    
#   else:
#     H.remove(max_h)
    
#   if count >= K:
#     break
  
# if count >= K:
#   print("Yes")
# else:
#   print("No")