def fib1(n):
    # perfomance O(n), memory O(1)
    if n == 0: return 0
    a, b = 0, 1
    while n-1: 
        a, b = b, a + b
        n -= 1
    return b
    
def fib2(n):
    # perfomance O(n^2), memory O(n)
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)
    
def fib3(n):
    # more code, but perfomance O(log(n)), memory O(1)
    a = [1, 1, 1, 0]
    r = [0, 1]
    while n:
        if n & 1:
            r = [a[0] * r[0] + a[2] * r[1],
                 a[1] * r[0] + a[3] * r[1]]
        a = [a[0] ** 2 + a[1] * a[2],
             a[0] * a[1] + a[1] * a[3],
             a[0] * a[2] + a[2] * a[3],
             a[1] * a[2] + a[3] ** 2]
        n >>= 1
    return r[0]
