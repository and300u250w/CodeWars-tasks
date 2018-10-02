# def is_square(n):
#     if n > 0 and n % (pow(n,0.5)) == 0:
#         # print ("True")
#         return True
#     elif n == 0:
#         # print("True")
#         return True
#     else:
#         # print ("False")
#         return False;


        
def is_square(n):
    if n >= 0:
        if int(n**.5)**2 == n:
            return True
    return False



is_square(-1);''' False '''
is_square(0);''' True '''
is_square(3);''' False '''
is_square(4);''' True '''
is_square(25); ''' True '''
is_square(26); ''' False '''

# # ''' The best Practice '''
# def is_square(n):
#     if n >= 0:
#         if int(n**.5)**2 == n:
#             return True
#     return False
