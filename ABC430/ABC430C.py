
N, A, B = map(int, input().split())
S = input().strip()

# 累積和 pa[i]: 先頭から i 文字目までの 'a' の個数
# 累積和 pb[i]: 先頭から i 文字目までの 'b' の個数
pa = [0] * (N + 1)
pb = [0] * (N + 1)
for i, ch in enumerate(S):
    pa[i + 1] = pa[i] + (1 if ch == "a" else 0)
    pb[i + 1] = pb[i] + (1 if ch == "b" else 0)

ans = 0

# jA: a >= A となる最小の j
# rB: b <  B を満たす最大の j
jA = 1
rB = 0

for i in range(N):
    # j は少なくとも i+1 から始まるので、jA もそれより左にはならないよう調整
    if jA < i + 1:
        jA = i + 1

    # 条件1: a >= A となる最小の jA を見つける
    while jA <= N and pa[jA] - pa[i] < A:
        jA += 1

    # 条件2: b < B を満たす最大の rB を伸ばしていく
    while rB + 1 <= N and pb[rB + 1] - pb[i] < B:
        rB += 1

    # この i について有効な j の範囲は [start, end]
    start = max(jA, i + 1)
    end = rB

    if start <= end:
        ans += end - start + 1

print(ans)

