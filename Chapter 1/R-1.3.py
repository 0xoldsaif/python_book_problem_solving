'''
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
'''
def minmax(sequence):
    largest_num =sequence[0]
    smallest_num = sequence[0]
    results = ()
    # print(len(sequence))
    for i in range(0,len(sequence)):
        if largest_num <= sequence[i]:
            largest_num = sequence[i]
            # print(largest_num)
        if smallest_num >= sequence[i]:
            smallest_num = sequence[i]
    else:
        largest = results + (largest_num,)
        smallest = results + (smallest_num,)
    return largest + smallest


minimax=minmax([int(x) for x in input().split()])
print(minimax)


