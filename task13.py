min_qiymat = None
max_qiymat = None

for i in range(1, 6):
    a = int(input(f"{i}-sonni kiriting: "))

    if min_qiymat is None or a < min_qiymat:
        min_qiymat = a

    if max_qiymat is None or a > max_qiymat:
        max_qiymat = a

ortacha = (min_qiymat + max_qiymat) / 2

print(max_qiymat)
print(min_qiymat)
print(ortacha)
