def square_digits(num):
    z  = ""
    for x in str(num):
        z+= str(int(x)**2)
    return int(z)

print(square_digits(9119))