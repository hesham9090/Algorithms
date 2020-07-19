"""
Memoized Dynamic programing Algorithm for Fibonacci positive numbers (Top Down)

"""

def memoizedDPAlg(n):
    #Check if n is negative will return -1 means this function does not support negative nubers
    if n < 0:
        return -1
    memo = {}
    def fib(n):
        if n in memo:
            return memo[n]
        if n <= 2:
            fibN = 1
        else:
            fibN = fib(n - 1) + fib(n - 2)
        memo[n] = fibN
        print(memo)
        return fibN
    return fib(n)


print(memoizedDPAlg(9))

"""
Time Complexity is O(N)
Space Complexity is O(N)
"""