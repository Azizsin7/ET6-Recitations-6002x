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

