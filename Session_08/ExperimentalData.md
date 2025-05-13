# 🎓 Recitation #10 – MITx 6.00.2x

## 🧭 Topic: Curve Fitting, Linear Regression & Model Evaluation

## Main Objectives
- Understand how experimental data is analyzed using computational models.
- Fit curves (linear and polynomial) to data using least squares.
- Evaluate model accuracy using Mean Square Error (MSE) and R-squared (R2).
- Reflect on when higher-degree models are appropriate and when they lead to overfitting.

---

## Segment 1: Experimental Data and Hooke’s Law

**Concept**: Real-world data is noisy. We use models to estimate relationships between variables. Example: Hooke’s Law (F = -k * x)

**Goal**: Relate force (Newtons) to displacement (meters).

**Code Example**: Reading and plotting raw data

```python
def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    dataFile.readline()
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)

def plotData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals) * 9.81  # Convert mass to force
    yVals = pylab.array(yVals)
    pylab.plot(xVals, yVals, 'bo', label='Measured displacements')
```

---

## 🔹 Segment 2: Linear Regression with Least Squares (Spring Example)

### 📌 Concept
We fit a linear model of the form:

y = a * x + b

Using the **least squares method** to estimate `a` (slope) and `b` (intercept), which minimizes the total squared error between predicted and actual values.

### ⚙️ Real-World Example: Hooke’s Law (Spring Force)

**Hooke’s Law:**

F = -k * x

Where:
- `F` is the force applied to the spring (in Newtons)
- `x` is the displacement (stretch/compression in meters)
- `k` is the spring constant (N/m)


### ✅ Variable Roles

| Role                 | Variable   | Description                                                                 |
|----------------------|------------|-----------------------------------------------------------------------------|
| Independent Variable | `F`        | The force you apply (by hanging weights)                                   |
| Dependent Variable   | `x`        | The measured stretch of the spring in meters (changes based on the force)  |


### Interpreting the Regression Slope in Hooke’s Law
In our spring experiment, we're trying to understand how force affects displacement using Hooke’s Law:

```
𝐹 = 𝑘 * 𝑥 or rearranged: 𝑥 = 1/𝑘 * F
```
This tells us:

- When you apply more force (F), the spring stretches (x)
- The constant k (spring stiffness) determines how much stretch happens per unit of force

### 📊 What Does the Regression Line Tell Us?
In our regression model, we place:

- Force (F) on the x-axis (independent variable)

- Displacement (x) on the y-axis (dependent variable)

 When we fit a line:

       x= a* F+ b

The slope a from the regression line tells us how displacement changes with force, just like the 1/k in Hooke’s Law.

      a ≈ 1/K  ⇒ k ≈ 1/a
​

### 💻 Code Snippet: Fitting the Spring Data

```python
# Assume xVals = force values (F), and yVals = displacement values (x)
# Fit a linear model: y = a * x + b
a, b = pylab.polyfit(xVals, yVals, 1)
# Generate predicted values using the fitted model
estYVals = a * xVals + b

# Plot the data and the fitted line
# The slope 'a' corresponds to 1/k, so we compute k = 1 / a
pylab.plot(xVals, estYVals, 'r', label=f'Linear fit, k = {round(1/a, 5)}')

# Optionally: a cleaner version using polyval
model = pylab.polyfit(xVals, yVals, 1)        # model = [a, b]
estYVals = pylab.polyval(model, xVals)        # evaluates a*x + b for each x
```

### 📌 Interpretation

- This regression fits the equation:  
  	 `displacement = a * force + b`
- Based on Hooke’s Law:  
  	 `x = (1/k) * F` → `a ≈ 1/k`
- Therefore, we calculate the spring constant as:  
  	 `k = 1 / a`

---

## Segment 3: Model Evaluation with MSE and R-squared

**Concept**: Evaluate how good a model is using two metrics:
- Mean Square Error (MSE): Average of squared prediction errors.
- R-squared (R2): Proportion of data variance explained by the model.

**Code Example**: MSE

```python
def aveMeanSquareError(data, predicted):
    error = 0.0
    for i in range(len(data)):
        error += (data[i] - predicted[i])**2
    return error / len(data)
```
## 📏 R-squared (R²) – Coefficient of Determination

**Formula:**

R² = 1 - (SS_res / SS_tot)

Where:
- **SS_res** = ∑(yᵢ - ŷᵢ)² → sum of squared residuals (prediction errors)
- **SS_tot** = ∑(yᵢ - ȳ)² → total variance in the observed data

## 📏 Adjusted R-squared (R²) – Matching Code Implementation

**Formula:**

R² = 1 - (MSE / Var(y))

Where:
- **MSE** = Mean Squared Error = average of (yᵢ - ŷᵢ)²
- **Var(y)** = variance of observed values = average of (yᵢ - ȳ)²

**Explanation:**

- This form of R² still measures how much of the variance in the data is explained by the model.
- It’s mathematically equivalent to the standard formula but expressed in terms of **averages** instead of total sums.

Use this when your code uses `numpy.var(...)` and divides by the number of samples (n).



**Code Example**: R-squared

```python
# ⚠️ This version uses a simplified R² calculation.
# It is mathematically valid, but less transparent than the full SS_res / SS_tot formula.

def rSquared(observed, predicted):
    # Step 1: Calculate total squared error between predictions and actual values (SS_res)
    error = ((predicted - observed)**2).sum()
    
    # Step 2: Compute the mean squared error (MSE)
    meanError = error / len(observed)
    
    # Step 3: Divide MSE by variance of observed values (numpy.var returns SS_tot / n)
    # Then subtract from 1 to get R²
    return 1 - (meanError / numpy.var(observed))

```

---

## Caution: Overfitting

Higher-degree polynomials may improve R2 on training data but perform worse on new data.  
Visual cues and high R2 don't always indicate a good model — evaluate in context.

**Fitting multiple polynomial models**

```python
degrees = (2, 4, 8, 16)
models = genFits(xVals, yVals, degrees)
testFits(models, degrees, xVals, yVals, 'Mystery Data')
```

---

## Summary Table

| Tool / Term           | Purpose                                   | Code Usage                         |
|-----------------------|--------------------------------------------|------------------------------------|
| polyfit               | Fit polynomial (least squares)            | pylab.polyfit(x, y, degree)        |
| polyval               | Evaluate polynomial                       | pylab.polyval(model, xVals)        |
| aveMeanSquareError    | Compute Mean Square Error                 | Custom function                    |
| rSquared              | Compute R-squared                         | Custom function                    |
| Polynomial Degree     | Controls model complexity                 | degrees = (1, 2, 4, 8, 16)         |
