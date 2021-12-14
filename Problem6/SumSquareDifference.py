
list1 = []
list2 = list(range(1, 101))

for i in range(1, 101):
    list1.append(i**2)

a = (sum(list2))**2 - sum(list1)
print(a)