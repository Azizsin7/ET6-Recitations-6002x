# 📘 Sampling, Standard Error, and Confidence Intervals

## 🎯 Learning Objectives
- Understand why a single sample can still be useful for inference if it is random and sufficiently large.
- Explain how **standard error** relates to sample size and variability in sample means.
- Use Python simulations to visualize how sample means are distributed and how confidence intervals change.
- Interpret histograms and error bars as tools for statistical reasoning.

---

## 🧪 Part 1: Is One Sample Enough?

In Segment 1, we saw that a single random sample happened to have a mean and standard deviation close to the population's. In Segment 2, we test if this was **luck or something predictable**.

We use the Central Limit Theorem (CLT):

> When we take many random samples, their means form a normal distribution centered around the true population mean.

```python
population = getHighs()
sampleSize = 200
numSamples = 1000
sampleMeans = []

for i in range(numSamples):
    sample = random.sample(population, sampleSize)
    sampleMeans.append(sum(sample) / len(sample))
```

Here, we take 1000 random samples (each size 200) from real temperature data and store their means.

---

## 📊 Part 2: Visualizing Sample Means and the Population Mean

We now plot the distribution of sample means and compare it to the true population mean:

```python
makeHist(sampleMeans, 'Means of Samples', 'Mean', 'Frequency')
pylab.axvline(x=popMean, color='r')  # Red line shows the population mean
```

This histogram shows:
- Sample means form a **bell-shaped curve**
- The red line (population mean) lies near the center
- This confirms what the CLT predicts

---

## 🧮 Part 3: Standard Error – How Much Do Sample Means Vary?

Next, we measure how *spread out* the sample means are:

```python
print('Standard deviation of sample means =', round(numpy.std(sampleMeans), 3))
```

This value is the **standard error (SE)**:

> A smaller SE means the sample mean is more tightly clustered around the population mean.

We also track the maximum deviation between sample and population stats:

```python
print('Maximum difference in means =', round(maxMeanDiff, 3))
print('Maximum difference in standard deviations =', round(maxSDDiff, 3))
```

---

## 📉 Part 4: Error Bars and Confidence Intervals

What happens when we increase **sample size**? Does it improve accuracy?

This function simulates multiple sample sizes and visualizes their 95% confidence intervals:

```python
def showErrorBars(population, sizes, numTrials):
    ...
    pylab.errorbar(xVals, sizeMeans,
                   yerr=1.96 * pylab.array(sizeSDs), fmt='o',
                   label='95% Confidence Interval')
    ...
    pylab.axhline(y=popMean, color='r', label='Population Mean')
```

To run the visualization:

```python
showErrorBars(population, (50, 100, 200, 300, 400, 500, 600), 50)
```

📌 You will observe:
- All sample means stay close to the red population line.
- **Larger sample sizes** → **narrower error bars** → **more precise estimates**

---

## ✅ Key Takeaways

| Concept               | Why It Matters                                                   |
|-----------------------|------------------------------------------------------------------|
| Sample Mean           | Used to estimate the population mean                            |
| Standard Error (SE)   | Measures variability of sample means                            |
| Confidence Interval   | Tells how sure we are about our estimate                        |
| Larger Sample Size    | Decreases SE and narrows confidence intervals                   |
| Central Limit Theorem | Explains why sample means form a normal distribution            |

---



## 👩‍🏫 Instructor Notes

- Emphasize interpretation over syntax
- Reinforce the CLT with visual evidence
- Let students draw links to real-world polling or surveys
