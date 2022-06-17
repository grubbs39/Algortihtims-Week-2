def binomialCoeff1(n, k):
 
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
 
    # Recursive Call
    return binomialCoeff1(n-1, k-1) + binomialCoeff1(n-1, k)
