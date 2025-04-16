import random 
import matplotlib.pyplot as plt

# Simulate drawing 3 balls with replacement from a bucket
# with 3 red (R) and 3 green (G)
def draw_balls(n=3):
    bucket = ['R', 'G', 'R', 'G', 'R', 'G']  # 3 Red, 3 Green
    result = []  # This will store the balls we draw

    for i in range(n):  # Repeat n times
        chosen_ball = random.choice(bucket)  # Pick one ball randomly
        result.append(chosen_ball)  # Add it to the result list

    return result

# Run 1000 trials and record specific outcomes
def simulate_draws(num_trials=1000):
     """
    Simulates drawing 3 balls with replacement from a bucket containing
    3 red ('R') and 3 green ('G') balls, repeated over a number of trials.

    For each trial, tracks the frequency of specific outcomes:
    
    - "RRR": All three draws are red.
    - "RGR": The exact sequence Red → Green → Red.
    - "2R1G": Any sequence with exactly two red balls and one green.
    - "R>=G": Any sequence where the number of red balls is greater than
             or equal to the number of green balls.

    Parameters:
        num_trials (int): Number of simulation runs to perform (default is 1000).

    Returns:
        dict: A dictionary mapping each tracked outcome to its observed frequency.
              Keys: "RRR", "RGR", "2R1G", "R>=G"
              Values: Integer counts of how many times each condition occurred.
    """
    counts = {"RRR": 0, "RGR": 0, "2R1G": 0, "R>=G": 0}
    for i in range(num_trials):
        draw = draw_balls()
        r_count = draw.count('R')
        g_count = draw.count('G')
        if draw == ['R', 'R', 'R']:
            counts["RRR"] += 1
        if draw == ['R', 'G', 'R']:
            counts["RGR"] += 1
        if r_count == 2 and g_count == 1:
            counts["2R1G"] += 1
        if r_count >= g_count:
            counts["R>=G"] += 1
    return counts

# Plotting the results
def plot_results(result_dict):
    plt.bar(result_dict.keys(), result_dict.values())
    plt.title("Results from 1000 Simulations")
    plt.ylabel("Frequency")
    plt.show()

# Run simulation and plot
result = simulate_draws()
print(result)
plot_results(result)

def plot_pie_chart(result_dict):
    plt.figure(figsize=(6, 6))
    plt.pie(result_dict.values(), labels=result_dict.keys(), autopct='%1.1f%%', startangle=90)
    plt.title("Winning Proportions (1000 Simulations)")
    plt.axis('equal')  # Ensures the pie is circular
    plt.show()
    
plot_pie_chart(result)

def plot_horizontal_bar(result_dict):
    plt.figure(figsize=(8, 5))
    plt.barh(list(result_dict.keys()), list(result_dict.values()), color='skyblue')
    plt.xlabel("Number of Wins")
    plt.title("Dice Wins in 1000 Simulations")
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

plot_horizontal_bar(result)

