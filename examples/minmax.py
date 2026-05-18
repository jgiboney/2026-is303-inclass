
paintings = [
    {"name":"Park", "artist":"Holly", "year":1905},
    {"name":"Building", "artist":"Pete", "year":2010},
    {"name":"Flowers", "artist":"Michelangelo", "year":1650}
]

# Oldest painting
# Find the painting with the smallest year (minimum)

oldest_painting_so_far = {"year":10000}

# The variable painting is being created in the for loop
for painting in paintings:
    if painting["year"] < oldest_painting_so_far["year"]:
        oldest_painting_so_far = painting
    print(oldest_painting_so_far)


# Removes paintings one by one
# No variable created in a while loop
while len(paintings) > 0:
    print("removing first painting")
    paintings.remove(paintings[0])


# Add numbers until the sum is greater than 20.
our_sum = 0
current_number = 0
while our_sum < 20:
    our_sum += current_number
    current_number += 1
print(current_number, our_sum)