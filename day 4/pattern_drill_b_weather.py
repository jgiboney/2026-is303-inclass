# ============================================================
# Pattern Drill B: Provo Weather Week
# ============================================================
# The data is already loaded — your job is to write the loops.
# Complete each TODO using a for loop.
# ============================================================

# --- DATA (do not modify) -----------------------------------
days       = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
highs      = [72, 68, 75, 80, 77, 65, 70]
lows       = [45, 42, 48, 52, 50, 40, 44]
conditions = ["sunny", "cloudy", "sunny", "sunny",
              "rain", "rain", "cloudy"]
# ------------------------------------------------------------


# TODO 1 — Accumulator
# Calculate the average high temperature for the week.
# Hint: sum all highs, then divide by the count.



print(f"Average high: ___")  # replace ___ with your variable


# TODO 2 — Filter
# Build a list of days that were sunny.
# Hint: loop through the indices so you can check conditions[i]
#       and grab days[i].



print(f"Sunny days: ___")  # replace ___ with your list


# TODO 3 — Search
# Was there any rain this week?
# Use a boolean flag — do NOT use the `in` operator.
# Hint: start with found = False, flip it inside the loop.



print(f"Rain this week: ___")  # replace ___ with your flag


# TODO 4 — Challenge (combine two patterns)
# Which day had the biggest temperature swing (high - low)?
# Hint: you need a loop that tracks the biggest swing AND
#       which day it belongs to.



print(f"Biggest swing: ___ on ___")  # replace with degrees and day
