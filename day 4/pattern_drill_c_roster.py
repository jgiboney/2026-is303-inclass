# ============================================================
# Pattern Drill C: Class Roster Stats
# ============================================================
# The data is already loaded — your job is to write the loops.
# Complete each TODO using a for loop.
# ============================================================

# --- DATA (do not modify) -----------------------------------
students = ["Alex", "Jordan", "Taylor", "Morgan",
            "Casey", "Riley", "Quinn", "Avery"]
scores   = [88, 92, 75, 95, 67, 84, 91, 78]
majors   = ["IS", "CS", "IS", "Finance",
            "IS", "Marketing", "CS", "IS"]
# ------------------------------------------------------------


# TODO 1 — Accumulator
# Calculate the class average score.
# Hint: sum all scores, then divide by the count.



print(f"Class average: ___")  # replace ___ with your variable


# TODO 2 — Filter
# Build a list of students scoring 85 or above.
# Hint: loop through the indices so you can check scores[i]
#       and grab students[i].



print(f"High scorers (85+): ___")  # replace ___ with your list


# TODO 3 — Search
# Is there anyone majoring in "Finance"?
# Use a boolean flag — do NOT use the `in` operator.
# Hint: start with found = False, flip it inside the loop.



print(f"Finance major found: ___")  # replace ___ with your flag


# TODO 4 — Challenge (combine two patterns)
# What is the average score for IS majors only?
# Hint: you need to filter for IS majors AND accumulate
#       their scores in the same loop. Watch out for
#       dividing by zero if no IS majors exist.



print(f"IS major average: ___")  # replace ___ with your variable
