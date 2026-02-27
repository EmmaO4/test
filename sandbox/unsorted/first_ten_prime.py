# prime defn: a number that can only be divided by itself and one. A whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11). 
# Whole Number: 0,1,2,3,...
# https://www.geeksforgeeks.org/python-def-keyword/     -- Example 2

'''
check if a number is prime

keep track of how many primes you've found

stop at 10
'''
import math

def tenPrimes(n):
    x = 2
    count = 0

    while count < n:
        is_prime = True
        for d in range(2, int(math.sqrt(x)) + 1):
            if x % d == 0:
                is_prime = False
                break
        if is_prime:
            print(x)
            count += 1
        x += 1

n = 10
tenPrimes(n)
