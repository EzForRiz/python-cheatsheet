"""
🧠 22.3 - Greedy Algorithms
----------------------------
The **Greedy Algorithm** builds a solution step by step.
At each step, it chooses the **best immediate (local) option**, 
hoping that this leads to the **best overall (global) solution**.

It’s called *greedy* because it always takes the choice 
that looks best *right now* — without worrying about future consequences.
"""

"""
⚙️ Greedy Choice Property
--------------------------
If a global optimum can be reached by choosing local optimums,
the problem can be solved using the greedy method.
"""

"""
🔗 Optimal Substructure
-----------------------
An optimal solution to the whole problem contains
optimal solutions to its subproblems.

Example: The shortest path between A and C that goes through B
also contains the shortest path from A to B.
"""

# 🧩 Example 1: Greedy Coin Change Problem
# -----------------------------------------
# Problem: Given coin denominations and a total amount,
# find the minimum number of coins needed to make that amount.
# (Assuming we can use each coin unlimited times.)

def greedy_coin_change(coins, amount):
    """
    Greedy approach: always pick the largest coin possible first.
    """
    coins.sort(reverse=True)  # Sort coins in descending order
    result = []
    
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)  # Pick the largest possible coin each time
    
    return result

# Example run
coins = [1, 2, 5, 10, 20, 50]
amount = 93
change = greedy_coin_change(coins, amount)
print("Coins used:", change)
# Output: [50, 20, 20, 2, 1] → Total = 93


"""
💬 Explanation:
---------------
The algorithm picks:
- 50 first → remaining 43
- 20 → remaining 23
- 20 → remaining 3
- 2 → remaining 1
- 1 → remaining 0 ✅

It takes the *locally best choice (largest coin)* at each step.
This works perfectly here because local optimum = global optimum.
"""

# 🧩 Example 2: Greedy Activity Selection
# ---------------------------------------
# Problem: Select the maximum number of activities that don't overlap,
# given their start and end times.

def activity_selection(activities):
    """
    Each activity is a tuple (start_time, end_time).
    Greedy choice: Always pick the next activity that finishes earliest.
    """
    # Sort activities based on end time
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]
    last_end_time = activities[0][1]
    
    for i in range(1, len(activities)):
        # If current activity starts after or when previous one ends, select it
        if activities[i][0] >= last_end_time:
            selected.append(activities[i])
            last_end_time = activities[i][1]
    
    return selected

# Example run
activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9), (8, 9)]
selected = activity_selection(activities)
print("Selected activities:", selected)
# Output: [(1, 3), (4, 6), (6, 7), (8, 9)]


"""
💬 Explanation:
---------------
The algorithm always picks the activity that ends the earliest,
so it leaves maximum room for others → a greedy strategy.

✅ Works here because each local choice leads to a globally optimal set.
"""

"""
✅ Advantages
--------------
- Easy to understand and implement
- Works well when local optimum = global optimum
- Efficient and fast for certain problems

❌ Disadvantages
----------------
- Doesn’t always guarantee the best global solution
- May fail if the problem doesn’t satisfy the greedy choice property

🕒 Time Complexity:
Depends on the problem:
- Coin Change (sorting + loop): O(n log n)
- Activity Selection: O(n log n)

"""

"""
🧩 TL;DR
---------
Greedy Algorithm = Always pick the best immediate option.
It’s fast and simple but not always correct for every problem.
"""

