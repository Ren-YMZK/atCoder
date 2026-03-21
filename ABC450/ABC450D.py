N, K = map(int, input().split())
A = list(map(int, input().split()))

# まず全部 K で割った余りにする
for i in range(N):
  A[i] = A[i] % K

# 小さい順に並べる
A.sort()

# いちばん大きいすき間を探す
big = 0

# となり同士の差を見る
for i in range(N - 1):
  gap = A[i + 1] - A[i]

  if gap > big:
    big = gap

# 最後と最初の間のすき間も見る
gap = A[0] + K - A[N - 1]
if gap > big:
  big = gap

# 答えは K - いちばん大きいすき間
print(K - big)