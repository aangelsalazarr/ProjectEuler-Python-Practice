A = []
B = list(range(1, 1000))

for b in B:
    if b % 3 == 0  or b % 5 == 0:
        A.append(b)

print(A)
print(sum(A))
