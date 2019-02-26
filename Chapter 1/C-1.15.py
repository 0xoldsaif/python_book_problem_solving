'''
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
'''
# set(iteral) that rearrange numbers from smaller to bigger

def all_are_different(seq):
    if len(seq)==len(set(seq)):
        result = print('different Numbers')
        return result
    else:
        result = print('is not distincit numbers')
        return result
all_are_different([x for x in input().split()])
