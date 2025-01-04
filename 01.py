a = """3   4
4   3
2   5
1   3
3   9
3   3"""

rows = [list(map(int, row.split())) for row in a.splitlines()]
print(rows)

transposed = list(map(list, zip(*rows)))
print(transposed)

sorted_transposed = [sorted(s) for s in transposed]

print(sorted_transposed)

differences = [abs(x-y) for x, y in zip(*sorted_transposed)]
print(differences)

total_sum = sum(differences)
print(total_sum)

res = 0
for number in transposed[0]:
    x = transposed[1].count(number)
    res += number * x

print(res)