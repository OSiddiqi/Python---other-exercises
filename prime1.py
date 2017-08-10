import time
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
start = time.time()
for num in range(2,2000000000):
    if is_prime(num):
        print(num)

print('It took {0:0.3f} seconds'.format(time.time() - start))