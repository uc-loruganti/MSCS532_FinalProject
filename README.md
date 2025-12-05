# HPC Optimization Techniques Demonstration

This project provides Python code examples to demonstrate Domain and architecture agnostic algorithm and datastructure optimization techniques used in High-Performance Computing (HPC).

## Techniques Demonstrated

### 1. Reducing Asymptotic Complexity
- **Concept:** The most effective way to speed up an algorithm is to improve its fundamental efficiency (asymptotic complexity).
- **Demonstration:** We compare a `linear_search` (O(n)) with a `binary_search` (O(log n)) on a large, sorted dataset. The results clearly show that the algorithmic improvement leads to a massive performance gain.

### 2. Fast Data Structure Interface
- **Concept:** Choosing the right data structure for the task is critical. Operations that are slow on one data structure can be incredibly fast on another.
- **Demonstration:** We compare the time it takes to find an element in a Python `list` (which requires a linear scan, O(n)) versus looking up a key in a `dict` (which uses a hash table for average O(1) access). The dictionary lookup is orders of magnitude faster.

### 3. Caching / Memoization
- **Concept:** If a function repeatedly calculates the same results for the same inputs, we can store (cache) these results. Subsequent calls can then retrieve the result from the cache instead of re-computing it, saving significant time.
- **Demonstration:** We calculate a number in the Fibonacci sequence using a naive recursive function, which has exponential time complexity (O(2^n)) due to redundant calculations. We then show a memoized version that stores intermediate results in a cache, reducing the complexity to linear time (O(n)) and providing a dramatic speedup.

## How to Run
To see the performance demonstrations, simply run the Python script:
```sh
python main.py
```
### Expected ouput:
_Note: Execution time may change slightly, depending on the hardware and OS of the running system._  
```
==================================================
Technique 1: Reducing Asymptotic Complexity
==================================================
Linear Search (O(n)) took: 0.369491 seconds
Binary Search (O(log n)) took: 0.000037 seconds

Observation: Binary search is significantly faster due to its logarithmic time complexity.

==================================================
Technique 2: Fast Data Structure Interface
==================================================
List 'in' lookup (O(n)) took: 0.098527 seconds
Dictionary 'in' lookup (O(1)) took: 0.00101800 seconds

Observation: Dictionary key lookup is almost instantaneous, showcasing the power of hash-based O(1) access.

==================================================
Technique 3: Caching/Memoization
==================================================
Calculating Fibonacci(35) without memoization...
Naive Fibonacci (O(2^n)) took: 1.855077 seconds. Result: 9227465

Calculating Fibonacci(35) with memoization...
Memoized Fibonacci (O(n)) took: 0.00005740 seconds. Result: 9227465

Observation: Memoization avoids re-computing the same subproblems, leading to a dramatic speedup.
```
