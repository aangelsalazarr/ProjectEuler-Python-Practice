primary = [1, 2]
secondary = []

while primary[-1] < 4E6:
    a = primary[-1]
    b = primary[-2]
    new_value = a + b
    primary.append(new_value)

for value in primary:
    if value % 2 == 0:
        secondary.append(value)

print(sum(secondary))