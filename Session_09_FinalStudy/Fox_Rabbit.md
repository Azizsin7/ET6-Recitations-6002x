# Fox and Rabbit Population Simulation 

For this problem you are going to simulate growth of fox and rabbit population in a forest!

The following facts are true about the fox and rabbit population:

- The maximum population of rabbits is determined by the amount of vegetation in the forest, which is relatively stable.

- There are never fewer than 10 rabbits; the maximum population of rabbits is 1000.

  For each rabbit during each time step, a new rabbit will be born with a probability of

$$
p_{rabbit\ birth} = 1 - \frac{CURRENTRABBITPOP}{MAXRABBITPOP}
$$

In other words, when the current population is near the maximum, the probability of giving birth is very low, and when the current population is small, the probability of giving birth is very high.

- The population of foxes is constrained by number of rabbits. There are never fewer than 10 foxes.

- At each time step, after the rabbits have finished reproducing, a fox will try to hunt a rabbit with success rate of

$$
p_{fox\ eats\ rabbit} = \frac{CURRENTRABBITPOP}{MAXRABBITPOP}
$$

In other words, the more rabbits, the more likely a fox will eat one.

- If a fox succeeds in hunting, it will decrease the number of rabbits by 1 immediately. Remember that the population of rabbits is never lower than 10.

Additionally, if a fox succeeds in hunting, then it has a 1/3 probability of giving birth in the current time-step.

If a fox fails in hunting then it has a 10 percent chance of dying in the current time-step.

- If the starting population is below 10 then you should do nothing. You should not increase the population nor set the population to 10. 

Start with 500 rabbits and 30 foxes.

At the end of each time step, record the number of foxes and rabbits.

Run the simulation for 200 time steps, and then plot the population of rabbits and the population of foxes as a function of time step. (You do not need to paste your code for plotting for Part A of this problem).

Use the following steps, and the template file rabbits.py (click to download .py file), as guides in your implementation of this simulation.

**Step 1:** Write the procedure, rabbitGrowth, that updates the number of rabbits during the first part of a time step

**Step 2:** Write the procedure, foxGrowth, that updates the number of rabbits and foxes during the second part of a time step

**Step 3:** Write the master procedure, runSimulation, that loops for some amount of time steps, doing the first part and then the second part of the simulation. Record the two populations in two different lists, and return those lists.

Paste your code for the three functions rabbitGrowth, foxGrowth, and runSimulation in the following box.

**WARNING**
DO NOT define the global variables MAXRABBITPOP, CURRENTRABBITPOP, or CURRENTFOXPOP in this box. We alter the values of these variables to test your code. If you define the variables in this box, you may overwrite our values, causing your code to be marked incorrect.

**CLARIFICATIONS / HINTS**
"See Full Output": If you are getting the line "0 10" in your output for "Test 4 foxGrowth" then for this particular test, your code changes the CURRENTFOXPOP (increases it if the fox population has gone below the minimum fox population), which is not the right behavior -- the code should not reset CURRENTFOXPOP.
It is not correct to assume that there is a 1/3 chance that the population increases in "Test 3 foxGrowth". Pay special attention to the following statement in the docstring of foxGrowth(): "Each fox, based on the probabilities in the problem statement, may eat one rabbit (but only if there are more than 10 rabbits)."

---
### Problem 1:

Enter the code for the functions rabbitGrowth, foxGrowth, and runSimulation below.

```python
import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    pass
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    pass
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    pass


```

## Problem 2: At some point in time, there are more foxes than rabbits.

- True
- False

<details>
  <summary>Answer</summary>
  True
  
  **Explanation:** In predator-prey dynamics, it is possible for the number of foxes to exceed the number of rabbits for a brief period. As foxes consume rabbits, the fox population can temporarily outnumber the rabbit population, especially in early stages of the simulation or when the prey (rabbits) decreases rapidly.
</details>

---

## Problem 3: The polyfit curve for the rabbit population is:

- A straight line
- A concave up curve (looks like a U shape)
- A concave down curve (looks like a ∩ shape)
- An exponentially decreasing curve
- An exponentially increasing curve
- None of the above

<details>
  <summary>Answer</summary>
  - **Answer:** A concave up curve (looks like a U shape)
  
  **Explanation:** The rabbit population grows rapidly initially, but as it approaches the maximum capacity of the environment (carrying capacity), growth slows down. This results in a **concave up** shape (U-shaped curve).
</details>

---

## Problem 4: The polyfit curve for the fox population is:

- A straight line
- A concave up curve (looks like a U shape)
- A concave down curve (looks like a ∩ shape)
- An exponentially decreasing curve
- An exponentially increasing curve
- None of the above

<details>
  <summary>Answer</summary>
  - **Answer:** A concave down curve (looks like a ∩ shape)
  
  **Explanation:** The fox population grows when the rabbit population increases, but as the rabbit population declines due to predation, the fox population decreases. This leads to a **concave down** shape (∩-shaped curve) for the fox population.
</details>

---

## Problem 5: 
Changing the initial conditions from 500 rabbits and 30 foxes to 50 rabbits and 300 foxes changes the general shapes of both the polyfit curves for the rabbit population and fox population.

- True
- False

<details>
  <summary>Answer</summary>
  - **Answer:** False
  
  **Explanation:** Changing the initial conditions will affect the **rate** of population changes, but the **general shapes** of the curves remain the same. The rabbit population will still follow a **concave up (U-shaped)** curve, and the fox population will still follow a **concave down (∩-shaped)** curve.
</details>

---

## Problem 6: 
Let's say we make a change in the original simulation. That is, we are going to change one detail in the original simulation, but everything else will remain the same as it was explained in Problem 8 - Part A. Now, if a fox fails in hunting, it has a 90 percent chance of dying (instead of a 10 percent chance, as in the original simulation). Changing the probability of an unsuccessful fox dying from 10% to 90% changes the general shapes of both the polyfit curves for the rabbit population and fox population.

- True
- False

<details>
  <summary>Answer</summary>
  - **Answer:** False
  
  **Explanation:** Although changing the death rate of foxes will cause the fox population to decline faster, it will not change the **general shapes** of the curves. The rabbit population will still have a **concave up (U-shaped)** curve, and the fox population will still have a **concave down (∩-shaped)** curve.
</details>

