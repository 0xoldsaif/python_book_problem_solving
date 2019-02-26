'''
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
'''
def product_odd(seq):
    num = 1
    odd_num = 0
    for i in range(0,len(seq)):
        odd_num = seq[i] + seq[i+num]
        if odd_num % 2 == 1:
            print(i)
            result = "%s and %s its product is %s that is an odd number"%(seq[i] , seq[i+num] , odd_num)

        else:
            num += 1
            continue
        return result
print(product_odd([int(x) for x in input().split()]))




