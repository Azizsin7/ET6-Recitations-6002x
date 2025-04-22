# 🎓 Recitation #4 – MITx 6.00.2x

## 🧭 Topic:Stochastic Thinking & Random Walks

# 🎯Definition
 🧠 **A stochastic process is simply a process that includes randomness. Instead of predicting one fixed outcome, we simulate many possible outcomes —
based on probability.**


## 🔹 Stochastic Processes

- Involve **randomness** and **uncertainty**
- Useful for modeling real-world phenomena where outcomes are not deterministic
- Contrast:
  - **Deterministic processes** → Predictable given initial conditions
  - **Stochastic processes** → Involve variability even with same inputs

---

## 🔹 Simulation Models

- Simulations imitate real-world processes computationally
- Allow us to explore system behaviors under different conditions
- Especially powerful when dealing with stochastic processes

---

## 🔹 Hand Simulation of Homer’s Random Walk

### 🧭 One-Step Walk:
- Homer can move in 4 directions: {E, W, N, S}
- After one step, he is guaranteed to be **1 unit** away from the origin
- **Probability:** 100%
 
<p align="center">
  <img src=https://github.com/MIT-Emerging-Talent/ET6-Recitations-6002x/blob/main/Session_04/images/1unit.png alt="Homer 1-Step Breakdown" width="450"/>
</p>

---

### 🍷 Two-Step Walk:
Don’t lose the generality.
  
 • Calculation breakdown:
 
 • Probability of being 0 units away from the origin: 25%.
 
 • Reason: Homer can return to the origin by moving in the opposite direction from the first step 
 
(e.g., if the first step was east, the second step is west).

Sample space: 
- S2 = { (E,E), **(E,W)**, (E,N), (E,S), **(W,E)**, (W,W), (W,N), (W,S), (N,E), (N,W), (N,N), **(N,S)**, (S,E), (S,W), **(S,N)**, (S,S) }

- 4/16 = 1/4 = 25%
  <p align="center">
  <img src="https://github.com/MIT-Emerging-Talent/ET6-Recitations-6002x/blob/main/Session_04/images/2unit.png">
</p>

---

## Two-Step Analysis (Move in the same direction)

- Probability of being 2 units away from the origin: 25%.
- Reason: Homer moves two units in the same direction as the first step  
  (e.g., two steps east or two steps west).
- Sample space:
- S2 = {**(E, E)**, (E, W), (E, N), (E, S), (W, E), **(W, W)**, (W, N), (W, S), (N, E), (N, W), **(N, N)**, (N, S), (S, E), (S, W), (S, N), **(S, S)** }

- 4/16 = 1/4 = 25%

---

## 📐Two-Step Analysis (Move in perpendicular direction)

- Probability of being √2 units away from the origin: 50%.
- Reason: Homer moves in a direction perpendicular to the first step  
  (e.g., if the first step was east, the second step is north or south).
- Sample space:
- S2 = {(E, E), (E, W), **(E, N)**, **(E, S)**, **(W, E)**, (W, W), **(W, N)**, **(W, S)**, **(N, E)**, **(N, W)**, (N, N), (N, S), **(S, E)**, **(S, W)**, (S, N), (S, S) }
- 8/16 = 1/2 = 50%
  
 <p align="center">
  <img src="https://github.com/MIT-Emerging-Talent/ET6-Recitations-6002x/blob/main/Session_04/images/2unit_prependicular.png">
</p>



---

## 📏 Distance Categories from the Origin

| Distance        | Count | Probability | Explanation |
|-----------------|-------|-------------|-------------|
| **0 units**     | 4     | 4/16 = 25%  | Homer returns to the origin by reversing the first step. Examples: (E, W), (W, E), (N, S), (S, N) |
| **2 units**     | 4     | 4/16 = 25%  | Homer moves in the same direction twice. Examples: (E, E), (W, W), (N, N), (S, S) |
| **√2 units**    | 8     | 8/16 = 50%  | Homer takes two perpendicular steps. Examples: (E, N), (N, W), (W, S), etc. |

---

## 📏 Expected Distance After Two Steps

We compute the expected value using the formula:
- 𝟐𝟓% × 𝟎 + 𝟐𝟓%× 2 + 5𝟎% × √𝟐 = 𝟏.𝟐 units


- After taking 100 or 1000 steps, how far is he from the origin in terms of units?




