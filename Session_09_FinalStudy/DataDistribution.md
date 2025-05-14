### Problem: Data Distrbution 
Consider the following code:
```python
import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals
```
For each of the following questions, select the best answer from the set of choices.

### Problem 1:
The values in tVals are most closely:
1. Uniformly distributed
2. Distributed with a Gaussian distribution
3. Exponentially distributed

<details>
  <summary>Click to view answer</summary>
  
   - **Answer**: The values in `tVals` are most closely **distributed with a Gaussian distribution**.
    - Since `tVals` is the sum of three uniform distributions, by the **central limit theorem**, the resulting distribution will approach a Gaussian (normal) distribution.
</details>

### Problem 2:
The values in xVals are most closely:
1. Uniformly distributed
2. Distributed with a Gaussian distribution
3. Exponentially distributed

<details>
  <summary>Click to view answer</summary>
  
  - **Answer**: The values in `xVals` are most closely **uniformly distributed**.
    - The values in `xVals` are generated using `random.random()`, which produces values uniformly distributed between 0 and 1. Doubling the values does not affect the uniformity but scales the range to between 0 and 2.
</details>
