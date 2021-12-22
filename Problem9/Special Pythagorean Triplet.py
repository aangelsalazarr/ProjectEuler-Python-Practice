import constraint

# we have to uphold the formula a+b+c= n | n = 1000 in our case
n = 1000

# next, our variables must meet the pythagorean criteria
# Find all (a, b, c) where (a, b, c) is an element of [0, 1000]
#  and a + b + c = 1000 and a**2 + b**2 = c**2 and a < b < c
problem = constraint.Problem()

problem.addVariable('a', range(1, int(n/3)))  # a < 1000 / 3
problem.addVariable('b', range(int(n/3), 1000))  # b < a can never occur
problem.addVariable('c', range(int(n/3), 1001)) # c < b < a can never occur


def our_constraint(a, b, c):
    if (n ** 2 - 2 * a * n) / (2 * n - 2 * a) == b:  # rearranging b given constraints
        if (a * a) + (b * b) == (c * c):
            return True


problem.addConstraint(our_constraint, ['a', 'b', 'c'])

solutions = problem.getSolutions()

print(solutions)

print(200*375*425)  # our answer -- took 3:23 to process (yikes)
