#12)  Python Program to Sum of Three Given Integers (If Two are Equal, Sum is Zero):
def sum_three(x, y, z):
    if x == y or y == z or x == z:
        return 0
    return x + y + z
    print (sum_three(1,1,3)) # Two are equal
    # print (sum_three(1,2,3)) # Two are not equal
