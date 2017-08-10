import time

start = time.time()

def primes_method5(n):
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    #print(out)
    return out
(primes_method5(2000000000))
print('It took {0:0.3f} seconds'.format(time.time() - start))