# Problem 1
# 15.0/15.0 points (graded)
# You are given a list of unique positive integers L sorted in descending order and a positive integer sum s. The list has n elements.
# Consider writing a program that finds values for multipliers m0,m1,...,mn−1 such that the following equation holds:
# s=L[0]∗m0+L[1]∗m1+...+L[n−1]∗mn−1
# Assume a greedy approach to this problem. You calculate the integer multipliers m_0, m_1, ..., m_(n-1) by finding the largest
# multiplier possible for the largest value in the list, then for the second largest, and so on. Write a function that returns the sum
# of the multipliers using this greedy approach. If the greedy approach does not yield a set of multipliers such that the equation above
# sums to s, return the string "no solution". Write the function implementing this greedy algorithm with the specification below:

def greedySum(L, s):
    """
    input: 
        s: positive integer, the target sum
        L: list of unique positive integers sorted in descending order
    Uses a greedy approach to solve:
        s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
    return: sum of multipliers if possible, else 'no solution'
    """
    multipliers = []
    remain = s

    for i in L:
        mult = remain // i
        multipliers.append(mult)
        remain -= i * mult

    if remain == 0:
        return sum(multipliers)
    else:
        return 'no solution'
    
print(greedySum([10, 5, 1], 14))  # 14 = 10*1 + 5*0 + 1*4 Output: 5
print(greedySum([10, 5, 1], 23))  # 23 = 10*2 + 5*0 + 1*3 Output: 5
print(greedySum([9, 6], 8))       # No solution 


