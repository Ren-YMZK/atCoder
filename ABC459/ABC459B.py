N = int(input())
S = input().split()

result = ""

for i in range(N):
  first = S[i][0]  # 先頭文字を取得

  if first in "abc":
    C = 2
  elif first in "def":
    C = 3
  elif first in "ghi":
    C = 4
  elif first in "jkl":
    C = 5
  elif first in "mno":
    C = 6
  elif first in "pqrs":
    C = 7
  elif first in "tuv":
    C = 8
  elif first in "wxyz":
    C = 9

  result += str(C)

print(result)