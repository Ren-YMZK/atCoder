X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())
P = [int(input()) for _ in range(Q)]

parts = []
weight = X

for i in range(Q):
  if P[i] in parts:
     #取り外す
     weight -= W[P[i]-1]
     parts.remove(P[i])
     print(weight)
  else:
    #取り付ける
    weight += W[P[i]-1]
    parts.append(P[i])
    print(weight)