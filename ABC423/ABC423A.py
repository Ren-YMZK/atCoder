X, C = map(int, input().split())

unit = X // (1000 + C)

money = unit * 1000

print(money)