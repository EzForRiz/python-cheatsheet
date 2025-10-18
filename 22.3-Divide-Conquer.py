"""
🧠 22.4 - Divide and Conquer
----------------------------
Divide and Conquer is an algorithmic paradigm that:
1️⃣ Divides a problem into smaller subproblems  
2️⃣ Conquers (solves) those subproblems  
3️⃣ Merges their results to form the final answer  

It’s often used with recursion (like in Merge Sort, Quick Sort, etc.).
"""

"""
⚙️ Steps:
---------
1. **Divide** → Split the problem into smaller subproblems  
2. **Conquer** → Solve each subproblem (often recursively)  
3. **Merge** → Combine all solutions into one
"""

# 🧩 Example: Convert a list of mixed-case letters to lowercase
# -------------------------------------------------------------

def to_lowercase_divide_and_conquer(lst):
    # Base (atomic) case: if list has one character
    if len(lst) == 1:
        return [lst[0].lower()]
    
    # Step 1: Divide → split into two halves
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    
    # Step 2: Conquer → solve sublists recursively
    lower_left = to_lowercase_divide_and_conquer(left)
    lower_right = to_lowercase_divide_and_conquer(right)
    
    # Step 3: Merge → combine results
    return lower_left + lower_right


# Example run
chars = ['A', 'b', 'C', 'd', 'E', 'F']
print(to_lowercase_divide_and_conquer(chars))
# Output: ['a', 'b', 'c', 'd', 'e', 'f']

"""
💬 Explanation:
---------------
- The list is divided until only single characters remain (atomic problems)
- Each is converted to lowercase
- Then all sublists are merged together
"""

"""
✅ Advantages
--------------
- Efficient when problems can be divided evenly (e.g., sorting)
- Uses cache memory efficiently (smaller problems fit in cache)

❌ Disadvantages
----------------
- Recursive → can be slow or memory-heavy
- Sometimes more complex than a simple loop

🕒 Example Complexities:
- Merge Sort → O(n log n)
- Binary Search → O(log n)
"""

"""
🧩 TL;DR
---------
Divide → Conquer → Merge  
Break problems down, solve smaller parts, then combine.
"""

