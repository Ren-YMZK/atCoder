N, L, R = map(int, input().split())
S = str(input())

posisions = {}
for i, ch in enumerate(S):
  if ch not in posisions:
    posisions[ch] = []
  posisions[ch].append(i)

ans = 0
for pos in posisions.values():
  left, right = 0, 0

  for i in range(len(pos)):
    if left < i + 1:
      left = i + 1
    if right < i + 1:
      right = i + 1

    while left < len(pos) and pos[left] - pos[i] < L:
      left += 1
    while right < len(pos) and pos[right] - pos[i] <= R:
      right += 1

    ans += right - left
    # print("i=", i, "left=", left, "right=", right)

print(ans)