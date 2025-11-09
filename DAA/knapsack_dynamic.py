# 0-1 Knapsack Problem using Dynamic Programming (with selected items)

def knapsack(weights, values, capacity):
    n = len(values)
    
    # Step 1: Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Step 2: Fill the DP table
    for i in range(1, n + 1):         # Loop through each item
        for w in range(1, capacity + 1):  # Loop through each capacity
            if weights[i-1] <= w:
                # If item can fit, check:
                # include item or exclude item → choose the better option
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                # If item can't fit, skip it
                dp[i][w] = dp[i-1][w]

    # Step 3: Backtrack to find which items are included
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:   # If value changes, item was included
            selected_items.append(i)
            w -= weights[i-1]

    selected_items.reverse()  # Show items in order

    # Step 4: Return result
    return dp[n][capacity], selected_items


# Example usage:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value, items = knapsack(weights, values, capacity)
print("Maximum value in Knapsack =", max_value)
print("Items included (1-indexed) =", items)

























































# 💡 EASY CONCEPTS (IN SIMPLE WORDS):

# 🎯 What is the problem?
# We have some items — each has a weight and a value.
# We have a bag (knapsack) with a maximum weight limit (capacity).
# We must choose some items to put in the bag so that:
# 👉 Total weight ≤ capacity
# 👉 Total value is maximum

# ⚙️ What does 0-1 mean?
# Either take the full item (1) or don’t take it (0). No fractions allowed.

# 🧠 How does the logic work?
# We use a **DP table (2D array)** where:
#   dp[i][w] = maximum value we can get using first i items with bag capacity w.

# For each item i:
#   We have two choices:
#   1️⃣ Include it — if weight of item ≤ remaining capacity
#       → value = item_value + best value of remaining capacity (dp[i-1][w - weight])
#   2️⃣ Exclude it — skip the item → dp[i-1][w]
#   We take the maximum of both.

# After filling the table:
#   dp[n][capacity] gives the maximum value possible.

# 🔁 Then we backtrack:
# We move from bottom of table and check which items were included 
# by comparing current and previous row values.

# 📊 Time Complexity:  O(n * capacity)
# 💾 Space Complexity: O(n * capacity)

# 🧾 SAMPLE INPUT:
# weights = [2, 3, 4, 5]
# values  = [3, 4, 5, 6]
# capacity = 5

# 🧮 SAMPLE OUTPUT:
# Maximum value in Knapsack = 7
# Items included (1-indexed) = [1, 2]

# ✅ SIMPLE EXPLANATION OF OUTPUT:
# Bag capacity = 5
# If we take Item 1 (weight 2, value 3) and Item 2 (weight 3, value 4)
# → Total weight = 2 + 3 = 5 (fits perfectly)
# → Total value = 3 + 4 = 7 (this is the best possible)
