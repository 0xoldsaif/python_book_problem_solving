'''
Give a single command that computes the sum from Exercise R-1.6, relying
on Python’s comprehension syntax and the built-in sum function.
'''
print(sum([int(x**2) for x in range(1,int(input())) if x % 2 == 1]))