def fib(n):
    a,b=0,1
    for i in range(n):
        print(a,end=' ')
        a,b=b,a+b
print('斐波那契数列:')
fib(20)