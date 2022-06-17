import time
import random
from KnapsackGreedy import knapSack_greed
from KnapsackDP import knapsack_DP

print("Hello,")
print("We are going to be comparing greedy algorithm ,and dynamic programing.")
print("With the Knapsack Problem")

for i in range(5):
    
    val = [60, 100, 120 ]
    wt = [10, 20, 30 ]
    W = 50
    n = len(val)
    
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
    
    print("Here is the time for Binomial coefficient with divide and conquor:")

    start = time.perf_counter()
    knapSack_greed(wt, val, W, n)
    end = time.perf_counter()
    
    print ("Knapsack of Greedy Algorithim:" % knapsack_greed(wt, val, W, n))
    print("Time consumed for Knapsack of Greedy Algorithim: ",end - start)

    print("Here is the time for Binomial coefficient with Dynamic Programming:")

    start = time.perf_counter()
    knapsack_DP(wt, val, W, n)
    end = time.perf_counter()
    
    print("Knapsack of Dynamic programming:", knapsack_DP(wt, val, W, n))
    print("Time consumed for Dynamic Programming: ",end - start)