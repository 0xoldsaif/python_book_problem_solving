'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
'''
def sum_ood_numbers(n):
    sum = 0
    for i in range(1,n):
        if i % 2 == 1:
            sum += i**2
        else:
            i += 1
            continue
    return sum
print(sum_ood_numbers(int(input('Put your num:  '))))
