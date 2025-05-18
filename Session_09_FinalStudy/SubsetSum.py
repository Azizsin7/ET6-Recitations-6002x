import numpy as np
import itertools

def find_combination(choices, total):
    """(list of ints, int) -> array
    
    choices: a non-empty list of ints
    total: a positive int
    
    Returns a numpy.array of length len(choices) such that
        * each element of result is 0 or 1
        * sum(result * choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result * choices) closest to total without going over.
    """
    
    # Try to find combinations that exactly match the total
    for i in range(1, len(choices) + 1):
        for seq in itertools.combinations(enumerate(choices), i):
            if sum(x[1] for x in seq) == total:
                result = np.zeros(len(choices), dtype=int)
                for index, _ in seq:
                    result[index] = 1
                return result

    # If no exact match is found, pick the closest sum without exceeding the total
    best_result = None
    closest_sum = 0
    
    for i in range(1, len(choices) + 1):
        for seq in itertools.combinations(enumerate(choices), i):
            current_sum = sum(x[1] for x in seq)
            if current_sum <= total and current_sum > closest_sum:
                closest_sum = current_sum
                best_result = np.zeros(len(choices), dtype=int)
                for index, _ in seq:
                    best_result[index] = 1

    return best_result

# Example usage:
print(find_combination([1], 10))                             #array([1])
print(find_combination([1, 81, 3, 102, 450, 10], 9))         #array([1, 0, 1, 0, 0, 0])
print(find_combination([10, 100, 1000, 3, 8, 12, 38], 1171)) #array([1, 1, 1, 1, 1, 1, 1])
print(find_combination([1,1,3,5,3], 5))                      #array([0, 0, 0, 1, 0])
print(find_combination([1,2,2,3], 4))                        #array([0, 1, 1, 0]) or array([1, 0, 0, 1])
