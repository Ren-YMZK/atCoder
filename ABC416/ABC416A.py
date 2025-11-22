N, L, R = map(int, input().split())
S = input()

moji = set(S[L-1:R])

if moji == {"o"}:
  print("Yes")
else:
  print("No")