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
# 🎯 Monte Carlo Simulation: Estimating π Code

### 👉 Core Idea:
- Generate random (x, y) points inside the square using:
  ```python
  x = random.random()
  y = random.random()


