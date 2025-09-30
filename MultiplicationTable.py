# Multiplication table that multiply upto 10

pro = 0

for x in range(1, 11):
    for y in range(1, 11):
        pro = x * y
        print(f"{x} * {y} = ", pro)