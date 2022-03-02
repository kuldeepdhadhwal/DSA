def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

y = fib(30)
print(y)

def fib1(n,memo={}):
#     dynamic programming
    if n ==0 or n ==1:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib1(n-1,memo) + fib1(n-2,memo)
    return memo[n]

y = fib1(120)
print(y)
