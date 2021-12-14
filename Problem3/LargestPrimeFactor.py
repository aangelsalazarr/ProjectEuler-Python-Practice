import math

x = 600851475143
y = 3

while y < math.sqrt(x):
    if x % y == 0:
        x /= y
    else:
        y += 2

print(x)



