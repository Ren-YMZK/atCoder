N = int(input())
X_list = list(map(int, input().split()))

# (座標, 人番号)
points = [(0, 0)]

for i in range(1, N+1):
  points.append((X_list[i-1], i))

points.sort()

M = N + 1

coordinate_sorted = 

