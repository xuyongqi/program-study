#the nth Fibonacci number
def fib(n):
    a,b=0,1
    count = 1
    while count < n:
        a,b = b,a+b
        count = count +1
    print (a)

#
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return (fib(n-1)+ fib(n-2))