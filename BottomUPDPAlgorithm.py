"""
Bottom UP Dynamic Programming Algorithm
for Fibonacci positive number problem

"""

def bottomUPDPAlg(n):
    #Check if n is negative will return -1 means this functio does not support negative nubers
    if n < 0:
        return -1
    fibDic = {}
    for k in range(1,n+1):
        #Base case
        if k <= 2:
            fibN = 1
        else:
            fibN = fibDic[k-1] + fibDic[k-2]
        fibDic[k] = fibN
    return fibDic[n]



print(bottomUPDPAlg(9))

"""
Time Complexity is O(N)
Space Complexity is O(1)
"""