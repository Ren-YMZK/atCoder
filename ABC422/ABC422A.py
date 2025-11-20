w, s = map(int, input().split('-'))

if s < 8:
    s += 1
else:
    w += 1
    s = 1

print(f"{w}-{s}")








# Sw, h, Ss = map(str, input().strip()) 

# Sw = int(Sw)
# Ss = int(Ss)
# Rw = 0
# Rs = 0

# if Sw <= 8 and Ss < 8:
#   Rw = Sw
#   Rs = Ss + 1
#   print(str(Rw) + '-' + str(Rs))
# elif Sw < 8 and Ss == 8:
#   Rw = Sw + 1
#   Rs = 1
#   print(str(Rw) + '-' + str(Rs))