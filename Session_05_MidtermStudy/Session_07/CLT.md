# 🧪 Why Did the Empirical Rule Work?

- Empirical Rule works for **normal distributions**
- But how about other types of distribution?
- Spins of a **roulette wheel** are **not normally distributed**
- They are **uniformly distributed** (each outcome equally probable)
- However, we reason not about a **single spin**, but the **mean of a set of spins**
- And the **Central Limit Theorem (CLT)** applies

---

## 🔶 Theoretical Concept: Central Limit Theorem (CLT)

> The CLT says:  
> If you take **many samples** from **any population** (even if not normal),  
> compute the **mean** of each sample,  
> and plot those means — the result will be a **normal distribution** (bell curve),  
> **If the sample size is large enough.**

### ✅ Key Takeaways:
- Applies to **sample means**, not raw values
- Works even if original data is **uniform, skewed**, etc.
- The larger the sample, the more the average results look like a bell-shaped (normal) curve.

---

## 🎯 Summary Table

| Scenario            | Distribution Shape | Std Dev   | Why                        |
|---------------------|--------------------|-----------|-----------------------------|
| 1 die               | Uniform            | High (~1.4) | Not sampling average        |
| Mean of 50 dice     | Normal             | Low (~0.2) | CLT in action               |
| Roulette 1 spin     | Skewed             | High       | High variance               |
| Mean of 200 spins   | Almost normal      | Low        | CLT + large sample          |

---

## 🔁 `plotMeans(...)` Function – CLT in Action

```python
def plotMeans(numDice, numRolls, numBins, legend, color, style):
    means = []
    for i in range(numRolls // numDice):         # Repeat many trials
        vals = 0
        for j in range(numDice):                 # Each trial rolls 'numDice' times
            vals += 5 * random.random()          # Each roll is a random value between 0 and 5
        means.append(vals / float(numDice))      # Compute the sample mean
```
This loop simulates what CLT is all about:

> “If we take many random samples (each of size numDice) from a uniform distribution and compute the mean of each sample,
> the distribution of those sample means will be approximately normal, especially when numDice is large.”

## 📊 CLT Visualization
```python
pylab.hist(means, numBins, color=color, label=legend,
           weights=pylab.array(len(means) * [1]) / len(means),
           hatch=style)
```
- Weights ensure the histogram shows probability, not raw count
- This line visualizes the distribution of sample means
- It should look normal (bell curve), even though the original die is uniform

## 💡 CLT Code Summary

| Code Element                          | CLT Concept                             |
|--------------------------------------|------------------------------------------|
| `for i in range(numRolls // numDice)` | Take many samples                        |
| `for j in range(numDice)`             | Each sample has `n` observations         |
| `vals += 5 * random.random()`         | Draw random values from uniform dist     |
| `means.append(vals / float(numDice))` | Compute sample mean                      |
| `pylab.hist(means, ...)`              | Plot the sample mean distribution        |

---
## 🎲 Difference Between numDice and numRolls
🔢 numDice = Number of dice per trial
- Controls the sample size
- Each trial rolls numDice times and averages the result

Examples: 
- numDice = 1 → 1 die → 1 number → 1 sample mean
- numDice = 50 → 50 dice → averaged → 1 sample mean

🔁 numRolls = Total dice rolled across all trials
Controls the total number of samples collected

# 🎲 Understanding the Difference Between `numDice` and `numRolls`

In the `plotMeans(...)` function, two key parameters determine how sampling is done:


## 🔢 `numDice` — Number of Dice Per Trial

- This controls the **sample size**.
- In **each trial**, we roll `numDice` times and compute the **average** of those rolls.
- This average is one **sample mean**.

### 📌 Examples:
- `numDice = 1`:  
  → Roll 1 die → Get 1 number → That number *is* the sample mean

- `numDice = 50`:  
  → Roll 50 dice → Compute average of 50 values → That’s your sample mean

So, a **larger `numDice`** gives a **more stable average**, which is what the CLT describes.

---

## 🔁 `numRolls` — Total Dice Rolled Across All Trials

- This sets the **total number of dice rolled** during the whole simulation.
- It determines **how many trials (samples)** we can perform.

### 🧮 Relationship:
```python
numTrials = numRolls // numDice
```
That is:

- If we want to roll numRolls = 1000 dice in total
- And we roll numDice = 10 dice per trial
- Then:
  
```python
  numTrials = 1000 // 10 = 100
```
→ We perform 100 trials, and we compute 100 sample means

## 🧠 Full Example:
```python

numDice = 10
numRolls = 1000
```
- Total dice rolled = 1000
- Dice per trial = 10
- Number of trials = 1000 // 10 = 100
- So, we compute 100 sample means → plotted in a histogram

## 📝 Summary Table

| Parameter   | Meaning                   | Affects                                      |
|-------------|----------------------------|----------------------------------------------|
| `numDice`   | Sample size in each trial | Std. deviation of sample means ↓ with size   |
| `numRolls`  | Total dice to roll        | Number of trials (how many histogram bars)   |






