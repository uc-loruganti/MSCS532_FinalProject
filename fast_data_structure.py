
import time

# =================================================================================
# Technique 2: Use of Fast Data Structure Interface
# Demostrates the optimization technique by comparing list (O(n)) vs. a dictionary (O(1) average) lookups.
# =================================================================================

# Demostrate the performance difference between list and dictionary lookups.
def demo_fast_data_structure():
    print("="*50)
    print("Technique 2: Fast Data Structure Interface")
    print("="*50)
    
    # Prepare data
    num_elements = 10_000_000
    list_data = list(range(num_elements))
    dict_data = {i: f"value_{i}" for i in range(num_elements)}
    lookup_key = num_elements - 1 # Key to search for
    
    # Time list lookup (using 'in' operator which is O(n))
    start_time = time.perf_counter()
    _ = lookup_key in list_data
    end_time = time.perf_counter()
    print(f"List 'in' lookup (O(n)) took: {end_time - start_time:.6f} seconds")

    # Time dictionary lookup (O(1) on average)
    start_time = time.perf_counter()
    _ = lookup_key in dict_data
    end_time = time.perf_counter()
    print(f"Dictionary 'in' lookup (O(1)) took: {end_time - start_time:.8f} seconds")
    print("\nObservation: Dictionary key lookup is almost instantaneous, showcasing the power of hash-based O(1) access.\n")

if __name__ == "__main__":
    demo_fast_data_structure()
