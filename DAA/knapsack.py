def knapsack_dp():
    # Step 1: Take user input
    n = int(input("Enter number of items: "))

    weights = []
    values = []

    print("\nEnter weight and value (profit) for each item separated by space:")
    for i in range(n):
        w, v = map(int, input(f"Item {i+1}: ").split())
        weights.append(w)
        values.append(v)

    W = int(input("\nEnter maximum capacity of knapsack: "))

    # Step 2: Create DP table (2D list)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Step 3: Build DP table (Bottom-up approach)
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:  # If current item can fit in the bag
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    # Step 4: Final answer is in dp[n][W]
    print("\nMaximum profit that can be obtained:", dp[n][W])


if __name__ == "__main__":
    knapsack_dp()































































# 🔶 CONCEPT IN EASY LANGUAGE 🔶
# -------------------------------------------------------------
# 🧠 What is 0/1 Knapsack Problem?
# → You have 'n' items, each with a weight and a value (profit).
# → You also have a bag (knapsack) that can hold up to a maximum weight 'W'.
# → You must pick items such that:
#       1️⃣ Total weight ≤ W
#       2️⃣ Total profit is maximum
# → You can either take an item completely (1) or not take it at all (0).
#    (That’s why it’s called “0/1 Knapsack”)

# 🧮 Concept of Dynamic Programming:
# We create a table (2D array) dp[i][w] where:
# → i = number of items considered
# → w = current capacity of knapsack
# → dp[i][w] = maximum profit with first i items and capacity w

# Formula:
# If weight of item i-1 <= w:
#     dp[i][w] = max(value[i-1] + dp[i-1][w - weight[i-1]], dp[i-1][w])
# Else:
#     dp[i][w] = dp[i-1][w]

# 🚀 The table is built step by step (bottom-up) and the final answer is dp[n][W].

# -------------------------------------------------------------
# ✅ SAMPLE INPUT:
# Enter number of items: 3
# Enter weight and value (profit) for each item separated by space:
# Item 1: 10 60
# Item 2: 20 110
# Item 3: 30 150
# Enter maximum capacity of knapsack: 50

# ✅ SAMPLE OUTPUT:
# Maximum profit that can be obtained: 260
# -------------------------------------------------------------
