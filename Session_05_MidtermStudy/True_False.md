
# 🧠 Midterm Review – Practice Questions

These practice questions cover key concepts that may appear on the midterm.  
Try each question before expanding the hidden answers.

---

## 📌 Midterm Tips

- Review lecture recordings, especially the ones that introduce new problem-solving strategies.
- Understand not just **what** the answer is, but also **why** it's correct.
- Pay special attention to:
  - Stochastic vs deterministic behavior
  - Brute-force vs optimized approaches
  - Graph theory basics
  - Python’s random module behavior

---


## 📚 Table of Contents

1. [Problem 1 – Stochastic Function & Int Cast](#problem-1)  
2. [Problem 2 – Random Seed for Reproducibility](#problem-2)  
3. [Problem 3 – Brute Force & Knapsack](#problem-3)  
4. [Problem 4 – Seeding in Loops](#problem-4)  
5. [Problem 5 – Graph & Shortest Path](#problem-5)  
6. [Problem 6 – Probability of Rolling 6s](#problem-6)  
7. [Problem 7 – Greedy Algorithms](#problem-7)  
8. [Problem 8 – BFS in Weighted Graphs](#problem-8)  
9. [Problem 9 – Deterministic Functions (F & G)](#problem-9)

---

## ❓ Problem 1  
<a name="problem-1-1"></a>  
**The following function is stochastic:**  
```python
def f(x):
    # x is an integer
    return int(x + random.choice([0.25, 0.5, 0.75]))
```

**Level:** ⭐  
**Tags:** `#random` `#typecasting` `#stochastic`

<details>
<summary>🔎 Answer & Explanation</summary>

**❌ Answer: False**  
**Explanation:**  
Although `random.choice()` is random, each option rounds down to 0 when cast to `int`, so the output is always just `x`. This makes it **deterministic**, not stochastic.

</details>

---

## ❓ Problem 2  
<a name="problem-1-2"></a>  
**In Python, we can use `random.seed(100)` at the beginning of a program to generate the same sequence of random numbers each time we run the program.**

**Level:** ⭐  
**Tags:** `#random` `#reproducibility`

<details>
<summary>🔎 Answer & Explanation</summary>

**✅ Answer: True**  
**Explanation:**  
Seeding the random number generator ensures the same sequence of values across runs — this is crucial for testing and debugging stochastic processes.

</details>

---

## ❓ Problem 3  
<a name="problem-1-3"></a>  
**A brute force solution to the 0/1 knapsack problem will always produce an optimal solution.**

**Level:** ⭐⭐  
**Tags:** `#bruteforce` `#knapsack` `#optimization`

<details>
<summary>🔎 Answer & Explanation</summary>

**✅ Answer: True**  
**Explanation:**  
Brute-force tries all possible combinations of items, so it’s guaranteed to find the best one — though it’s computationally inefficient.

</details>

---

## ❓ Problem 4  
<a name="problem-1-4"></a>  
**The following function is stochastic:**  
```python
import random

def A():
    mylist = []
    r = 1

    if random.random() > 0.99:
        r = random.randint(1, 10)
    for i in range(r):
        random.seed(0)
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
    print(mylist)
```

**Level:** ⭐⭐  
**Tags:** `#random` `#stochastic` `#seed`

<details>
<summary>🔎 Answer & Explanation</summary>

**❌ Answer: False**  
**Explanation:** Despite using random.random() initially, the seed is reset inside the loop, making the outcome consistent every time. The condition for r rarely changes, and even if it does, it produces deterministic output due to the fixed seed.
</details>


---

## ❓ Problem 5  
<a name="problem-1-5"></a>  
**Consider an undirected graph with non-negative weights that has an edge between each pair of nodes. The shortest distance between any two nodes is always the path that is the edge between the two nodes.**

**Level:** ⭐⭐  
**Tags:** `#graphs` `#shortestpath` `#weights`

<details>
<summary>🔎 Answer & Explanation</summary>

**❌ Answer: False**  
**Explanation:**  
Even in a fully connected graph, an indirect path may be shorter if its total weight is smaller. Direct edges are not always the shortest.

</details>

---

## ❓ Problem 6  
**What is the exact probability of rolling at least two 6's when rolling a die three times?**

**Level:** ⭐⭐⭐  
**Tags:** `#probability` `#combinatorics`

<details>
<summary>🔎 Answer & Explanation</summary>

**✅ Answer: 2/27**  
**Explanation:**  
## 📝 Summary of Steps – Probability of Rolling at Least Two 6s (3 rolls)

1. **Total Outcomes:**
   - When rolling a die 3 times, there are:
6 × 6 × 6 = 216 total possible outcomes.


---

2. **Break into Cases:**

- **Case A:** Exactly **two 6s**.  
- **Case B:** Exactly **three 6s**.

---

3. **Case A: Exactly two 6s**

- **Step 1:** Choose **2 positions** for the 6s:
C(3, 2) = 3 ways

- **Step 2:** The **remaining position** must **not be a 6**:
  - Possible values = **1, 2, 3, 4, 5** → **5 options**.

- **Total outcomes for Case A:**
3 × 5 = 15 favorable outcomes

---

4. **Case B: Exactly three 6s**

- Only **one outcome**:
(6, 6, 6)


---

5. **Total favorable outcomes:**
15 (Case A) + 1 (Case B) = 16


---

6. **Calculate the probability:**
Probability = favorable / total = 16 / 216 = 2 / 27

</details>

---

## ❓ Problem 7  
**A greedy optimization algorithm is typically efficient in time.**

**Level:** ⭐  
**Tags:** `#greedy` `#efficiency`

<details>
<summary>🔎 Answer & Explanation</summary>

**✅ Answer:True**  
**Explanation:**  
Greedy algorithms are designed to make local optimal choices at each step, usually resulting in low computational cost. However, they don't always produce globally optimal solutions.

</details>

---

## ❓ Problem 8  
**Suppose you have a weighted directed graph and want to find a path between nodes A and B with the smallest total weight.**  
**Select the most accurate statement:**

**If all edges have weight 2, breadth-first search guarantees that the first path found is the shortest path.**

**Level:** ⭐⭐  
**Tags:** `#graphs` `#BFS` `#shortestpath`

<details>
<summary>🔎 Answer & Explanation</summary>

**✅ Answer: True**  
**Explanation:**  
If all edge weights are equal, finding the path with the fewest edges is equivalent to finding the path with the least total weight. BFS guarantees the shortest path in unweighted (or uniformly weighted) graphs.

</details>

---

## ❓ Problem 9  
**Which of the following functions are deterministic?**
```python
import random

def F():
    mylist = []
    r = 1

    if random.random() > 0.99:
        r = random.randint(1, 10)
    for i in range(r):
        random.seed(0)
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            if number not in mylist:
                mylist.append(number)
    print(mylist)

def G():  
    random.seed(0)
    mylist = []
    r = 1

    if random.random() > 0.99:
        r = random.randint(1, 10)
    for i in range(r):
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
            print(mylist)
```

**Level:** ⭐⭐  
**Tags:** `#random` `#deterministic` `#seed`

<details>
<summary>🔎 Answer & Explanation</summary>

**✅ Answer: Both F and G**  
**Explanation:**  
- `F()` resets the seed inside the loop — every time producing the same random values.
- `G()` sets the seed once, and all randomness is reproducible from that seed.
So both functions produce the **same output every run**, making them **deterministic**.

</details>
