# 🎲 Activity: Comparing Sample Estimates from Two Populations
Facilitator: Somaia Zabihi  
Breakout Room Leaders: Ian and Raymon

---

## 🎯 Objective

In this activity, you will:

- Generate two different populations:
  - One with **low variation**
  - One with **high variation**
- Take random samples from each population
- Calculate:
  - Sample **mean**
  - Sample **standard deviation**
  - Approximate **95% confidence interval (CI)**
- Compare the results and discuss how variation affects your confidence in the estimates

---

## 📦 Quick Note on NumPy

We’ll use the Python library **NumPy** to simulate data and do math operations.

| NumPy Function       | What It Does                         |
|----------------------|---------------------------------------|
| `np.random.normal()` | Creates data from a normal distribution |
| `np.mean()`          | Calculates the average                |
| `np.std()`           | Calculates standard deviation         |

---

## 🧪 Steps

1. Complete and run the code provided below.
2. Observe the sample statistics from each population.
3. Discuss the results with your group.

---

## 💻 Code

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random

# Set random seed for consistency
np.random.seed(0)

# Step 1: Simulate two populations
# TODO: Create a population with mean ~70 and low variation (SD = 5)
low_var_pop = np.random.normal(loc=___, scale=___, size=___)

# TODO: Create a second population with the same mean but high variation (SD = 20)
high_var_pop = np.random.normal(loc=___, scale=___, size=___)

# Step 2: Draw 10 random samples from each population
# TODO: Sample 10 values from each population using random.sample
sample_size = ___
sample_low = random.sample(list(low_var_pop), sample_size)
sample_high = random.sample(list(high_var_pop), sample_size)

# Step 3: Define a function to compute mean, SD, and CI
def summarize(sample):
    # TODO: Calculate the sample mean using NumPy
    mean = ___
    
    # TODO: Calculate the sample standard deviation (use ddof=1)
    sd = ___
    
    # TODO: Compute margin of error using 1.96 * (SD / sqrt(n))
    margin = ___
    
    # TODO: Calculate CI lower and upper bounds
    ci_lower = ___
    ci_upper = ___
    
    return mean, sd, (ci_lower, ci_upper)

# Step 4: Analyze both samples
mean_low, sd_low, ci_low = summarize(sample_low)
mean_high, sd_high, ci_high = summarize(sample_high)

# Step 5: Print results
print("Low Variation Sample:")
print("Mean:", mean_low)
print("SD:", sd_low)
print("95% Confidence Interval:", ci_low)

print("\nHigh Variation Sample:")
print("Mean:", mean_high)
print("SD:", sd_high)
print("95% Confidence Interval:", ci_high)

# Already defined: sample_low, sample_high
# Already computed: mean_low, ci_low, mean_high, ci_high

# Low variance sample
plt.figure(figsize=(10, 4))
sns.histplot(sample_low, kde=True, color='skyblue', bins=8)
plt.axvline(mean_low, color='blue', linestyle='--', label='Mean')
plt.axvline(ci_low[0], color='gray', linestyle=':', label='95% CI bounds')
plt.axvline(ci_low[1], color='gray', linestyle=':')
plt.title("Low-Variance Sample Distribution")
plt.legend()
plt.show()

# High variance sample
plt.figure(figsize=(10, 4))
sns.histplot(sample_high, kde=True, color='salmon', bins=8)
plt.axvline(mean_high, color='red', linestyle='--', label='Mean')
plt.axvline(ci_high[0], color='gray', linestyle=':', label='95% CI bounds')
plt.axvline(ci_high[1], color='gray', linestyle=':')
plt.title("High-Variance Sample Distribution")
plt.legend()
plt.show()

```
## 💬 Discuss in Breakout Room

- Which confidence interval is wider? Why?
- What does this tell you about the connection between variation and confidence?
- How would your answer change if you increased the sample size?

👩‍🏫 Tip: Think carefully about how variation in the population influences sampling — this is the core takeaway!
