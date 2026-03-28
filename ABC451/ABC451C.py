import heapq

Q = int(input())
heap = []

for _ in range(Q):
  t, h = map(int, input().split())

  if t == 1:
    heapq.heappush(heap, h)
  else:
    while heap and heap[0] <= h:
      heapq.heappop(heap)

  print(len(heap))