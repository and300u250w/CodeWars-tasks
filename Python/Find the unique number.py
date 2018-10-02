# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
# findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
# It’s guaranteed that array contains more than 3 numbers.

# The tests contain some very huge arrays, so think about performance.

# This is the first kata in series:

# Find the unique number (this kata)
# Find the unique string
# Find The Unique

from collections import Counter

def find_uniq(arr):

    return Counter(arr).most_common()[-1][0]


find_uniq([ 1, 1, 1, 2, 1, 1 ])
# === 2
find_uniq([ 0, 0, 0.55, 0, 0 ])
# === 0.55
find_uniq([ 3, 10, 3, 3, 3, 10, 2, 8, 9 ])
#, 10)

# def find_uniq(arr):
#     a, b = set(arr)
#     return a if arr.count(a) == 1 else b