min_qiymat = None

for i in range(1, 8):
    a = int(input(f"{i}-sonni kiriting: "))
    if min_qiymat is None or a < min_qiymat:
        min_qiymat = a

print("Minimal qiymat:", min_qiymat)
