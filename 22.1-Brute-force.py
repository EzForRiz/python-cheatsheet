# 🧠 Brute Force Algorithm Cheatsheet

## 💡 Concept
**Brute Force** → simplest approach where we check **all possible options** to find the correct answer.  
No shortcuts — just a full scan of the data.

Used when:
- Data is **unsorted**
- We want **guaranteed correctness**
- Efficiency is not a priority

---





## ⚙️ Example 1: Find Index of a Given Element

```python
def find_index(lst, key):
    """
    Finds the index of a specific element in the list.
    :param lst: List of integers
    :param key: Element to find
    :return: Index of element if found, otherwise -1
    """
    
    # Loop through each element in the list
    for i in range(len(lst)):
        # Check if the current element matches the key
        if lst[i] == key:
            return i  # Return index if found

    return -1  # If not found, return -1


# Example
nums = [2, 4, 6, 3, 5, 7, 9, 1, 8]
print(find_index(nums, 7))  # Output: 5


"""
Explanation:

The algorithm checks every element one by one.

Stops only when it finds a match or reaches the end of the list.

Time Complexity: O(n)

Best case: Element found early.

Worst case: Element at the end or not present."""








#Example 2: Find Index of Maximum Element

def maximum_index(lst):
    """
    Finds the index of the maximum element in the list.
    :param lst: List of integers
    :return: Index of the maximum element
    """
    
    max_index = -1       # Start with no index found
    max_val = -99999     # Initialize with a very small number
    
    # Check every element in the list
    for i in range(len(lst)):
        if max_val < lst[i]:   # If current element is greater
            max_val = lst[i]   # Update max value
            max_index = i      # Update max index

    return max_index


# Example
nums = [2, 4, 6, 3, 5, 7, 9, 1, 8]
idx = maximum_index(nums)
print("Max value:", nums[idx], "at index:", idx)


"""
Explanation:

Checks every element to find the largest value.

Keeps track of both max value and its index.

Time Complexity: O(n)

Uses brute force → full list traversal."""









#Example 3: Find Index of Minimum Element

def minimum_index(lst):
    """
    Finds the index of the minimum element in the list.
    :param lst: List of integers
    :return: Index of the minimum element
    """
    
    min_index = -1      # Start with no index found
    min_val = 9999      # Initialize with a very large number
    
    # Check every element in the list
    for i in range(len(lst)):
        if min_val > lst[i]:   # If current element is smaller
            min_val = lst[i]   # Update min value
            min_index = i      # Update min index

    return min_index


# Example
nums = [2, 4, 6, 3, 5, 7, 9, 1, 8]
idx = minimum_index(nums)
print("Min value:", nums[idx], "at index:", idx)


"""Explanation:

Checks all elements to find the smallest value.

Updates min value and its index when a smaller one is found.

Time Complexity: O(n)"""