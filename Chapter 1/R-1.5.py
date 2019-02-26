'''
Give a single command that computes the sum from Exercise R-1.4, relying
on Python’s comprehension syntax and the built-in sum function
'''
print(sum([int(x) for x in input().split()]))