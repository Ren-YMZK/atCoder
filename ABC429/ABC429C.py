N = int(input())
A = list(map(int, input().split()))

# N = 5
# A = [3, 2, 5, 2, 2]

# Ai は 1..N なので N+1 にして、0番目は使わない。
freq = [0] * (N + 1)

for x in A:
  freq[x] += 1

# freq = [0, 0, 3, 1, 0, 1]
#         ↑  ↑  ↑  ↑  ↑
#        値1 値2 値3 値4 値5 の回数

ans = 0

for c in freq:
    if c >= 2:
        ans += c * (c - 1) // 2 * (N - c)

print(ans)