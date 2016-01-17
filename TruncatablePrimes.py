"""The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
primes = []

def isPrime(num = 0):
    return (num in primes)

def readPrimes(maximum = 100000):
    """Function that reads primes and adds them to the list of primes"""
    primeFile = open("1000000primes.txt", 'r')
    for line in primeFile:
        primesList = line.split()
        for prime in primesList:
            if int(prime) >= maximum: 
                return
            primes.append(int(prime))
def isLeftTruncatable(prime = 2):
    if not isPrime(prime):
        return False
    if prime in (2, 3, 5, 7):
        return False
    prime = str(prime)
    while (prime != ""):
        if not isPrime(int(prime)):
            return False
        prime = prime[1:]
    return True

def isRightTruncatable(prime = 2):
    if not isPrime(prime):
        return False
    if prime in (2,3,5,7):
        return False
    while(prime != 0):
        if not isPrime(prime):
            return False
        prime = prime//10
    return True

def determineTruncPrimes(primes = []):
    truncList = []
    for prime in primes:
        if isRightTruncatable(prime) and isLeftTruncatable(prime):
            truncList.append(prime)
    return truncList

readPrimes(1000000)
truncList = determineTruncPrimes(primes)
print(truncList)


