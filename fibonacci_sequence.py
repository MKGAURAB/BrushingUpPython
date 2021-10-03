def fib_recursive(n):
    if n<=1 :
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

from functools import lru_cache
@lru_cache()
def fib_recursive_cached(n):
    if n<=1 :
        return n
    else:
        return fib_recursive_cached(n-1) + fib_recursive_cached(n-2)


def fib_gen(n):
    fib_0 = 1
    yield fib_0
    fib_1 = 1
    yield fib_1
    
    for i in range(n-2):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1

from timeit import timeit

def main():
    print(fib_recursive(10))
    print(timeit('fib_recursive(10)', globals=globals(), number=10))
    print(timeit('fib_recursive(28)', globals=globals(), number=10))
    print(timeit('fib_recursive(29)', globals=globals(), number=10))


    #Using cached version of the Fibonacci with recursion
    print("Using cached version of the Fibonacci with recursion")
    print(timeit('fib_recursive_cached(10)', globals=globals(), number=10))
    print(timeit('fib_recursive_cached(28)', globals=globals(), number=10))
    print(timeit('fib_recursive_cached(29)', globals=globals(), number=10))

    #Using iterative approach with generator
    print(f'Using iterative approach with generator with max depth {5000}')
    print(timeit('[num for num in fib_gen(5_000)]', globals=globals(), number=10))

if __name__ == '__main__':
    main()
    