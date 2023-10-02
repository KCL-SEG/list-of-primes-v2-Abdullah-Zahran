"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError()
    primes = [2]
    i = 1
    while len(primes) < number_of_primes:
        prime = True
        i+=2
        for primeNum in primes:
            if i % primeNum == 0:
                prime = False
                break
        if prime:
            primes.append(i)

    return primes