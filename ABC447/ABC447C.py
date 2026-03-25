S = str(input())
T = str(input())

S_noA = S.replace("A", "")
T_noA = T.replace("A", "")

if S_noA != T_noA:
  print(-1)
else:
  # Sの場所ごとのAの数のリスト
  s_counts = []
  # SのAの数を数える用の変数
  cnt = 0

  # 文字を一個ずつ見ていく
  for ch in S:
    # Aだったらカウント
    if ch == "A":
      cnt += 1
    # Aじゃなかったら、その前にあるAの数を記録
    else:
      s_counts.append(cnt)
      cnt = 0
  s_counts.append(cnt)

  # Tの場所ごとのAの数のリスト
  t_counts = []
  # TのAの数を数える用の変数
  cnt = 0

  for ch in T:
    # Aだったらカウント
    if ch == "A":
      cnt += 1
    # Aじゃなかったら、その前にあるAの数を記録
    else:
      t_counts.append(cnt)
      cnt = 0
  t_counts.append(cnt)

  # 答え用のやつ
  ans = 0

  # 各区間のAの数を比較して、絶対値を足していく
  for i in range(len(s_counts)):
    ans += abs(s_counts[i] - t_counts[i])

  print(ans)