def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


f = fib
f(100)


"""
Coming from other languages, you might object that fib 
is not a function but a procedure since it doesn’t return 
a value. In fact, even functions without a return statement 
do return a value, albeit a rather boring one. 
This value is called None (it’s a built-in name). 
Writing the value None is normally suppressed by the
interpreter if it would be the only value written.
 You can see it if you really want to using print():
"""

t = f(200)
print(t)# This will print None since fib does not return a value


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    
    while a < n:
        result.append(a)
        a, b = b, a+b

    return result


f100 = fib2(100)
print(f100)