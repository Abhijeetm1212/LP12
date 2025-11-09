# Job Sequencing with Deadlines using Greedy Algorithm

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit


def job_sequencing(jobs):
    # Step 1: Sort jobs by decreasing profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Step 2: Find maximum deadline
    max_deadline = max(job.deadline for job in jobs)

    # Step 3: Initialize time slots (None = free slot)
    slots = [None] * (max_deadline + 1)
    total_profit = 0

    # Step 4: Try to schedule each job in its latest possible slot
    for job in jobs:
        for slot in range(job.deadline, 0, -1):  # Go backward from job.deadline to 1
            if slots[slot] is None:              # If this slot is free
                slots[slot] = job.job_id         # Assign job here
                total_profit += job.profit       # Add its profit
                break                            # Move to next job

    # Step 5: Display final scheduled jobs and total profit
    scheduled_jobs = [job for job in slots if job is not None]
    print("Scheduled Jobs:", scheduled_jobs)
    print("Total Profit:", total_profit)



# --- Driver Code ---
if __name__ == "__main__":
    jobs = [
        Job('J1', 2, 100),
        Job('J2', 1, 19),
        Job('J3', 2, 27),
        Job('J4', 1, 25),
        Job('J5', 3, 15)
    ]

    job_sequencing(jobs)




























































# 💡 CONCEPTS IN EASY LANGUAGE 💡
# -----------------------------------------------------------
# 🔹 PROBLEM:
# We are given a set of jobs.
# Each job has:
#    → a deadline (last time it can be completed)
#    → a profit (money earned if completed before or on deadline)
#
# We can only do ONE job at a time (one per time slot).
# Goal = schedule jobs in such a way that total profit is MAXIMUM.
#
# -----------------------------------------------------------
# 🔹 WHY GREEDY APPROACH?
# Because we want maximum profit quickly.
# So we always choose the job which gives the HIGHEST profit first,
# and try to fit it before its deadline if there’s any empty slot.

# -----------------------------------------------------------
# 🔹 LOGIC IN SIMPLE WORDS:
# 1️⃣ Sort all jobs by profit (highest first)
# 2️⃣ Find the largest deadline among all jobs (it gives total slots)
# 3️⃣ For each job (starting from highest profit):
#       → Check if its deadline slot is empty
#       → If yes, schedule it there
#       → If not, check one slot before
#       → Continue until slot found or no slot left
# 4️⃣ Once all jobs checked → print scheduled jobs and total profit

# -----------------------------------------------------------
# 🔹 EXAMPLE:
# Jobs: (JobID, Deadline, Profit)
# J1 = (2, 100)
# J2 = (1, 19)
# J3 = (2, 27)
# J4 = (1, 25)
# J5 = (3, 15)
#
# Step 1: Sort by profit → J1(100), J3(27), J4(25), J2(19), J5(15)
# Step 2: Max deadline = 3 → slots = [None, None, None, None]
# Step 3:
#   - J1 → slot 2 free → place J1
#   - J3 → slot 2 full → try slot 1 → place J3
#   - J4 → slot 1 full → skip
#   - J2 → slot 1 full → skip
#   - J5 → slot 3 free → place J5
#
# ✅ Final schedule = [J3, J1, J5]
# ✅ Total profit = 27 + 100 + 15 = 142

# -----------------------------------------------------------
# 🔹 SAMPLE INPUT:
# Job('J1', 2, 100)
# Job('J2', 1, 19)
# Job('J3', 2, 27)
# Job('J4', 1, 25)
# Job('J5', 3, 15)

# 🔹 SAMPLE OUTPUT:
# Scheduled Jobs: ['J3', 'J1', 'J5']
# Total Profit: 142

# -----------------------------------------------------------
# 🔹 TIME COMPLEXITY:
# Sorting → O(n log n)
# Slot assignment → O(n * m), where m = max deadline
# Overall → O(n log n + n*m)
#
# 🔹 SPACE COMPLEXITY: O(m)
# -----------------------------------------------------------

