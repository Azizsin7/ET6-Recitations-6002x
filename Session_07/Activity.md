
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

\[
SE = \frac{\text{standard deviation of sample means}}{\sqrt{n}}
\]

---

## 3️⃣ Visualization

- Create a histogram showing the distribution of sample means for each sample size.
- Add **error bars** representing ±1 SE around the mean of the sample means using `plt.errorbar()`.

---

## 4️⃣ Observations and Discussion

- How does the **spread** of sample means change with larger sample sizes?
- What do the **error bars** tell us about the **precision** of the sample mean?
- How does this relate to the **Central Limit Theorem**?

---

### 🧩 Python Tips

- Use `np.std()` to compute the standard deviation of sample means.
- Use `plt.hist()` to plot distributions.
- Use `plt.errorbar()` to add ±1 SE bars to your graph.

