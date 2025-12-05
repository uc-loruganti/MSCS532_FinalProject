

import time

# =================================================================================
# Technique 1: Reducing Asymptotic Complexity of Search Algorithm
# =================================================================================
# Demostrate this optimization technique by comparing a linear search (O(n)) with a binary search (O(log n)).
# Binary search requires the data to be sorted.

# Performs a linear search to find the target in the array. Complexity: O(n)
    
def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Performs a binary search to find the target in a sorted array. Complexity: O(log n)
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Demonstrates the performance difference between linear and binary search.
def demo_asymptotic_complexity():
    print("="*50)
    print("Technique 1: Reducing Asymptotic Complexity")
    print("="*50)
    
    # Create a large, sorted list with the capacity of 10 million to demonstrate the difference
    large_sorted_list = list(range(10_000_000))
    target = 9_999_999 # Target is at the end to show worst-case for linear search
    
    # Time linear search
    start_time = time.perf_counter()
    linear_search(large_sorted_list, target)
    end_time = time.perf_counter()
    print(f"Linear Search (O(n)) took: {end_time - start_time:.6f} seconds")
    
    # Time binary search
    start_time = time.perf_counter()
    binary_search(large_sorted_list, target)
    end_time = time.perf_counter()
    print(f"Binary Search (O(log n)) took: {end_time - start_time:.6f} seconds")
    print("\nObservation: Binary search is significantly faster due to its logarithmic time complexity.\n")

if __name__ == "__main__":
    demo_asymptotic_complexity()
