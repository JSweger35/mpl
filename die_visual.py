from die import Die

# create a D6
die = Die()

# Make some rolls, and store results in a list
results = []
for roll in range(100):
    result = die.roll()
    results.append(result)