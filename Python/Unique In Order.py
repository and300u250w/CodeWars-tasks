# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:


def unique_in_order(iterable):
    second_index = ""
    new_table = []
    for i in iterable:
        if i != second_index:
            new_table.append(i)
            second_index = i
    print(new_table)
        

        

unique_in_order('AAAABBBCCDAABBB')
#  == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')
#          == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])
#       == [1,2,3]