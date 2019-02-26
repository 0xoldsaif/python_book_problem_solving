'''
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
'''
def opposite_list(seq):
    seq_ = []
    for i in range(-len(seq),0):
        seq_.append(-i)
    return seq_
print(opposite_list([int(x) for x in input().split()]))
