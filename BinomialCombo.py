import time
import random
from BinomialDnC import binomialCoeff1
from BinomialDP import binomialCoeff2

print("Hello,")
print("We are going to be comparing divide and concuer ,and dynamic programing.")
print("With the Binomial Coeficient")

for i in range(5):
    n = 15
    k = 10
    print(n,k)
    
    print("Here is the time for Binomial coefficient with divide and conquor:")

    start = time.perf_counter()
    binomialCoeff1(n, k)
    end = time.perf_counter()
    
    print ("Binomial of (%d,%d) is (%d)" % (n, k, binomialCoeff1(n, k)))
    print("Time consumed for  togetherDivide and Conquor: ",end - start)

    print("Here is the time for Binomial coefficient with Dynamic Programming:")

    start = time.perf_counter()
    binomialCoeff2(n, k)
    end = time.perf_counter()
    
    print("Binomial of (" + str(n) + ", " + str(k) + ") is", binomialCoeff2(n, k))
    print("Time consumed for Dynamic Programming: ",end - start)
