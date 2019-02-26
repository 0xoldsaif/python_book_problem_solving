'''
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
'''
def is_even(k):
    while True:
        if k==0:
            print('True = even ')
            break
        elif k==1:
            print('False = ood')
            break
        k=k-2
#     x1=k//2
#     x2=(k+1)//2
#     if x1==x2:
#         print('True = Even ')
#     else:
#         print('False = ood ')
is_even(int(input('put num : ')))
