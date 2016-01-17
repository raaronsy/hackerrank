"""The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

import math

primes = []

def readPrimes(maximum = 100):
    """Function that reads primes and adds them to the list of primes"""
    primeFile = open("1000000primes.txt", 'r')
    for line in primeFile:
        primesList = line.split()
        for prime in primesList:
            if int(prime) >= maximum: 
                return
            primes.append(int(prime))
def summedSliceInList(start = 0, end = 1, theList = [0]):
    """Function that determines if the sum of slice of items in LIST
    from START to END equals another item in the list"""
    return sumTheSlice(start, end, theList) in theList

def sumTheSlice(start = 0, end = 1, theList = [0]):
    return math.fsum(theList[start:end])

def findMaxNumPrimes(primeList, maxSum):
    """Return the maximum number of primes in PRIMELIST that is less than maxSum
    Assume primeList is in order"""
    size = 1
    while (sumTheSlice(0, size, primeList) < maxSum):
        size += 1
    return size - 1

def findTheLongestSumPrime(maxSumPrime = math.pow(10, 6)):
    """Given the list of primes less than one million, from the prime that is equal to
    the longest sum of primes"""

    maxIndex = findMaxNumPrimes(primes, maxSumPrime) 
    size = maxIndex
    while (size > 0):
        start = 0
        while (start + size <= maxIndex):
            end = start + size
            if summedSliceInList(start, end, primes):
                return sumTheSlice(start, end, primes)
            else:
                start += 1
        size -= 1
    return 0

readPrimes(maximum = math.pow(10, 6))
print(findTheLongestSumPrime())
