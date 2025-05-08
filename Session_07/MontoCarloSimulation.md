# 🎲 Monte Carlo Simulation & Estimating π 

## 🎰 What is a Monte Carlo Simulation?

- A **Monte Carlo simulation** estimates unknown values by running **many random experiments**.
- It’s named after the **Monte Carlo casino** because it involves randomness and chance.
- Invented in 1946 by **Stanislaw Ulam** while recovering from illness and playing solitaire.

---

## 💡 Why Use Monte Carlo Methods?

- Some problems are **too complex for exact math**.
- Monte Carlo lets us simulate the problem and **use results from random samples** to estimate the answer.
- Useful in physics, games, finance, AI, and more.

---

## 🧪 Estimating π with Random Sampling

### 🟦 Step-by-Step Setup:
- Imagine a **square** of side length 2 with a **circle** of radius 1 inside it.
- Areas:
  - Square: 2 × 2 = **4**
  - Circle: π × 1² = **π**

### 🎯 Drop Random Points
- Drop many points **randomly** into the square.
- Count how many land **inside the circle**.

### 📐 Formula:
```text
π ≈ 4 × (number of points in the circle / total number of points)
```
### 🎬 What Happened in the Video?
- They tried to estimate π by shooting arrows at a paper target.
- They missed the circle, or all landed in the same place.
- The experiment wasn’t random or independent, so the estimate was bad.

### 🎓 Lesson:
- Monte Carlo simulations work only if trials are truly random and independent. 
- That’s why we write code instead of relying on real-world randomness (like needles or arrows).

## ✅ Key Takeaways

| Concept                   | Meaning                                                             |
|---------------------------|----------------------------------------------------------------------|
| Monte Carlo Simulation    | Use of repeated random sampling to estimate values                  |
| Randomness & Independence | Critical for valid simulation results                               |
| Estimating π              | Use ratio of circle points to square points to estimate π           |
| Simulation > Manual Methods | Code is faster, more accurate, and easier to repeat               |

---
# 🎯 Monte Carlo Simulation: Estimating π 

### Core Idea:
- Generate random (x, y) points inside the square using:
  
  ```python
  x = random.random()
  y = random.random()
  
  ```
- Check if the point lies inside the circle:

  ```python
  if (x**2 + y**2)**0.5 <= 1.0
  ```
- If it does, count it. Then estimate π using:
  ```python
  pi ≈ 4 × (points inside circle / total points)
  ```
### 🔁 Code Snapshot: Simulating Needle Drops
```python

def throwNeedles(numNeedles):
    inCircle = 0
    for _ in range(numNeedles):
        x, y = random.random(), random.random()
        if (x**2 + y**2)**0.5 <= 1:
            inCircle += 1
    return 4 * (inCircle / numNeedles)
```
### 📏 Getting a Confident Estimate
To avoid guessing how many points to simulate, we:
- Run multiple trials with the same number of needles
- Compute the average and the standard deviation (SD) of the estimates
- Repeat with more needles until the SD is small enough
```python
def getEst(numNeedles, numTrials):
    estimates = [throwNeedles(numNeedles) for _ in range(numTrials)]
    sDev = numpy.std(estimates)
    curEst = sum(estimates) / len(estimates)
    return curEst, sDev
```
We aim for a 95% confidence interval:

```python

while sDev >= precision / 1.96:
```
## 🔍 Why More Needles Help

| Needles | Std Dev ↓ | Estimate of π → Closer to true value?               |
|---------|------------|------------------------------------------------------|
| Fewer   | High       | Sometimes closer, but unreliable                    |
| More    | Low        | Even if the estimate is slightly off, it’s more trustworthy |


Even if one estimate with fewer needles looks better, it has a wider range of uncertainty.

## ⚠️ Confidence vs. Correctness

Low standard deviation (SD) means the simulation results are **consistent**, so we have **high confidence** in the estimate.

But confidence ≠ correctness.

> A simulation can be **precise but wrong** if the logic or formula is incorrect.

### 🧪 Example:
If you mistakenly compute π like this:
```python
return 2 * (inCircle / totalPoints)
```
Instead of 
```python
return 4 * (inCircle / totalPoints)
```
- You’ll get values close to π / 2, with low variation.
- This gives you high confidence in the wrong result.

## 🧠 Takeaway:
- Always validate your simulation logic using known values or sanity checks.
- Being consistently wrong is worse than being uncertain.

