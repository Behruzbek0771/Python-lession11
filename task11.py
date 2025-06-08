n = int(input("Qancha qiymat kiritmoqchisiz: "))

min_qiymat = None
max_qiymat = None

for i in range(1, n+1):
    a = int(input(f"{i}-sonni kiriting: "))

    if min_qiymat is None or a < min_qiymat:
        min_qiymat = a

    if max_qiymat is None or a > max_qiymat:
        max_qiymat = a

ortacha = (min_qiymat + max_qiymat) / 2

print(ortacha)
