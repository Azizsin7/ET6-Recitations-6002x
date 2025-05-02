# 🧠 Inferential Statistics & Probability


---

## 📘 Overview

This session introduces essential statistical concepts for understanding how data varies, how we can make predictions based on samples, and how to analyze that variation using mean, standard deviation, confidence intervals, and sampling distributions.

---

## 📊 1. Inferential Statistics

- Use sample data to make generalizations about a population.
- Helps with estimating unknown parameters (e.g., population mean) and testing hypotheses.
- Based on **random sampling** and **probability theory**.

---

## 📈 2. Law of Large Numbers (LLN)

- The more trials you run, the closer your **empirical (observed)** probability will approach the **theoretical** one.
- Example: flipping a coin 10 times vs. 1000 times — the proportion of heads will stabilize around 0.5 as trials increase.

---

## 📉 3. Regression to the Mean

> **Real-life example (student-focused)**:  
> A student scores **very low** on their first exam. Due to effort or natural variation, they are likely to score **closer to average** on the second exam.  
> Similarly, an **extremely high** score may be followed by a more average one.  
> This is **not** because performance must balance out — it's a statistical tendency for extreme outcomes to move toward the mean over time.

### ⚠️ Don’t confuse with **Gambler’s Fallacy**:
| Concept | Description |
|--------|-------------|
| **Regression to the Mean** | Extreme values are likely to be followed by more typical ones due to randomness. |
| **Gambler’s Fallacy** | Incorrect belief that past outcomes influence future ones (e.g., “tails is due”). |

---

## 📐 4. Variation in Data

- How variable is the data?
- More **variation → less reliable** the mean estimate from a small sample.
- Smaller variation → faster convergence to the true mean.

---

## 📊 5. Mean and Standard Deviation

- **Mean (µ)**: average value of a dataset.
- **Standard Deviation (σ)**: how far data values are spread around the mean.
  - Low SD → data is clustered
  - High SD → data is spread out

---

## 🔄 6. Coefficient of Variation (CV)

- CV = Standard Deviation ÷ Mean
- **Dimensionless** (no units) → useful for comparing variability across datasets with different scales.
- Example:
  - Data A: Mean = 50, SD = 5 → CV = 0.1
  - Data B: Mean = 100, SD = 10 → CV = 0.1
  - Equal relative variation, even though absolute SD differs.

---

## 🧪 7. Confidence Interval (CI)

- Provides a **range of values** that likely includes the population parameter.
- Based on **sampling variability**.
- Common CI: 95% → "We are 95% confident that the population mean lies within this range."

---

## 📏 8. Empirical Rule (for Normal Distribution)

- 68% of values fall within **±1 SD**
- 95% within **±2 SD**
- 99.7% within **±3 SD**

Helps to construct confidence intervals and interpret normal distributions.

---

## 📦 9. Types of Data Distributions

| Distribution | Example | Shape |
|--------------|---------|-------|
| **Uniform** | Rolling a fair die | Flat |
| **Normal** | Heights, test scores | Bell curve |
| **Exponential** | Time between radioactive decays | Right-skewed |

Understanding distribution shape helps determine which tools (e.g., CI, SD) are appropriate.

---

## 🎲 10. Application: Longest Run Simulation (Activity Preview)

- Simulate random outcomes (like dice rolls)
- Analyze variation across repeated samples
- Visualizes key concepts like:
  - Sampling
  - Random variation
  - Empirical distribution

---

## 📌 Summary of Key Takeaways

- Sampling introduces uncertainty — **we need tools like SD, CI, and CV** to quantify it.
- **Larger samples** reduce uncertainty.
- **Extreme results are likely to normalize** over repeated measurements (regression to the mean).
- **Visualizing distributions** helps us make better inferences from data.

---

> 📢 *Next up*: Apply these ideas in code! Open the activity notebook to simulate sampling and visualize results.
