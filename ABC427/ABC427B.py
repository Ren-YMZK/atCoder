N = int(input())

digit_list = [1 for _ in range(N)]

for i in range(1,N):
    digit_bef = digit_list[i-1]

    ans = sum(map(int, str(digit_bef)))

    digit_list[i] = digit_bef + ans

print(digit_list[N-1])


# N = int(input())

# digit = int(len(str(N)))

# digit_list = [0 for _ in range(digit)]

# for i in range(digit):
#   digit_list[i] = N // (10 ** (digit-1))
#   N = N % (10 ** (digit-1))
#   digit -= 1

# result = sum(digit_list)

# print(result)