'''
Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes
a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
'''
import random
def choice_(seq):
    correct_num = random.randrange(min(seq),(max(seq)+1))
    if correct_num in seq:
       return correct_num
    else:
        return choice_(seq)
while True:
    print(choice_([1,2,5]))

#[int(x) for x in input().split()]