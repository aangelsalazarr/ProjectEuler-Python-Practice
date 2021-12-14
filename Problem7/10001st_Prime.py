# by listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is
# 13. What is the 10 001st prime number?

# for all n, all unique divisors of n are numbers less than or equal to sqrt(n)
# we know that all primes greater than 3 are of the form 6k +/- 1, where k is an int > 0

# want to create a primality test function
def is_prime(n: int) -> bool:
    """Primality test using 6k+1 optimization"""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# creating a variable list to store prime numbers while including primes <= 3
primes = []

n = 1

while len(primes) < 10001:
    if is_prime(n) == True:
        primes.append(n)
        n += 1
    else:
        n += 1

print(primes[-1])
