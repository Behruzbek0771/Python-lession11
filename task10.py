max_qiymat = None

for i in range(1, 8):
    a = int(input(f"{i}-sonni kiriting: "))
    if max_qiymat is None or a > max_qiymat:
        max_qiymat = a

print("Maximal qiymat:", max_qiymat)
