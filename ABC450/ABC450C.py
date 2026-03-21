from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

# 訪れたことがある場所を記録する
visited = [[False] * W for _ in range(H)]
ans = 0

# 全マス見る
for i in range(H):
  for j in range(W):

    #訪れてない白マスを見つけたら探索開始
    if S[i][j] == '.' and not visited[i][j]:
      # キューを用意して、[i][j]を入れる。
      q = deque()
      q.append((i, j))
      # 見たからvisitedをTrueにしておく
      visited[i][j] = True

      # 外周に触れてるかどうかをチェックする
      touches_border = False

      while q:
        # キューから一個取り出す
        x, y = q.popleft()

        # 取り出したやつが外周に触れていないかを調べる
        if x == 0 or x == H - 1 or y == 0 or y == W - 1:
          touches_border = True

        # 今見てるマスの上下左右を見る
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          nx = x + dx
          ny = y + dy

          # 範囲外じゃないかをチェックする
          if 0 <= nx < H and 0 <= ny < W:

            # 白マスかつ未探索だったら進む
            if S[nx][ny] == '.' and not visited[nx][ny]:
              visited[nx][ny] = True
              q.append((nx, ny))

      # 一個の塊を見て、外周に触れてなかったら数える
      if not touches_border:
        ans += 1

print(ans)