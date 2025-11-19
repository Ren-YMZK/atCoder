s = input()
# s = "dreamerdreamerdreamerdreamereraserdreamer"

t = []

while (1):
  if s.endswith("dreamer"):
    s = s[:-7]
  elif s.endswith("eraser"):
    s = s[:-6]
  elif s.endswith("dream"):
    s = s[:-5]
  elif s.endswith("erase"):
    s = s[:-5]
  else:
    break

if s == "":
  print("YES")
else:
  print("NO")