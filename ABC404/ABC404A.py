import string

S = list(map(str, input().strip()))

alphabet_list = list(string.ascii_lowercase)

ans_list = list(set(alphabet_list) - set(S))

print(ans_list[0])