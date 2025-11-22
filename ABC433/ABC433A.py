X, Y, Z = map(int, input().split())

takahashi = X
aoki = Y
age = False

for i in range(100):
    if takahashi == aoki * Z:
        age = True

    takahashi += 1
    aoki += 1

if age:
    print("Yes")
else:
    print("No")
