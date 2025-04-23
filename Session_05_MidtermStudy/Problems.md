# 🧮 GreedySum Activity – Problem 1

This activity explores the concept of **greedy algorithms** in solving linear integer equations. It is designed to help you understand how greedy strategies can be applied and where they might fail.

---

## 📝 Problem Description

You are given:
- A list `L` of **unique positive integers**, sorted in **descending order**
- A **target sum** `s`, which is a positive integer

You are asked to find a list of integer multipliers `m_0, m_1, ..., m_{n-1}` such that:

s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_{n-1]


Use a **greedy approach** to find these multipliers:
- Start with the largest number in the list (`L[0]`) and choose the **maximum multiplier** that doesn't exceed the remaining target `s`
- Repeat this for each subsequent value in `L`

🎯 **Goal**: Return the **sum of all multipliers**.

❗ If the greedy strategy fails to reach `s` exactly, return:

"no solution"


---

## ✅ Example

```python
L = [25, 10, 1]
s = 41
```
Greedy selection:

- 25 × 1 → 25 → remaining: 16

- 10 × 1 → 10 → remaining: 6

- 1 × 6 → 6 → remaining: 0

Final multipliers: [1, 1, 6] → Sum = 8 ✅


## ❌ When Greedy Fails
There are cases where greedy won’t find the correct solution even if one exists. That’s why we need to verify the result by checking if the constructed sum really equals s.

---
# 📊 Problem 2 – Maximum Contiguous Subsequence Sum (Kadane's Algorithm vs Brute Force)

This problem explores how to find the maximum sum of a **contiguous subsequence** from a list of integers that includes both positive and negative numbers.

---

## 🔍 Problem Summary

You are given a list of integers and must find the **maximum sum of any contiguous subsequence**.

Examples:
- `[3, 4, -1, 5, -4]` → max sum is `3 + 4 - 1 + 5 = 11`
- `[3, 4, -8, 15, -1, 2]` → max sum is `15 - 1 + 2 = 16`

---

## ❗ Misconception Clarified

Some may think brute-force generates the power set and should have **O(2^N)** complexity.  
But in this problem:

> ✅ The brute-force solution only considers **contiguous subsequences**, not the power set.

---

## 📈 Time Complexity Comparison

| Approach                     | Candidate Space             | Time Complexity |
|------------------------------|-----------------------------|-----------------|
| Power set brute-force        | All subsets (non-contiguous) | O(2^N)          |
| Contiguous brute-force       | Only contiguous subsequences | O(N²)           |
| Kadane’s Algorithm (greedy)  | Only contiguous subsequences | O(N)            |

---

## 🧠 Why brute-force is O(N²) here:

The number of contiguous subsequences in a list of size **N** is:

N * (N + 1) / 2


- Choose a start index (N options)
- Choose an end index (up to N options)
- So, total contiguous ranges = O(N²)

That’s why the brute-force approach for this problem is **quadratic**, not exponential.


---

## 💬 Student Tip

Kadane’s algorithm is greedy: it makes local decisions (start new or extend previous subsequence) and tracks the max sum along the way.  
This is why it solves the problem in **linear time**, even though the naive method takes **quadratic time**.


