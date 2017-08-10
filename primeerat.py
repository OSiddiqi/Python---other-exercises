import itertools
import time
import math
 
start = time.time()      
def primeSieve(sieveSize):
    sieve = [True] * sieveSize
    sieve[0] = False # zero and one are not prime numbers
    sieve[1] = False

    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i
            primes = []
        for i in range(sieveSize):
            if sieve[i] == True:
                primes.append(i)
    print(primes)
    return primes
print('It took {0:0.3f} seconds'.format(time.time() - start))