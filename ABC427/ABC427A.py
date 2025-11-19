S = str(input())

letter_id = len(S) // 2

result = S[:letter_id] + S[letter_id + 1:]

print(result)