__author__ = 'taras'

from set_combinations import xuniqueCombinations

#Test correctness
assert list(xuniqueCombinations([1, 2, 3, 4], 2)) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

# Test amount of combinations
assert len(list(xuniqueCombinations([1, 2, 3, 4, 5], 3))) == 10


