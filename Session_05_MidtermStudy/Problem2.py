# 0/1 point (graded)
# There are 2 parts to this problem on this page!

# Consider a list of positive (there is at least one positive) and negative numbers. You are asked to find the maximum sum of a
# contiguous subsequence. For example,
# - in the list [3, 4, -1, 5, -4], the maximum sum is 3+4-1+5 = 11
# - in the list [3, 4, -8, 15, -1, 2], the maximum sum is 15-1+2 = 16
# One algorithm goes through all possible subsequences and compares the sums of each contiguous subsequence with the largest sum it has
# seen. What is the time complexity of this algorithm in terms of the length of the list, N?


# Problem 2
# 20.0/20.0 points (graded)
# Write a function that meets the specification below.
def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    max_ending_here = max_so_far = L[0]
    for i in L[1:]:
        max_ending_here = max(i, max_ending_here + i)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

max_contig_sum([1, 2, 3, 4]) # 10
max_contig_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) #6
max_contig_sum([-1, 2, 3, -4]) #5
