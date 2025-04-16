import random
import matplotlib.pyplot as plt

# -----------------------------------------
# Scenario:
# You have three dice:
# - Die A: values from 1 to 6
# - Die B: values from 2 to 5
# - Die C: values from 1 to 8
# In each round, all three dice are rolled.
# The die with the highest number wins.
# If there's a tie, it's counted as a "Tie".
# We simulate 1000 rounds and visualize the results.
# -----------------------------------------

def roll_die(min_val, max_val):
    return random.randint(min_val, max_val)

def simulate_dice_competition(rounds=1000):
    wins = {"Die A": 0, "Die B": 0, "Die C": 0, "Tie": 0}
    
    for i in range(rounds):
        winners=[]
        die_a = roll_die(1, 6)
        die_b = roll_die(2, 5)
        die_c = roll_die(1, 8)

        rolls = {"Die A": die_a, "Die B": die_b, "Die C": die_c}
        max_value = max(rolls.values())

        for name, value in rolls.items():
            if value == max_value:
                winners.append(name)

        if len(winners) == 1:
            wins[winners[0]] += 1
        else:
            wins["Tie"] += 1

    return wins

# Run the simulation
results = simulate_dice_competition(1000)

# Print results
print("Results after 1000 rounds:")
for die, count in results.items():
    print(f"{die}: {count} wins")

# Plotting with matplotlib
labels = list(results.keys())
values = list(results.values())

plt.figure(figsize=(8, 5))
plt.bar(labels, values)
plt.title("Dice Competition Results")
plt.xlabel("Dice")
plt.ylabel("Number of Wins")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#  PIE CHART
plt.figure(figsize=(6, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Dice Competition Results (Pie Chart)")
plt.axis('equal')  # Equal aspect ratio makes the pie a circle
plt.tight_layout()
plt.show()

