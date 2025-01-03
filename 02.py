

a = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1       
1 3 6 7 9"""
zv = [list(map(int,i.split())) for i in list(a.splitlines())]
print(zv)
print()
safe_zv = []
res = 0
for j in zv:
    valid = True
    for i in range(len(j)-1):
        if not (0 < abs(j[i] - j[i+1]) < 4 ):
            valid = False
            break
    if valid  and (j == sorted(j) or j == sorted(j, reverse=True)):
        res+=1
        safe_zv.append(j)
print(safe_zv)
print(res)