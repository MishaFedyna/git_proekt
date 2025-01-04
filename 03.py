a = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''
zv = [list(map(int, i.split())) for i in a.splitlines()]

safe_zv = []
res = 0


# Функція для перевірки різниць між сусідніми елементами
def check_differences(lst):
    return all(0 < abs(lst[i] - lst[i + 1]) < 4 for i in range(len(lst) - 1))


# Функція для перевірки зростання або спадання
def is_sorted(lst):
    ascending = all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))
    descending = all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))
    # print(ascending , descending,lst)
    return ascending or descending


# Перевірка кожного рядка
for j in zv:
    for i in range(len(j)):
        modified = j[:i] + j[i + 1:]  # Видаляємо один елемент
        print(is_sorted(modified), check_differences(modified), modified)
        if check_differences(modified) and is_sorted(modified) :
            safe_zv.append(modified)
            res += 1
            break


print(res)
