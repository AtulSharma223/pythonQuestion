def fib(n):
    if(n==0 or n==1):
        return n
    c=fib(n-1)+fib(n-2)
    return c
n=10
nthValue=fib(10)
print("nth value",nthValue)