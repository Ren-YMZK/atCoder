N, M = map(int, input().split())
A_list = list(map(int, input().split()))

ans = 0

for i in range(N):
    for j in range(N):
        x = A_list[i]
        y = A_list[j]
        s = int(str(x) + str(y))
        if s % M == 0:
            ans += 1

print(ans)