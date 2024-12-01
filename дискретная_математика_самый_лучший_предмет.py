A = [1, 2, 3, 4, 6, 7, 9, 10, 11, 13, 14, 17, 24, 26, 28, 29, 31, 32, 34, 35, 37, 38, 39]
B = [1, 2, 4, 10, 12, 13, 15, 17, 18, 19, 25, 30, 33, 34, 35, 36, 37]
C = [2, 7, 9, 14, 16, 21, 23, 25, 27, 28, 29, 32, 34, 35, 36, 37, 38]
D = [1, 3, 5, 6, 9, 10, 14, 15, 19, 21, 23, 28, 29, 31, 34, 35, 36, 37]
def sim_raz(ar1, ar2):
    res = []
    for i in ar1:
        if i not in ar2:
            res.append(i)
    for i in ar2:
        if i not in ar1:
            res.append(i)
    return sorted(res)
def raz(ar1, ar2):
    res = []
    for i in ar1:
        if i not in ar2:
            res.append(i)
    return res
def unite(ar1, ar2):
    return sorted(set(ar1 + ar2))
def cross(ar1, ar2):
    res = []
    for i in ar1:
        if i in ar2:
            res.append(i)
    return res
# Вариант 7
# 1. ((B ∪ C) ∆ ((C ∪ A) ∆ D)) \ ((C ∩ A) ∪ (C ∩ B))
part1_1 = sim_raz(unite(B, C), sim_raz(unite(C, A), D))
part1_2 = unite(cross(C, A), cross(C, B))
res1 = raz(part1_1, part1_2)
# 2. ((D \ B) ∪ C) ∩ (((C ∪ B) ∩ A ∩ D) ∆ ((C ∪ D) ∩ (A ∪ B)))
part2_1 = unite(raz(D, B), C)
part2_2 = cross(cross(unite(C, B), A), D)
part2_3 = cross(unite(C, D), unite(A, B))
part2_4 = sim_raz(part2_2, part2_3)
res2 = cross(part2_1, part2_4)
print("Результат 1:", res1)
print("Результат 2:", res2)