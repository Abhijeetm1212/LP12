# Iterative Fibonacci with step counter

def fib_iterative(n):
    steps = 0
    if n == 0:
        steps += 1
        return 0, steps
    elif n == 1:
        steps += 1
        return 1, steps
    
    a, b = 0, 1
    for i in range(2, n + 1):
        steps += 1
        a, b = b, a + b
    return b, steps


n = int(input("Enter n: "))
result, steps = fib_iterative(n)
print(f"Fibonacci({n}) = {result}")
print(f"Step count (iterative) = {steps}")




# Recursive Fibonacci with step counter

steps = 0  # global step counter

def fib_recursive(n):
    global steps
    steps += 1  # count each call as a step
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


n = int(input("Enter n: "))
steps = 0
result = fib_recursive(n)
print(f"Fibonacci({n}) = {result}")
print(f"Step count (recursive) = {steps}")

























































################################################################################################################################
# 💡 CONCEPTS IN EASY LANGUAGE:
# Fibonacci series means each number is the sum of the previous two numbers.
# Example: 0, 1, 1, 2, 3, 5, 8, 13, ...
# So,
# F(0) = 0
# F(1) = 1
# F(2) = 1  (0 + 1)
# F(3) = 2  (1 + 1)
# F(4) = 3  (1 + 2)
# F(5) = 5  (2 + 3)
# and so on...


# 🧠 LOGIC IN SIMPLE WORDS:

# ➤ Iterative Method:
# - Start from 0 and 1.
# - Keep adding the previous two numbers to get the next one.
# - Use a loop to go up to n.
# - "steps" count shows how many times the loop ran (how many calculations done).

# ➤ Recursive Method:
# - Function keeps calling itself for (n-1) and (n-2).
# - Adds both results together.
# - "steps" count shows how many total function calls happened.
# - Works same as mathematical formula:
#       F(n) = F(n-1) + F(n-2)


# 🧩 DIFFERENCE:
# - Iterative → faster, uses loops (less steps)
# - Recursive → slower, repeats same work many times (more steps)


# 🧮 FORMULA:
# F(n) = F(n-1) + F(n-2)
# Base cases → F(0) = 0, F(1) = 1


# 🧾 SAMPLE INPUT AND OUTPUT:

# INPUT 1:
# Enter n: 5
# OUTPUT (Iterative Part):
# Fibonacci(5) = 5
# Step count (iterative) = 4

# OUTPUT (Recursive Part):
# Fibonacci(5) = 5
# Step count (recursive) = 15


# INPUT 2:
# Enter n: 7
# OUTPUT (Iterative Part):
# Fibonacci(7) = 13
# Step count (iterative) = 6

# OUTPUT (Recursive Part):
# Fibonacci(7) = 13
# Step count (recursive) = 41


# ✅ CONCLUSION:
# - Both methods give the same Fibonacci value.
# - Iterative method is efficient and takes fewer steps.
# - Recursive method is slower but shows how recursion expands into many calls.
################################################################################################################################

