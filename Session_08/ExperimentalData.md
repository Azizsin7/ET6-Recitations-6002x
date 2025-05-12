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

---

### ⚙️ Real-World Example: Hooke’s Law (Spring Force)

**Hooke’s Law:**

F = -k * x

Where:
- `F` is the force applied to the spring (in Newtons)
- `x` is the displacement (stretch/compression in meters)
- `k` is the spring constant (N/m)

---

### ✅ Variable Roles

| Role                 | Variable   | Description                                                                 |
|----------------------|------------|-----------------------------------------------------------------------------|
| Independent Variable | `F`        | The force you apply (by hanging weights)                                   |
| Dependent Variable   | `x`        | The measured stretch of the spring in meters (changes based on the force)  |

Because:
- The slope of the regression line `a` ≈ displacement / force →  
- Then:  
  \[
  k = \frac{F}{x} = \frac{1}{a}
  \]

### In Data Terms

| Role            | Variable      | Why                            |
|-----------------|---------------|---------------------------------|
| Independent (X) | Force (F)      | You apply different values      |
| Dependent (Y)   | Displacement (x) | You observe the result          |



---

### 💻 Code Snippet: Fitting the Spring Data

```python
a, b = pylab.polyfit(xVals, yVals, 1)  # Linear regression: y = a*x + b
estYVals = a * xVals + b

pylab.plot(xVals, estYVals, 'r', label=f'Linear fit, k = {round(1/a, 5)}')
```
Or using polyval() for cleaner prediction:

```python
model = pylab.polyfit(xVals, yVals, 1)
estYVals = pylab.polyval(model, xVals)
```
### 📌 Interpretation
The fitted line represents how displacement (x) changes with applied force (F).
From the slope, we can calculate the spring constant k as:

k= 1/a

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

**Code Example**: R-squared

```python
def rSquared(observed, predicted):
    error = ((predicted - observed)**2).sum()
    meanError = error / len(observed)
    return 1 - (meanError / numpy.var(observed))
```

**Fitting multiple polynomial models**

```python
degrees = (2, 4, 8, 16)
models = genFits(xVals, yVals, degrees)
testFits(models, degrees, xVals, yVals, 'Mystery Data')
```

---

## Caution: Overfitting

Higher-degree polynomials may improve R2 on training data but perform worse on new data.  
Visual cues and high R2 don't always indicate a good model — evaluate in context.

---

## Summary Table

| Tool / Term           | Purpose                                   | Code Usage                         |
|-----------------------|--------------------------------------------|------------------------------------|
| polyfit               | Fit polynomial (least squares)            | pylab.polyfit(x, y, degree)        |
| polyval               | Evaluate polynomial                       | pylab.polyval(model, xVals)        |
| aveMeanSquareError    | Compute Mean Square Error                 | Custom function                    |
| rSquared              | Compute R-squared                         | Custom function                    |
| Polynomial Degree     | Controls model complexity                 | degrees = (1, 2, 4, 8, 16)         |
