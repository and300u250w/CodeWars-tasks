from string import ascii_lowercase


# def alphabet_position(text):
#     new_list =""
#     for i in text.lower():
#         if i in ascii_lowercase:
#             new_list += str(ascii_lowercase.find(i)+1) + " "
            
#     return new_list.strip()


# Second solutiuon is:
def alphabet_position(text):
    for c in text.lower():
        if c.isalpha():
            print( ' '.join(str(ord(c) - 96) )

alphabet_position("The sunset sets at twelve o' clock.")

# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" as a string.

