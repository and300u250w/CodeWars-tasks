import math

def row_sum_odd_numbers(n):
    # x = []
    # for i in range(1,n*n+n,2):
    #     x.append(i)
    # print (sum(x[-n:]))

    print (n**3)



#              1 b 
#           3 b+c    5 b+c+c
#        7 b+c+c+c     9 b+c+c+c+c    11 b+c+c+c+c+c
#    13    15    17    19
# 21    23    25    27    29
# ...

# row_sum_odd_numbers(1)
# row_sum_odd_numbers(2)
row_sum_odd_numbers(3)
row_sum_odd_numbers(4)
row_sum_odd_numbers(5)