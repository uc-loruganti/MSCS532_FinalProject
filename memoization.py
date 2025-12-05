import time

# =================================================================================
# Technique 3: Caching/Memoization/Lookup Table
# Demonstrates the optimization technique with the Fibonacci sequence, which has many overlapping subproblems.
# =================================================================================



#  Complexity: O(2^n) - very inefficient due to re-computation.
def fibonacci_simple(n):
    if n <= 1:
        return n
    return fibonacci_simple(n - 1) + fibonacci_simple(n - 2)

# Cache for the memoized version
fib_cache = {}

def fibonacci_memoized(n):
    """
    Memoized recursive Fibonacci calculation using a lookup table (cache).
    Complexity: O(n) - each Fibonacci number is computed only once and stored in the cache.
    """
    if n in fib_cache:
        return fib_cache[n]
    if n <= 1:
        return n
    
    result = fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
    fib_cache[n] = result # Store the result in the cache
    return result

# Demonstrates the performance difference with and without memoization.
def demo_memoization():
    print("="*50)
    print("Technique 3: Caching/Memoization")
    print("="*50)

    fib_n = 35 # A number large enough to show the difference
    
    # Time naive Fibonacci
    print(f"Calculating Fibonacci({fib_n}) without memoization...")
    start_time = time.perf_counter()
    fib_result_simple = fibonacci_simple(fib_n)
    end_time = time.perf_counter()
    print(f"Naive Fibonacci (O(2^n)) took: {end_time - start_time:.6f} seconds. Result: {fib_result_simple}")

    # Time memoized Fibonacci
    print(f"\nCalculating Fibonacci({fib_n}) with memoization...")
    start_time = time.perf_counter()
    fib_result_memoized = fibonacci_memoized(fib_n)
    end_time = time.perf_counter()
    print(f"Memoized Fibonacci (O(n)) took: {end_time - start_time:.8f} seconds. Result: {fib_result_memoized}")
    print("\nObservation: Memoization avoids re-computing the same subproblems, leading to a dramatic speedup.\n")

if __name__ == "__main__":
    demo_memoization()
