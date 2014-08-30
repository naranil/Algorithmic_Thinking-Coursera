__author__ = 'taras'

def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc