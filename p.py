#http://pi3.sites.sheffield.ac.uk/tutorials/week-3-prime-numbers
def apply_sieve(n):

    a = [1]*(n+1)  # Start with a list of 1s, of length (n+1). 
    a[0] = 0  # set to zero, as
    a[1] = 0  # neither 0 nor 1 are primes
    p = 2     # 2 is the first prime
    pmax = int(round(n**0.5)) + 1  # we only need to sieve up to square root of n.
    while p < pmax:
        while a[p] == 0:
            p += 1
        j = 2*p
        while j < n:
            a[j] = 0
            j += p
        p += 1
    return [p for p in range(n+1) if a[p] == 1]  # return the list of primes, which are the numbers we have NOT crossed out.

ok = False
while not ok:
    userInput = input("Please enter the size of the sieve : ")
    try:
        n = int(userInput)
        if n<2:
            print("Please enter an integer greater than 1.")
        else:
            ok = True
    except ValueError:
        print("Please enter an integer.")

import time  # Time how long the sieve takes to run
t1 = time.time() 
primes = apply_sieve(n)
t2 = time.time()

print ("#########################")
print (" The sieve took %.3f seconds to run." % ((t2-t1)))

import math
print (" There are %d primes less than or equal to %d." % (len(primes), n))
#print (" N / ln(N) = %d." % (round(n / math.log(n))))

#m = 100
#print ("Here are the first %d primes: " % (m))
#print (primes[:m])

#def isPrime(k, ps):
#    i = 0
#    maxi = k**0.5
#    for p in ps:
#        if p > maxi:
#            break
#        if k % p == 0:
#            return p
#    return 0

#def primeFactors(k, ps):
#    j = k
#    facs = []
#    ok = True
#    while ok:
#        fac = isPrime(j, ps)
#        if fac == 0:
#            facs.append(j)
#            ok = False
#        else:
#            facs.append(fac)
#            j = j / fac
#    return facs
#
#print ("#########################")
#print ("Looking for factors of the Fermat numbers 2^(2^n) + 1")
#for k in range(7):
#    j = 2**(2**k) + 1
#    print (k, j, isPrime(j, primes))
#
#print ("#########################")
#print ("Finding the prime factors of the Mersenne numbers:")
#for k in range(64):
#    j = 2**k - 1
#    if j < n:
#        print (k, j, primeFactors(j, primes))