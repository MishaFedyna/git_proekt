n = 11
a = []
for i in range(n):
    a.append([0] * (i + 1))

for i in range(n):
    for j in range(n):
        if i == j or j == 0:
            a[i][j] = 1

        if i > j and j != 0:
            a[i][j] = a[i - 1][j] + a[i - 1][j - 1]
print(a)
print(a)
for i in a:
    print(i)
