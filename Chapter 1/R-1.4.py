'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
'''

def sum_of_squares(n):

    sum = 0
    print(n)
    for i in range(0 , n):
        sum += i**2
    return sum

def pass_num_to_above_function():
    n =  int(input('put ant positive num:  '))
    if n >= 0:
        return sum_of_squares(n)
    else:
        print('YOU SHOULD WRITE POSITIVE/CORRECT NUMBER')
        return pass_num_to_above_function()

print(pass_num_to_above_function())