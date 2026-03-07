import sys
input = sys.stdin.readline

#入力
N, Q = map(int, input().split())
A = list(map(int, input().split()))

#クエリを一個ずつリストに入れる
queries = []
for _ in range(Q):
    K = int(input())
    B = list(map(int, input().split()))
    queries.append([K] + B)

#ボールを小さい順にしておく。（値, ボールの番号）
balls = sorted((A[i], i + 1) for i in range(N))

#クエリ一個ずつ見る
for query in queries:

  #クエリの一個目
  K = query[0]

  #取り除いたものの集合を作っておく
  removed = set(query[1:])

  #K+1まで一個ずつ見る
  for i in range(K + 1):

    #値と番号を取ってくる
    value = balls[i][0]
    index = balls[i][1]

    #それが取り除き集合になければ表示
    if index not in removed:
      print(value)
      break