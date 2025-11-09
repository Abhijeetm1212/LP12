# Program to generate Binomial Coefficients using Dynamic Programming

def binomial_coefficient(n, k):
    # Create a 2D DP table to store values of C(n, k)
    C = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    # Calculate value of Binomial Coefficient in bottom-up manner
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base Cases
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                # Using Pascal’s Rule: C(n,k) = C(n-1,k-1) + C(n-1,k)
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    return C[n][k]


# Driver code
n = int(input("Enter value of n: "))
k = int(input("Enter value of k: "))

print(f"Binomial Coefficient C({n}, {k}) = {binomial_coefficient(n, k)}")









































































































































































































































# 💡 CONCEPTS IN SIMPLE LANGUAGE 💡
# ------------------------------------------------------------
# 🔹 What is Binomial Coefficient?
# Binomial Coefficient C(n, k) means "how many ways can we choose k items from n items".
# Formula: C(n, k) = n! / (k! * (n - k)!)
#
# Example: C(5, 2) = 10
# (Means there are 10 ways to choose 2 items out of 5)
#
# ------------------------------------------------------------
# 🔹 Why use Dynamic Programming (DP)?
# Using factorials directly can be slow for large n and may cause overflow.
# So, we use Pascal’s Rule to calculate step by step:
# C(n, k) = C(n-1, k-1) + C(n-1, k)
#
# ------------------------------------------------------------
# 🔹 Base Cases:
# C(n, 0) = 1  → Only one way to choose none of the items.
# C(n, n) = 1  → Only one way to choose all items.
#
# ------------------------------------------------------------
# 🔹 How the DP Table Works:
# Each value depends on the two values above it (like Pascal’s Triangle)
#
# Example for n = 4, k = 2:
# Pascal’s Triangle:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# So, C(4, 2) = 6
#
# ------------------------------------------------------------
# 🔹 Time Complexity:  O(n * k)
# 🔹 Space Complexity: O(n * k)
#
# ------------------------------------------------------------
# 🧮 EXAMPLE INPUT AND OUTPUT 🧮
#
# Example 1:
# Input:
# Enter value of n: 5
# Enter value of k: 2
#
# Output:
# Binomial Coefficient C(5, 2) = 10
#
# ------------------------------------------------------------
# Example 2:
# Input:
# Enter value of n: 6
# Enter value of k: 3
#
# Output:
# Binomial Coefficient C(6, 3) = 20
#
# ------------------------------------------------------------
# ✅ This program uses Dynamic Programming (Bottom-Up approach)
# ✅ Efficient and avoids repeated recursive calls
# ✅ Very useful in combinatorics and probability problems
# ------------------------------------------------------------
