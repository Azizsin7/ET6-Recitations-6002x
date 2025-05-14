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






    # If no exact match is found, pick the closest sum without exceeding the total => APPLY GREEDY 



   
# Example usage:
print(find_combination([1], 10))                             #array([1])
print(find_combination([1, 81, 3, 102, 450, 10], 9))         #array([1, 0, 1, 0, 0, 0])
print(find_combination([10, 100, 1000, 3, 8, 12, 38], 1171)) #array([1, 1, 1, 1, 1, 1, 1])
print(find_combination([1,1,3,5,3], 5))                      #array([0, 0, 0, 1, 0])
print(find_combination([1,2,2,3], 4))                        #array([0, 1, 1, 0]) or array([1, 0, 0, 1])
