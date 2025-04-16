# 🍷 Random Walk Simulation: Hidden Bug and Fix

This document explains a subtle but important bug in a random walk simulation using OOP in Python. The code simulates a "drunk" walking randomly and calculates how far they end up from the starting point.

---

## 🔍 Problem Overview

We use the following structure:

- `Location`: represents a 2D point.
- `Field`: keeps track of the `Drunk`'s location.
- `Drunk` / `UsualDrunk` / `ColdDrunk`: defines how the drunk walks.
- `walk()`: simulates one drunk's walk.
- `simWalks()`: simulates multiple walks.
- `drunkTest()`: reports the statistics.

---

## 🧪 The Hidden Bug in `simWalks()`

### ❌ Buggy Code:

```python
def simWalks(numSteps, numTrials, dClass):
    Homer = dClass()  # ⛔ Reused across all trials
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances
```
### 🚨 What's wrong?

- The **same `Drunk` object** (`Homer`) is reused for **every trial**.
- This breaks the **independence** between trials.
- While results might *look* fine, they are **not statistically correct**.

---

## 🧠 Why It’s a Problem

Each trial is supposed to simulate a **fresh start**:
- A new drunk starts at (0, 0)
- Walks a specific number of steps
- We record their final distance

But if we reuse the same `Drunk` object, we risk:
- Shared state across trials (in more complex simulations)
- Violating the principle of **independent trials**
- Incorrect results in case of future changes (e.g., memory-based walkers)

---

## ✅ Corrected Code

```python
def simWalks(numSteps, numTrials, dClass):
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        Homer = dClass() # ✅ New drunk for each trial
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances
```
- Each drunk is **fresh** and used for **only one walk**.

- Trials are now **statistically independent**.

- The results are **correct and reproducible**.

---

## 🎯 Results Comparison

After fixing the bug, you should see reasonable outputs:

| Steps  | Expected √N | UsualDrunk Mean | ColdDrunk Mean |
|--------|--------------|------------------|------------------|
| 1      | 1.0          | ~1.0             | ~1.0             |
| 10     | ~3.16        | ~2.9             | ~2.8             |
| 100    | ~10.0        | ~8.4             | ~9.6             |
| 1000   | ~31.6        | ~27.1            | ~53.5            |
| 10000  | ~100         | ~90.6            | ~495             |

---

## 🧭 Observations

- `UsualDrunk` follows √N growth as expected from an **unbiased 2D random walk**.
- `ColdDrunk` shows **faster displacement** due to a **vertical bias** in its step choices.

---

## 🧑‍🏫 Key Takeaways

- ✅ Always check whether your **simulations are independent**.
- ⚠️ Even if output *looks* correct, the **logic must match the model**.
- 🧪 Bugs in simulation code can be **subtle** and **statistically misleading**.
- 🔁 Re-initializing objects per trial is a **best practice** in stochastic simulations.

---

## 🧑‍🔬 Challenge for Learners

Try implementing a new `Drunk` type that remembers the last step taken:

```python
class MemoryDrunk(Drunk):
    def __init__(self, name=None):
        super().__init__(name)
        self.last_step = (0, 0)

    def takeStep(self):
        # 50% chance to repeat the last step, 50% chance random
        if random.random() < 0.5 and self.last_step != (0, 0):
            return self.last_step
        else:
            stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            self.last_step = random.choice(stepChoices)
            return self.last_step
```
Compare its drift against UsualDrunk. See what happens when you reuse this drunk vs. recreate it per trial!

