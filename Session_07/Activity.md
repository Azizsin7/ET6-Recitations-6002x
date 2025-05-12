
# 🧪 Activity: Simulating the Central Limit Theorem in Python

### 🎯 Objective
To illustrate the **Central Limit Theorem (CLT)** through a Python-based simulation, helping you understand the behavior of **sample means**, and the relationship between **sample size**, **standard error**, and **confidence intervals**.

---

## 1️⃣ Generate a Non-Normal Population

Create a large synthetic dataset using a **non-normal distribution** such as:
- `exponential`
- `uniform`

You will use NumPy to generate the population data.

---

## 2️⃣ Sampling and Statistical Calculations

Choose several sample sizes (e.g., 10, 30, 50). For each sample size:

- Draw many **random samples** (e.g., 1000 samples).
- For each sample:
  - Calculate the **sample mean**
  - Store the mean to analyze its distribution
- Compute the **standard error** (SE) using the formula:

```
Standard Error (SE) ≈ sample standard deviation / sqrt(n)
```

---

## 3️⃣ Visualization

- Create a histogram showing the distribution of sample means for each sample size.
- Add **error bars** representing ±1 SE around the mean of the sample means using `plt.errorbar()`.

---

## 4️⃣ Observations and Discussion

- How does the **spread** of sample means change with larger sample sizes?
  <details>
  <summary>🔍 Show Answer</summary>
  In your simulation, the spread of the sample means (i.e., how wide the histogram is) becomes narrower as the sample size increases from 10 to 30 
  to 50.
  
  This is because:
  
  Larger samples reduce the impact of extreme values (which are common in an exponential distribution).
  
  Each larger sample gives a better estimate of the population mean, so the variability between sample means decreases.
  
  You can visually see this in your histograms — the one for sample size 10 is wider and more spread out, while the one for 50 is tighter around 
  the mean.
  </details>
  
- What do the **error bars** tell us about the **precision** of the sample mean?
  <details>
  <summary>🔍 Show Answer</summary>
  The error bars you plotted using plt.errorbar() show ±1 standard error (SE) around the average of the sample means.

  From the code:

  ```python
  std_err = np.std(sample_means, ddof=1) / np.sqrt(size)
  ```
  For larger sample sizes, this SE gets smaller. That means the sample mean is more precise — it’s closer to the true population mean more 
  consistently. So the error bars visually show us how confidence improves with more data per sample.


- How does this relate to the **Central Limit Theorem**?

  <details>
  <summary>🔍 Show Answer</summary>
  Even though your population data is exponentially distributed (highly skewed), the distribution of the sample means becomes approximately 
   normal — especially for larger sample sizes. This is exactly what the Central Limit Theorem (CLT) predicts:
  
  - Regardless of the original distribution, the distribution of sample means tends toward normal as sample size increases.
  
  - You can see this in your histograms: the shape of the sample mean distribution looks more bell-shaped as you go from size 10 → 30 → 50.
  
  - Also, the decrease in SE with increasing sample size matches the CLT’s prediction that:      SE ∝ 1 / √n

​


---

### 🧩 Python Tips

- Use `np.std()` to compute the standard deviation of sample means.
- Use `plt.hist()` to plot distributions.
- Use `plt.errorbar()` to add ±1 SE bars to your graph.

