a, b, c = map(int, input().split())
OK = False

if a != b and b != c and c != a:
  print("No")
else:
  print("Yes")
  
  
  
'''こっちでも可
a, b, c = map(int, input().split())

if a == b or b == c or c == a:
  print("Yes")
else:
  print("No")
'''