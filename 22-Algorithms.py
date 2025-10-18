"""
🧠 22 - Algorithms
-------------------
An **algorithm** is a set of clear, step-by-step instructions to solve a problem.

Think of it like a recipe:
1. Take input
2. Process it
3. Produce output

Every algorithm aims to solve a specific problem efficiently.
"""

# 🧩 Example 1: A simple algorithm — find the sum of two numbers

def add_numbers(a, b):
    # Step 1: Take two inputs (a and b)
    # Step 2: Add them
    # Step 3: Return the result
    return a + b

print(add_numbers(3, 5))  # Output: 8


# 🧩 Example 2: Algorithm to find the largest number in a list

def find_max(lst):
    # Step 1: Assume the first element is the largest
    max_num = lst[0]
    
    # Step 2: Compare each element with the current max
    for num in lst:
        if num > max_num:
            max_num = num
    
    # Step 3: Return the largest number found
    return max_num

print(find_max([2, 5, 1, 9, 3]))  # Output: 9


# 🧩 Example 3: Algorithm to check if a number is even or odd

def check_even_odd(num):
    # Step 1: Divide the number by 2
    # Step 2: If remainder is 0 → even, else odd
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))  # Output: Odd


"""
⚙️ Characteristics of a Good Algorithm
-------------------------------------
1. **Input** – Takes valid inputs
2. **Output** – Produces correct results
3. **Definiteness** – Each step is clear and unambiguous
4. **Finiteness** – Must finish after a limited number of steps
5. **Effectiveness** – Each step must be doable

"""

"""
🕒 Algorithm Efficiency
-----------------------
We measure how good an algorithm is using:

- **Time Complexity** → how long it takes to run
- **Space Complexity** → how much memory it uses

Example:
- Linear Search → O(n)
- Binary Search → O(log n)
- Sorting (Bubble Sort) → O(n²)

The lower the complexity, the faster the algorithm.
"""

"""
✅ Summary
----------
Algorithm = step-by-step method to solve a problem.

Different types include:
- Brute Force
- Divide and Conquer
- Greedy
- Dynamic Programming
- Backtracking
- Recursive

Next: 22.1 - Brute Force Algorithm
"""
