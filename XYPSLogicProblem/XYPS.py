# The Problem
# Two perfect logicians, S and P, are told that integers 
# x and y have been chosen such that 1 < x < y and x+y < 100.  
# S is given the value x+y and P is given the value xy.  
# They then have the following conversation.

#     P:  I cannot determine the two numbers.
#     S:  I knew that.
#     P:  Now I can determine them.
#     S:  So can I.

# Given that the above statements are true, what are the two numbers? 

# Since S knew that P couldn't determine the numbers, it must be that no possible
# additive combo of the sum x + y are prime. 
#     i.e. x+y != 10 because 3+7 = 10, but 4+6=10, and S would not know if P had
#     21 (which P can easily deduce x and y be 3 and 7) or 24 (which P cannot deduce from)
# By this logic, 3+7=10 is not x+y, 3+11=14 is not x+y, etc.
import math
forbiddenSums = {0,1,2,3,4,6}
possibleProducts = set()
primes = []

def possibleSums():
    pos = set()
    for x in range(100):
        if x not in forbiddenSums:
            pos.add(x)
    return pos

def printSumMatrix(forbiddenSums={}):
    """Displays a matrix of the possible numbers for X+Y
    forbiddenSums: a set containing number not to be printed
    """
    for x in range(10):
        tensX = x * 10
        lineToPrint = ""
        for y in range(10):
            if (tensX+y) in forbiddenSums:
                lineToPrint = lineToPrint + "   "
            else:
                if (tensX+y) < 10:
                    lineToPrint = lineToPrint + "  " + str(tensX+y)
                else:
                    lineToPrint = lineToPrint + " " + str(tensX+y)
        print(lineToPrint)

def readPrimes():
    """Function that reads primes and adds them to the list of primes"""
    primeFile = open("../primes.txt", 'r')
    for line in primeFile:
        primesList = line.split()
        for prime in primesList:
            if int(prime) >= 100: 
                return
            primes.append(int(prime))

def removeSumsOfPrimes():
    """Function that adds all sums of two primes to the set of forbiddenSums"""
    for x in range(len(primes)):
        prime1 = primes[x]
        if x > 100:
            break
        for y in range(1, len(primes) - x):
            prime2 = primes[x+y]
            if (prime1 + prime2) > 100:
                break
            else:
                forbiddenSums.add(prime1+prime2)
    return

def populatePossibleProducts():
    for posSum in possibleSums():
        for i in range(2, posSum//2):
            addend1 = i
            addend2 = posSum-i
            possibleProducts.add(addend1*addend2)

def removePossibleProducts():
    """After having a populated list of possible products, check to see if
    more than one of the sums of its (non prime) factors is a possible sum
    If two or more of the sums of its factors exist, then it is eliminated:
    Example if 30 is a possible products, it has factors 5*6, 2*15, 5+6 = 11, 2+15 = 17
        but both 11 and 17 are possible sums, so 30 is out"""

        
def primeFactOf(n):
    primeFactors = []
    while n != 1:
        for prime in primes:
            if n%prime == 0:
                primeFactors.append(prime)
                n = n//prime
                break
    return primeFactors

def hasThreeOrMorePrimeFacts(n):
    if len(primeFactOf(n)) >= 3:
        return True
    else:
        print(n)
        print(primeFactOf(n))
        return False

readPrimes()
removeSumsOfPrimes()
populatePossibleProducts()
# print(possibleProducts)
printSumMatrix(forbiddenSums)
