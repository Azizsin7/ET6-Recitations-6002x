# 🎲 Activity: Comparing Sample Estimates from Two Populations
## 💻 Code
```python
# -*- coding: utf-8 -*-
"""
Created on Thu May  1 13:36:58 2025

@author: somai
"""
import numpy as np
import random

np.random.seed(0)

# Create populations
low_var_pop = np.random.normal(loc=70, scale=5, size=1000)
high_var_pop = np.random.normal(loc=70, scale=20, size=1000)

# Sample
sample_size = 10
sample_low = random.sample(list(low_var_pop), sample_size)
sample_high = random.sample(list(high_var_pop), sample_size)

def summarize(sample):
    mean = np.mean(sample)
    sd = np.std(sample, ddof=1)
    margin = 1.96 * (sd / np.sqrt(len(sample)))
    ci_lower = mean - margin
    ci_upper = mean + margin
    return mean, sd, (ci_lower, ci_upper)

mean_low, sd_low, ci_low = summarize(sample_low)
mean_high, sd_high, ci_high = summarize(sample_high)

print("Low Variance Sample:")
print(f"Mean = {mean_low:.2f}, SD = {sd_low:.2f}, 95% CI = {ci_low}")
print("\nHigh Variance Sample:")
print(f"Mean = {mean_high:.2f}, SD = {sd_high:.2f}, 95% CI = {ci_high}")


import matplotlib.pyplot as plt
import seaborn as sns

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
## 💬 Sample Answers to Discussion Questions

---

### 1. Which confidence interval is wider? Why?

✅ The confidence interval for the **high-variance sample** is wider.

**Reason:**  
The standard deviation (SD) is higher in the high-variance population.  
Since CI is calculated as:

CI = mean ± 1.96 × (SD / √n)


A larger SD increases the **margin of error**, resulting in a **wider interval**.

---

### 2. What does this tell you about the relationship between variation and confidence?

✅ **More variation = less confidence** in your estimate from a small sample.

- High variation means your sample mean is less reliable.
- Confidence intervals widen to reflect this uncertainty.
- In contrast, low variation gives tighter, more trustworthy estimates.

---

### 3. How does the variation in the population affect the stability of the sample mean?

✅ High variation leads to **unstable sample means** across repeated samples.

- In high-SD populations, sample means jump around more.
- In low-SD populations, samples give more consistent estimates.
- This is why **low-CV data is more predictable**.

---

### 4. What would happen if we increased the sample size?

✅ Confidence intervals would become **narrower** for both distributions.

**Why?**

- The margin of error in the CI formula shrinks as `n` increases:
  
  Margin of error ∝ 1 / √n

- Larger samples reduce randomness and improve estimate accuracy.
- Even high-variance data becomes **more manageable** with more data.



