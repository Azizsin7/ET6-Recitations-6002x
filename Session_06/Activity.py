import numpy as np
import random

# Set random seed for consistency
np.random.seed(0)

# Step 1: Simulate two populations
# TODO: Create a population with mean ~70 and low variation (SD = 5)
low_var_pop = np.random.normal(loc=___, scale=___, size=___)

# TODO: Create a second population with the same mean but high variation (SD = 20)
high_var_pop = np.random.normal(loc=___, scale=___, size=___)

# Step 2: Draw 10 random samples from each population
# TODO: Sample 10 values from each population using random.sample
sample_size = ___
sample_low = random.sample(list(low_var_pop), sample_size)
sample_high = random.sample(list(high_var_pop), sample_size)

# Step 3: Define a function to compute mean, SD, and CI
def summarize(sample):
    # TODO: Calculate the sample mean using NumPy
    mean = ___
    
    # TODO: Calculate the sample standard deviation (use ddof=1)
    sd = ___
    
    # TODO: Compute margin of error using 1.96 * (SD / sqrt(n))
    margin = ___
    
    # TODO: Calculate CI lower and upper bounds
    ci_lower = ___
    ci_upper = ___
    
    return mean, sd, (ci_lower, ci_upper)

# Step 4: Analyze both samples
mean_low, sd_low, ci_low = summarize(sample_low)
mean_high, sd_high, ci_high = summarize(sample_high)

# Step 5: Print results
print("Low Variation Sample:")
print("Mean:", mean_low)
print("SD:", sd_low)
print("95% Confidence Interval:", ci_low)

print("\nHigh Variation Sample:")
print("Mean:", mean_high)
print("SD:", sd_high)
print("95% Confidence Interval:", ci_high)
